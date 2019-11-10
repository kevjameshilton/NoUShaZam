# Game
from flask_restful import Resource, reqparse
from bson import json_util
from bson.objectid import ObjectId
#from db import mongo

import datetime
import traceback
from random import random
import math

from resources.genre import songPicker, pick

class GameCreator(Resource):
	parser = reqparse.RequestParser()
	"""parser.add_argument('song_time',
						type = int,
						required=True,
						)
	"""

	def post(self, id, pick):
		data = GameCreator.parser.parse_args()

		try:
			genre = pick()
			song_index = int(random() * 5) + 1
			song = songPicker.loadName(song_index, genre)
			lyrics = songPicker.loadLyrics(song_index, genre)
			song_mp3 = songPicker.loadPath(song_index, genre)
			game_start = {"data": [song, lyrics, song_mp3]}
		except:
			return 'message: unable to load data', 500

		return json_util._json_convert(game_start), 201 



class Game(Resource):

	def get(self, id):
		try:
			game = {"_id": ObjectId(id)}
		except:
			return {'message': 'game not found'}, 500
		return json_util._json_convert(game)

	def put(self, id):
		try:
			game = {"_id": ObjectId(id)}
		except:
			return {'message': 'Error looking up game'}




	def delete(self, id):
		pass




