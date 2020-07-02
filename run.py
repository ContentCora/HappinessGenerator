# coding=utf-8
from flask import Flask, render_template
app = Flask(__name__)

# Here comes the function to open the list of happiness items

@app.route("/")
def start():
    
    return render_template("start.html")

@app.route("/random")
def random():
    
    return render_template("random.html")

@app.route("/list")
def entire_list():

    return render_template("list.html")