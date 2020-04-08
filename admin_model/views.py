from flask import session
from . import admin


@admin.route('/')
def index():
    return "This page is for admin!"


@admin.route('/login')
def login():
    session['name'] = 'ahmad'
    #session.clear()
    #print(session.get('name'))
    print(session)
    return '1'