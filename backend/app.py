from flask import Flask, jsonify
from flask_restful import Api

from resources.game import GameCreator

app = Flask(__name__)
api = Api(app)

api.add_resource(GameCreator, '/song/<string:genre>')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
