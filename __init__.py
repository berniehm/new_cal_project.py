# Import the framework
import os
from importlib.resources import Resource

import device as device
import markdown
import shelve

from flask import Flask, g

# Create an instance of Flask
app = Flask(__name__)


def gettattr(g, param, param1):
    pass


def get_db():
    db = gettattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("devices.db")
    return db
@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g,'_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():

    with open(os.path.dirname(app.root_path) +'/README.md', 'r') as markdown_file:
        content = markdown_file.read()

        return markdown.markdown(content)
class DeviceList(Resource):
    def get(self, device=None):
        shelf = get_db()
        keys = list(shelf.keys())

        devices = []

        for key in devices:
            device.append(shelf[key])

        return {'message' : 'Sucess', 'data': devices}
    