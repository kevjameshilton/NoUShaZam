from flask import Flask, jsonify
from flask_restful import Api

# from resources.genre import pick

app = Flask(__name__)
api = Api(app)

api.add_resource(pick, 'genres')
api.add_resource(sendSong, '/song/<string:genre>')

if __name__ == '__main__':
    app.run(port=3000, debug=True)
