#!/usr/bin/python

import requests
import json

response = requests.get('http://trivia-api.thedundies.com/questions/')

json_data = json.loads(response.text)

#print (json.dumps(j, indent = 4, sort_keys = True))

print (type(json_data))

print (response.json().get("question"))

#new comment