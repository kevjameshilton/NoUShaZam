# Game
from flask_restful import Resource, reqparse

import datetime
import traceback
from random import random
import math

from genre import songPicker

class GameCreator(Resource):
	parser = reqparse.RequestParser()

	def get(self, genre_name):
		data = GameCreator.parser.parse_args()

		try:
			_genre = pick()
			song_index = int(random() * 5) + 1
			song = songPicker.loadName(song_index, _genre)
			lyrics = songPicker.loadLyrics(song_index, _genre)
			song_mp3 = songPicker.loadPath(song_index, _genre)
			game_start = {"data": [song, lyrics, song_mp3]}
		except:
			return 'message: unable to load data', 500

		return game_start 



"""class Game(Resource):

	def get(self):
		try:
			#game = {"_id": ObjectId(id)}
			pass
		except:
			return {'message': 'game not found'}, 500
		return json_util._json_convert(game)

	def put(self, id):
		try:
			game = {"_id": ObjectId(id)}
		except:
			return {'message': 'Error looking up game'}



	def delete(self, id):
		pass"""




