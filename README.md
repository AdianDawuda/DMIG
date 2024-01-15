# Domestic Migration in Germany

![DMIG logo](https://git.sbg.ac.at/s1093093/dmig/-/raw/main/display_images/dmig.png)

This Project aims to build a spatial data infrastructure of yearly German domestic migration data. The migration data will be sourced from the German GENESIS (Gemeinsames Neues Statistisches Informations-System) online platform. The German State boundary geodata will be sourced separately from the Eurostat online platform and combined with the migration data in a PostGIS geodatabase. The process of downloading and preprocessing the aforementioned data will be highly automated with Python scripts. Using Geoserver, WFS/WMS of the data will be created and incorporated into a dashboard. The dashboard will also include external services to aid in visualization (e.g., basemap) and will enable the interactive visualization of data from different years. In addition to the spatial visualization, data not depicted on the map will also be shown in panels of the dashboard.

## Wiki

The project's wiki can be found [here](https://git.sbg.ac.at/s1093093/dmig/-/wikis/DMIG-Wiki). It provides more in-depth information about the project, its status, and how to replicate the results.

## License

See the [LICENSE](https://git.sbg.ac.at/s1093093/dmig/-/blob/main/LICENSE) file for license rights and limitations ([GPL v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)).