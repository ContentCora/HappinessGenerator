# coding=utf-8
from flask import Flask, render_template
app = Flask(__name__)

# Here comes the function to open the list of happiness items
def get_hi(): #short for "get happiness items"
    hi_db = open("happiness_items.txt") #hi_db is short for "happiness items database"
    content = hi_db.read()
    hi_db.close()
    # put the values of content into an array. "hitems" is short for "happiness items"
    hitems = content.split("\n")
    return hitems

@app.route("/")
def start():
    
    return render_template("start.html", title="Welcome to the Happiness Generator", 
                                            metadescription="This app lets you look for Happiness Items and add to the list yourself. This Happiness Item was randomly selected from a list. I hope it brings you joy.", 
                                            HAPPINESSITEM="Hello there!")

@app.route("/list")
def entire_list():
    hi_list = get_hi()
    hi_values = "" # hi_values = happiness item values
    for item in hi_list:
        #put each HI (hi_list) into one separate paragraph
        hi_values += item + "\n"
        hi_values += "<p>" + item + "</p>"
    print(hi_values)
    return render_template("list.html", title="All Happiness Items, united", metadescription="This is the complete list of Happiness Items. You can add to the list or edit existing items. Enjoy!")

    return hi_list.replace("$$happiness$$", hi_values)                                                                       