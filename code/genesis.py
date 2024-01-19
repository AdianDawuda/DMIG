from requests import get

from parameters import year, genesis_uname, genesis_passwd

# API description: https://www-genesis.destatis.de/genesis/online?Menu=Webservice
# Base URL of the API
api_url = 'https://www-genesis.destatis.de/genesisWS/rest/2020/data/tablefile'

# Parameters to be sent with the request
params = {
    'username': f'{genesis_uname}',
    'password': f'{genesis_passwd}',
    'name': '12711-0022',
    'area': 'all',
    'compress': 'false',
    'transpose': 'false',
    'startyear': year,
    'endyear': year,
    'timeslices': '',
    'regionalvariable': '',
    'regionalkey': '',
    'classifyingvariable1': 'NAT',
    'classifyingkey1': '*',
    'classifyingvariable2': 'GES',
    'classifyingkey2': '*',
    'classifyingvariable3': 'BLDHK1',
    'classifyingkey3': '*',
    'format': 'csv',
    'job': 'false',
    'stand': '01.01.1970',
    'language': 'de'
}

# Constructing GET request
response = get(api_url, params=params)

# Check if the request was successful
if response.ok:
    # Define filename for downloaded file
    filename = f'dmig{year}.csv'

    # Write response content to file
    with open(filename, 'wb') as file:
        file.write(response.content)

    # Output message if successful
    print(f'{filename} successfully downloaded.')
else:
    # Output message if failed
    print('Error:', response.status_code)