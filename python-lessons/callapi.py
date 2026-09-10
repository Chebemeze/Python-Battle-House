import requests
import json

try:
    response = requests.get("https://iss-api.polluxlabs.io/iss-pass?lat=4.8242&lon=7.0336")
    #HAndling error in from the response
    if response.status_code != 200:
        raise ConnectionError()
    #inspecting the structure of the dictionary
    with open("library.json", "w") as file:
        json.dump(response.json(), file, indent=4)
except ConnectionError:
    print("Enter a valid name of city")
