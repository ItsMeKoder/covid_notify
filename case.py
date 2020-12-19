#!/bin/python3

import json
import requests


url="https://covid19.cloudeya.org/dec2020"

payload = {}
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3RhcGkxIiwiaWF0IjoxNjA4MzYyMjU1LCJleHAiOjE2MDg1NjIyNTV9.IKDx4yHOaoIZhzni4zmp2tIAc1my4amCV0oA-zVMaXs'
}

response = requests.request("GET", url, headers=headers, data = payload)
json_dat=response.text


with open('./cases.json','w')as json_file:
    json_file.write(json_dat)

json_file=open('./cases.json','r')
latest=json.load(json_file)['Document'][258]
state=latest["combined_key"]
deaths=latest["deaths"]
confirmed=latest["confirmed"]
recovered=latest["recovered"]
active=latest["active"]
cases= "State : "+str(state)+"\nDeaths : "+str(deaths)+"\nConfirmed : "+str(confirmed)+"\nRecovered : "+str(recovered)+"\nActive : "+str(active)
#print("cases")
