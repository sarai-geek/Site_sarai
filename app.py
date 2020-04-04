from flask import Flask
from admin_model import admin

app = Flask(__name__)


@app.route('/')
def index():
    return "My Site-First Page"

app.register_blueprint(admin)

