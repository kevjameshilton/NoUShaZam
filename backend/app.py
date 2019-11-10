from flask import Flask, jsonify
from flask_restful import Api
from flask_pymongo import PyMongo

from resource.

app = Flask(__name__)
api = Api(app)

api.add_resource(pickGenre, 'genres')


if __name__ == '__main__':
    app.run(port=3000, debug=True)
