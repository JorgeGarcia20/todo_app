from flask import Flask
from routes.tasks import tasks
from flask_sqlalchemy import SQLAlchemy
from config import SECRET_KEY, DATABASE_CONNECTION_URI

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)

app.register_blueprint(tasks)
