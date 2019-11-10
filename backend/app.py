from flask import Flask, jsonify
from flask_restful import Api
from flask_pymongo import PyMongo

app = flask(__name__)
api = Api(app)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
