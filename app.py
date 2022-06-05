from flask import Flask
from routes.tasks import tasks
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'j8hfk[*}dhfjsur'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:my_secret@localhost/task_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)

app.register_blueprint(tasks)
