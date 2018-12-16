from flask import Flask
from flask_restplus import Resource, Api, reqparse
from werkzeug.exceptions import BadRequest

from tic_tac_toe import is_safe_to_play, create_board, play

app = Flask(__name__)
api = Api(app)


class TicTacToe(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("board", type=str, required=True, location="args")
        args = parser.parse_args()
        board_state = args["board"]

        if is_safe_to_play(board_state):
            board = create_board(board_state)
            return play(board)
        else:
            raise BadRequest()


api.add_resource(TicTacToe, "/tictactoe")

if __name__ == "__main__":
    app.run(debug=False)
