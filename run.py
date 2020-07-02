# coding=utf-8
from flask import Flask, render_template
app = Flask(__name__)

# Here comes the function to open the list of happiness items

@app.route("/")
def start():
    
    return render_template("start.html", title="Welcome to the Happiness Generator", 
                                            metadescription="This app lets you look for Happiness Items and add to the list yourself.")

@app.route("/random")
def random():
    
    return render_template("random.html", title="Your randomly selected Happiness Item", 
                                            metadescription="This Happiness Item was randomly selected from a list. I hope it brings you joy.")

@app.route("/list")
def entire_list():

    return render_template("list.html", title="All Happiness Items, united",
                                            metadescription="This is the complete list of Happiness Items. You can add to the list or edit existing items. Enjoy!")