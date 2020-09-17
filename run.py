# coding=utf-8
from flask import Flask, render_template
app = Flask(__name__)

# This is the function to open the list of happiness items
def get_hi(): #short for "get happiness items"
    hi_db = open("happiness_items.txt") #hi_db is short for "happiness items database"
    content = hi_db.read()
    hi_db.close()
    # put the values of content into an array. "hitems" is short for "happiness items"
    hitems = content.split("\n")
    return hitems

# choosing a happiness item randomly
import random
happiness_list = get_hi()
happiness_item = random.choice(happiness_list)
# print ("The randomly selected item from list is: ", happiness_item) 

@app.route("/")
def start():
    
    return render_template("start.html", title="Welcome to the Happiness Generator", 
                                            metadescription="This app lets you look for Happiness Items and add to the list yourself. This Happiness Item was randomly selected from a list. I hope it brings you joy.", 
                                            HAPPINESSITEM=happiness_item)

@app.route("/list")
def entire_list():
    hi_list = get_hi()
    """ # add additional HI to the list
    hi_to_add = flask.request.args.get("add")
    # hi_to_add must not be empty
    if hi_to_add != None:
        # add the text input to happiness_items.txt
        # open notes.txt and append another note
        textfile = open("happiness_items.txt", "a")
        # put the string from input field into the file, add a line break before
        textfile.write("\n"+ hi_to_add)
        textfile.close() """

    # The placeholder {{happiness}} in list.html is being replaced by the individual Happiness Items, all in a <p> tag with the class "box".
    return render_template("list.html", title="All Happiness Items, united", metadescription="This is the complete list of Happiness Items. You can add to the list or edit existing items. Enjoy!", happiness=hi_list)
                                                                    
                                                                   