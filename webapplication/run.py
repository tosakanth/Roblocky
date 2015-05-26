#!/usr/bin/python

#from app import app
from flask import Flask
from tkrobot import tkrobot

app=Flask(__name__)
app.register_blueprint(tkrobot)

app.debug=True
app.run(host='0.0.0.0',port=int(8080))
