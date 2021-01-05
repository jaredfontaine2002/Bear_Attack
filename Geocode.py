from typing import Dict

import pandas as pd
import requests
import json
import os

from main import df_col

# read csv

#print(df_col)


#API Call and get the lat. and long values
for i, row in df_col.iterrows():
    apiAddress = str(df_col.at[i, 'City']) + str(df_col.at[i, 'State'])

    parameters: Dict[str, str] = {
        'key': os.environ.get('API_KEY'),
        'location': apiAddress
        }

    response = requests.get('http://www.mapquestapi.com/geocoding/v1/batch', params=parameters)
    print(response.text)
    data = json.loads(response.text)['results']

# Get the Lat and Lng of all the bear attacks

    lat = data[0]['locations'][0]['latLng']['lat']
    lng = data[0]['locations'][0]['latLng']['lng']

    df_col.at[i, 'lat'] = lat
    df_col.at[i, 'lng'] = lng


        # save data to CSV
    df_col.to_csv('Bear_Geo.csv')

'''
response = requests.get('https://opendata.arcgis.com/datasets/a27014d0f6e84e3082da209995a1285f_2.geojson')

Florida_data = json.loads(response.text)
bob = Florad{ "Type": "Point",
    "coordinates" : [0] },
print(bob)
#lat = Florida_data.Points
#print(lat)



#print(Florida_data)

lat = Florida_data'coordinates'
print(lat) '''