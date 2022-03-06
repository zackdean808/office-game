#!/usr/bin/python

import requests
import json
import random

# oh look gtk stuff
import gi 
gi.require_version("Gtk","3.0")
from gi.repository import Gtk as gtk


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


def choice1_clicked(widget, ql):
    if (ql[0][1] == True):
        print("Correct")
    else:
        print ("False")

def choice2_clicked(widget, ql): 
    if (ql[1][1] == True):
        print("Correct")
    else:
        print ("False")
    return 2 

def choice3_clicked(widget, ql): 
    if (ql[2][1] == True):
        print("Correct")
    else:
        print ("False")
    return 3

def choice4_clicked(widget, ql): 
    if (ql[3][1] == True):
        print("Correct")
    else:
        print ("False")
    return 4


if __name__ == "__main__":

    json_data = get_api_response()

    if DEBUG == True:
        print_debug_info(json_data)
    
    shuffled_answers = shuffle_answers(json_data)

    gladeFile = "./gtk-files/office-game.glade"
    
    builder = gtk.Builder()
    builder.add_from_file(gladeFile)

    window = builder.get_object("mainWindow")
    window.show_all()
    window.connect("destroy", gtk.main_quit)

    question_label = builder.get_object("gtkQuestionLabel")
    question_label.set_text(str(json_data["question"]))

    choice1_button = builder.get_object("choice1")
    choice1_button.set_label(str(shuffled_answers[0][0]))
    choice1_button.connect("clicked", choice1_clicked, shuffled_answers)
   
    choice2_button = builder.get_object("choice2")
    choice2_button.set_label(str(shuffled_answers[1][0]))
    choice2_button.connect("clicked", choice2_clicked, shuffled_answers)
   
    choice3_button = builder.get_object("choice3")
    choice3_button.set_label(str(shuffled_answers[2][0]))
    choice3_button.connect("clicked", choice3_clicked, shuffled_answers)

    choice4_button = builder.get_object("choice4")
    choice4_button.set_label(str(shuffled_answers[3][0]))
    choice4_button.connect("clicked", choice4_clicked, shuffled_answers)
    
    gtk.main()