from flask import render_template,request,send_from_directory,redirect
import os
from . import tkrobot

#same object defined in __init__.py
@tkrobot.route('/')
def show_intro():
	return render_template('index.html');
	
@tkrobot.route('/js/<path:filename>')
def send_script(filename):
   return send_from_directory(os.getcwd()+'/tkrobot/static/js',filename)	

@tkrobot.route('/images/<path:filename>')
def send_images(filename):
   return send_from_directory(os.getcwd()+'/tkrobot/static/images',filename)	

@tkrobot.route('/media/<path:filename>')
def send_media(filename):
   return send_from_directory(os.getcwd()+'/tkrobot/static/media',filename)	

@tkrobot.route('/css/<path:filename>')
def send_css(filename):
   return send_from_directory(os.getcwd()+'/tkrobot/static/css',filename)	
   
@tkrobot.route('/img/<path:filename>')
def send_img(filename):
   return send_from_directory(os.getcwd()+'/tkrobot/static/img',filename)	
