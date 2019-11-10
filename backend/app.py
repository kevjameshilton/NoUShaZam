from flask import Flask, jsonify
from flask_restful import Api

<<<<<<< HEAD
from resources.game import GameCreator
=======
# from resources.genre import pick
>>>>>>> 0e6d35300410b9651cedc499d97683c0779f43b2

app = Flask(__name__)
api = Api(app)

api.add_resource(GameCreator, '<string:genre>')


if __name__ == '__main__':
    app.run(port=3000, debug=True)
