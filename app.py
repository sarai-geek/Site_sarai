from flask import Flask
from admin_model import admin
from flask_sqlalchemy import SQLAlchemy
from config import Development
from flask_migrate import Migrate
import pymysql

app = Flask(__name__)
app.config.from_object(Development)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from admin_model import admin
from users_model import users

app.register_blueprint(admin)
app.register_blueprint(users)
