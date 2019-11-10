from flask import Flask, jsonify
from flask_restful import Api
from flask_pymongo import PyMongo

from resources.genre import pick

app = Flask(__name__)
api = Api(app)

api.add_resource(pick, 'genres')
api.add_resource(startGame, '/game/<string:genre>')


if __name__ == '__main__':
    app.run(port=3000, debug=True)
