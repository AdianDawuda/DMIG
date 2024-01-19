import geopandas as gpd
import pandas as pd
from geoalchemy2 import Geometry
from shapely.geometry import MultiPolygon, Polygon
from sqlalchemy import Integer, Float, create_engine
from sqlalchemy import text

import parameters

# Set parameters
year = parameters.year
username = parameters.username
password = parameters.password
host = parameters.host
port = parameters.port
dbname = parameters.dbname
table_name = parameters.table_name
schema = parameters.schema

# Load CSV as df
df = pd.read_csv(f'dmig{year}.csv',
                 sep=';',
                 header=None,
                 skiprows=[0, 1, 2, 3, 4, 5, 6, 7, 297, 298, 299],
                 names=['from', 'to', 'g_male', 'g_female', 'g_total', 'f_male', 'f_female', 'f_total', 'male_total', 'female_total', 'total'],
                 encoding='utf-8')
# Forward fill 'from' column (removes NaN values)
df['from'] = df['from'].ffill()

# Remove irrelevant columns
df.drop(['g_male', 'g_female', 'g_total', 'f_male', 'f_female', 'f_total', 'male_total', 'female_total'], axis=1, inplace=True)
# Remove total count rows
df = df[df['from'] != 'Insgesamt']
df = df[df['to'] != 'Insgesamt']
# Remove rows where from==to (no data)
df = df[df['from'] != df['to']]

# Load GeoJSON as gdf
gdf = gpd.read_file('NUTS_L1.geojson')
# Remove irrelevant columns
gdf.drop(['id', 'NUTS_ID', 'LEVL_CODE', 'NUTS_NAME', 'MOUNT_TYPE', 'URBN_TYPE', 'COAST_TYPE', 'FID'], axis=1, inplace=True)
# Remove non-germany rows
gdf = gdf[gdf['CNTR_CODE'] == 'DE']
# Convert all geometries to multipolygon
gdf['geometry'] = gdf['geometry'].apply(lambda geom: MultiPolygon([geom]) if isinstance(geom, Polygon) else geom)

# Create dictionary for gdf state names and state geometries
geometry_dict = gdf.set_index('NAME_LATN')['geometry'].to_dict()
# Map geometries to df
df['to_geom'] = df['to'].map(geometry_dict)
df['from_geom'] = df['from'].map(geometry_dict)

# Calculate centroids and extract x, y coordinates for 'from_geom'
df['from_geom_centroid'] = df['from_geom'].apply(lambda geom: geom.centroid if geom is not None else None)
df['from_centroid_x'] = df['from_geom_centroid'].apply(lambda c: c.x if c is not None else None)
df['from_centroid_y'] = df['from_geom_centroid'].apply(lambda c: c.y if c is not None else None)

# Calculate centroids and extract x, y coordinates for 'to_geom'
df['to_geom_centroid'] = df['to_geom'].apply(lambda geom: geom.centroid if geom is not None else None)
df['to_centroid_x'] = df['to_geom_centroid'].apply(lambda c: c.x if c is not None else None)
df['to_centroid_y'] = df['to_geom_centroid'].apply(lambda c: c.y if c is not None else None)

# Convert df to gdf
gdf = gpd.GeoDataFrame(df, geometry='to_geom')
# Add from_geom as geometry type
gdf = gdf.set_geometry('from_geom')
# Set gdf crs
gdf = gdf.set_crs('epsg:4326', inplace=True)

# Define PostGIS database connection
engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{dbname}')

# Write gdf to PostGIS database
gdf.to_postgis(
    con=engine,
    name= table_name,
    schema=schema,
    if_exists='replace',
    dtype={
        'to_geom': Geometry(geometry_type='MULTIPOLYGON', srid=4326),
        'from_geom': Geometry(geometry_type='MULTIPOLYGON', srid=4326),
        'total': Integer,
        'to_centroid_x': Float,
        'to_centroid_y': Float,
        'from_centroid_x': Float,
        'from_centroid_y': Float
    }
)

# Add Primary key to table
try:
    with engine.connect() as conn:
        query = f"ALTER TABLE {schema}.dmig{year} ADD COLUMN id SERIAL PRIMARY KEY;".format(dbname)
        conn.execute(text(query))
        conn.commit()
except Exception as e:
    print(f"Error: {e}")
