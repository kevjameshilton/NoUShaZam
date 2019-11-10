# Genre Picker
import json


class songPicker():

    def loadName(self, num, genre):
        song = json.load(open("../../music/" + genre + "/songsLib.json"))
        songName = song[str(num)]
        return songName

    def loadLyrics(self, num, genre):
        lyrics = json.load(open("../songs/", genre, "/lyricsLib.json"))
        songLyrics = lyrics[str(num)]
        return songLyrics

    def loadPath(self, num, genre):
        return '../songs/' + genre + '/' + loadLyrics(num, genre) + '.mp3'


class pick(Resource):
    parser = reqparse.ReqquestParser()
