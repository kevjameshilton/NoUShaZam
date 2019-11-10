# Game
from flask_restful import Resource, reqparse
from bson import json_util
from bson.objectid import ObjectId
#from db import mongo

import traceback
from random import random
import math

from resources.genre import pop

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
			song = pop.loadName(song_index)
			lyrics = pop.loadLyrics(song_index)
			#song_time needs to be implemented in genre
		except:
			return 'message: genre not found'

		

		return json_util._json_convert(game_created), 201 



"""class Game(Resource):

	def get(self, id):
		pass"""




