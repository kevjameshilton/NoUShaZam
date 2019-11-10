from flask import Flask, jsonify
from flask_restful import Api

from resources.game import GameCreator

app = Flask(__name__)
api = Api(app)

api.add_resource(GameCreator, '<string:genre>')


if __name__ == '__main__':
    app.run(port=3000, debug=True)
