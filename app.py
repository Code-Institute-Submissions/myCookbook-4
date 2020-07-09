import os
from flask import Flask, render_template, url_for, flash, redirect, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = "create_recipes"
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
SECRET_KEY = os.environ.get('SECRET_KEY')
mongo = PyMongo(app)

@app.route("/")
@app.route("/index")
def index():
    return render_template('pages/index.html', page_title="Home")


@app.route("/login")
def login():
    return render_template('pages/login.html', page_title="Login")


@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template('pages/register.html', page_title="Register")









if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True) 