#!/usr/bin/python

import requests
import json
import random

response = requests.get('http://trivia-api.thedundies.com/questions/')

# TM doesn't send back a json object that's recognized as a dict by python.
# It shows as a list 
# Strip off the leading [ and trailing ] 
# Now python sees this as a dict 
# Proceed to get individual sections. 
sanatized_response = response.text.lstrip("[").rstrip("]")

json_data = json.loads(sanatized_response)

# print the question id
print (json_data["question_id"])

# print the question 
print (json_data["question"])

# print the answers and correct value 
print (json_data["answers"][0]["answer"], json_data["answers"][0]["correct"])
print (json_data["answers"][1]["answer"], json_data["answers"][1]["correct"])
print (json_data["answers"][2]["answer"], json_data["answers"][2]["correct"])
print (json_data["answers"][3]["answer"], json_data["answers"][3]["correct"])

print ("")
print ("")

# Number zero is always true. I need to shuffle them a bit. 
number = [0,1,2,3]
random.shuffle(number)

for i in number:
    #print (i)
    print (json_data["answers"][i]["answer"], json_data["answers"][i]["correct"])
