from flask import Blueprint

#this object to be imported in run.py
tkrobot = Blueprint('tkrobot', __name__,template_folder='templates')

from . import views
