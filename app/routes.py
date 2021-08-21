from app import app
from flask import render_template, request, redirect, url_for, flash, jsonify
from os import getenv
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/signin')
def signin():
    return render_template("signin.html")