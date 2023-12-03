# API description: https://www-genesis.destatis.de/genesis/online?Menu=Webservice

import requests

# Base URL of the API
api_url = "https://www-genesis.destatis.de/genesisWS/rest/2020/data/tablefile"

# Parameters to be sent with the request
params = {
    "username": "DENP664828",
    "password": "Password1!!!",
    "name": "12711-0022",
    "area": "all",
    "compress": "false",
    "transpose": "false",
    "startyear": "2022",
    "endyear": "2022",
    "timeslices": "",
    "regionalvariable": "",
    "regionalkey": "",
    "classifyingvariable1": "NAT",
    "classifyingkey1": "*",
    "classifyingvariable2": "GES",
    "classifyingkey2": "*",
    "classifyingvariable3": "BLDHK1",
    "classifyingkey3": "*",
    "format": "csv",
    "job": "false",
    "stand": "01.01.1970",
    "language": "de"
}

# Constructing GET request
response = requests.get(api_url, params=params)

# Check if the request was successful
if response.ok:
    # Define filename for downloaded file
    filename = "dmig2022.csv"

    # Write response content to file
    with open(filename, 'wb') as file:
        file.write(response.content)

    # Output message if successful
    print(f"{filename} successfully downloaded.")
else:
    # Output message if failed
    print("Error:", response.status_code)