# Assignment 3 : CSO
# Author Anna Lozenko

#Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, and stores it into a file called "cso.json".

import requests
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"
response = requests.get(url)

#test response status code
print(f"Response Status Code: {response.status_code}")
# test response headers
print(f"Response Header: {response.headers}")

# store the data in a file called "cso.json"
with open("cso.json", "w") as jsonfp:
    json.dump(response.json(), jsonfp, indent=4)

# function that retrieves data from an API and stores it into a file with a given filename.
def save_to_json(filename, url):
    response = requests.get(url)
    data = response.json()
    print(f"Response Status Code: {response.status_code}")
    if response.status_code == 200:
        with open(filename, "w") as jsonfp:
            json.dump(data, jsonfp, indent=4)
    else:
        print("Failed to retrieve data from the API")

save_to_json("cso.json", "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en")



