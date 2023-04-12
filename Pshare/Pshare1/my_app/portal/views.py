#!/usr/bin/env python

from flask import Flask, render_template, session, redirect, url_for, flash, request, g
from my_app import app  #These are defined in __init__.py in the source directory of MyProject/my_app
from my_app.portal.models import MySQLDatabase
from my_app.portal.Table_Classes import User, Friend, UserFriend, ALbum, Like, Photo, Comment, Tag, PhotoTag

db = MySQLDatabase()
#Routes for main web application
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def process_login():
    email = request.form['username']
    password = request.form['password']

    # Replace this with your own authentication logic
    empw = db.select_user_by_email(email)
    em = empw[0]
    pw = empw[1]
    if em == email and pw == password:
        return 'Login successful!'
    else:
        return 'Invalid username or password'

@app.route('/create_account', methods=['POST'])
def create_account():
    email = request.form['email']
    password = request.form['password']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    dob = request.form['dob']
    hometown = request.form['hometown']
    gender = request.form['gender']

    # Add your logic here to store the user information in your database
    if db.check_if_email_in_users(email):
        return 'Error, user already exists'
    else:
        userID = db.select_max_userID() + 1
        db.insert_user(userID, first_name, last_name, email, dob, gender, hometown, password)
        return f"Account created for {first_name} {last_name}"


