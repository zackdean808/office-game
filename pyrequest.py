#!/usr/bin/python

import requests
import json
import random

DEBUG = False

def get_api_response():
    response = requests.get('http://trivia-api.thedundies.com/questions/')
    # TM doesn't send back a json object that's recognized as a dict by python.
    # It shows as a list 
    # Strip off the leading [ and trailing ] 
    # Now python sees this as a dict 
    # Proceed to get individual sections. 
    sanatized_response = response.text.lstrip("[").rstrip("]")
    
    json_data = json.loads(sanatized_response)
    return json_data

def print_debug_info(json_data):
    print (json_data["question_id"])
    # print the answers and correct value 
    print (json_data["answers"][0]["answer"], json_data["answers"][0]["correct"])
    print (json_data["answers"][1]["answer"], json_data["answers"][1]["correct"])
    print (json_data["answers"][2]["answer"], json_data["answers"][2]["correct"])
    print (json_data["answers"][3]["answer"], json_data["answers"][3]["correct"])
    print ("")
    print ("")

def shuffle_answers(json_data):
    question_list = []
    shuffled_list = []
    for i in (1,2,3,4):
        t = i - 1
        question_list.append([json_data["answers"][t]["answer"], json_data["answers"][t]["correct"]])

    random.shuffle(question_list)
   
    for i in (0,1,2,3):
        shuffled_list.append(question_list[i])

    return shuffled_list


if __name__ == "__main__":
    json_data = get_api_response()

    # print the question id
    if DEBUG == True:
        print_debug_info(json_data)

    shuffled_answers = shuffle_answers(json_data)
    
    # print the question 
    print (json_data["question"])

    for i in (0,1,2,3):
      uc = i + 1
      print(uc, shuffled_answers[i][0])
    
    while True:
        try:
            user_choice = int(input("Select an answer: ")) 
            break
        except ValueError:
            print("Please input integer only...")
            continue  

    


    ql = shuffled_answers



    if (user_choice == 1):
        if (ql[0][1] == True):
            print("Correct")
        else:
            print ("False")
    elif (user_choice == 2):
        if (ql[1][1] == True):
            print("Correct")
        else:
            print ("False")
    elif (user_choice == 3):
        if (ql[2][1] == True):
            print("Correct")
        else:
            print ("False")
    elif (user_choice == 4):
        if (ql[3][1] == True):
            print("Correct")
        else:
            print ("False")
    else:
        print ("outer false")

