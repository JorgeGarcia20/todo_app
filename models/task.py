from utils.db import db
from datetime import datetime

NOW = datetime.now()
# dt_str = now.strftime("%d/%m/%Y %H:%M:%S")


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.String(100))
    date = db.Column(db.DateTime)
    status = db.Column(db.Integer)

    def __init__(self, title, description, date=NOW, status=1):
        self.title = title
        self.description = description
        self.date = date
        self.status = status
