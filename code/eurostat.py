# API description: https://gisco-services.ec.europa.eu/distribution/v2/nuts/

import requests

# Full GISCO API URL
url = "https://gisco-services.ec.europa.eu/distribution/v2/nuts/geojson/NUTS_RG_10M_2021_3857_LEVL_1.geojson"

# Constructing GET request
response = requests.get(url)

# Check if the request was successful
if response.ok:
    # Define filename for downloaded file
    filename = "NUTS_L1.geojson"

    # Write response content to file
    with open(filename, 'wb') as file:
        file.write(response.content)

    # Output message if successful
    print(f"{filename} successfully downloaded.")
else:
    # Output message if failed
    print("Error:", response.status_code)