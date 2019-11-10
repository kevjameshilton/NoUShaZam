# Genre Picker
import ast


class genrePicker():
    parser = reqparse.RequestParser()
    parser.add_argument('genre', type=str,
                        required=True,
                        help='Please pick a genre!'
                        )

    def pick():


class pop():
    d = json.load(open("popLib.json"))

    def loadName(self, num):
        song = d[num]

    def loadLyrics(self, num):
        lyrics = d[num]
