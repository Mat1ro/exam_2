from datetime import datetime

from marshmallow import Schema, fields

from app.setup_db import db


class Note(db.Model):
    __tablename__ = 'note'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, text):
        self.text = text


class NoteSchema(Schema):
    id = fields.Int()
    text = fields.Str()
    date_added = fields.DateTime()
