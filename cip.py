import json
import requests
from bps_restpy.bps import BPS, pp


file_path = "./result.json"
url = "https://api.criminalip.io/v1/banner/search?query=title%3Aixia+labs&offset=0"

payload={}
headers = {
  "x-api-key": "<YOUR_API_KEY>"
}

#response = requests.request("GET", url, headers=headers, data=payload)

#json_data = json.loads(response.text)

#with open(file_path, 'w') as outfile:
#    json.dump(json_data, outfile, indent=2)

with open(file_path, "r") as json_file:
    json_data = json.load(json_file)

for jdata in json_data["data"]["result"]:

    

    bps_system  = jdata["ip_address"]
    bpsuser     = 'admin'
    bpspass     = 'admin'

    print("target: ",bps_system)
    ########################################
    ########################################
    # Login to BPS box
    bps = BPS(bps_system, bpsuser, bpspass)
    print(bps.login())
    print(bps.logout())
    break


