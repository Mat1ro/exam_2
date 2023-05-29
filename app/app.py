from flask import Flask

from flask_restx import Api
from config import Config
from app.setup_db import db
from app.views.note import note_ns
#test3

def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    db.init_app(app)
    register_extensions(app)
    return app


def register_extensions(app):
    api = Api(app)
    api.add_namespace(note_ns)


app = create_app(Config())

with app.app_context():
    db.create_all()

app.debug = True

if __name__ == '__main__':
    app.run()
