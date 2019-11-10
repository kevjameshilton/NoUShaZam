# Genre Picker
import json


class SongPicker:
    @classmethod
    def loadName(cls, num, genre):
        song = json.load(open("../../music/" + genre + "/songsLib.json"))
        songName = song[str(num)]
        return songName
    @classmethod
    def loadLyrics(cls, num, genre):
        lyrics = json.load(open("../songs/", genre, "/lyricsLib.json"))
        songLyrics = lyrics[str(num)]
        return songLyrics
    @classmethod
    def loadPath(cls, num, genre):
        return '../songs/' + genre + '/' + cls.loadName(num, genre) + '.mp3'


'''class picker():
    parser = reqparse.ReqquestParser()'''
