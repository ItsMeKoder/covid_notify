#!/bin/python3

import json
import requests

from config import State
url="https://covid19.cloudeya.org/dec2020"

payload = {}
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3RhcGkxIiwiaWF0IjoxNjA4NjI1NTU1LCJleHAiOjE2MDg4MjU1NTV9.bJ1nVSJct6At1GG4dl-cXXgnz_MpA7D7kyIbACf9jhQ'
}

response = requests.request("GET", url, headers=headers, data = payload)
json_dat=response.text


with open('./cases.json','w')as json_file:
    json_file.write(json_dat)


main=""

json_file=open('./cases.json','r')
latest=json.load(json_file)['Document']

state_r=latest[0]["province_state"]

global n

n = 0

while state_r != State and n!=43736:
  n += 1
  state_r = latest[n]["province_state"]
  state_i=latest[n]

print(state_i)


state=state_i["combined_key"]
deaths=state_i["deaths"]
confirmed=state_i["confirmed"]
recovered=state_i["recovered"]
active=state_i["active"]
cases= "State : "+str(state)+"\nDeaths : "+str(deaths)+"\nConfirmed : "+str(confirmed)+"\nRecovered : "+str(recovered)+"\nActive : "+str(active)
print("cases")
