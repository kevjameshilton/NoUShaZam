# Game
from flask_restful import Resource, reqparse

import datetime
import traceback
from random import random
import math
import traceback

from resources.genre import SongPicker

class GameCreator(Resource):

	def get(self, genre):
		try:
			song_index = int(random() * 5) + 1
			song = SongPicker.loadName(song_index, genre)
			lyrics = SongPicker.loadLyrics(song_index, genre)
			song_mp3 = SongPicker.loadPath(song_index, genre)
			game_start = {"data": [song, lyrics, song_mp3]}
		except:
			traceback.print_exc()
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




