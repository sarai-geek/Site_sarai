from flask import session
from . import admin


@admin.route('/')
def index():
    return "This page is for admin!"


@admin.route('/login')
def login():
    return '1'
