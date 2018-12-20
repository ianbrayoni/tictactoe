import random

X = "x"
O = "o"
EMPTY = " "
NUM_BOARD_POSITIONS = 9
WINNING_POSITIONS = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (1, 4, 7),
    (2, 5, 8),
    (3, 6, 9),
    (3, 5, 7),
    (1, 5, 9),
)


def create_board(str_board):
    """
    Convert string representation of the tictactoe board into a list
    List will have one extra item at the beginning so that board/grid
    positions can be referenced from 1 - refer to move_handler()

    >> create_board(" xxo  o x")
    [' ', ' ', 'x', 'x', 'o', ' ', ' ', 'o', ' ', 'x']

    :param str_board: str (string representation of the tictactoe board)
    :returns: list
    """
    board = [" "] + list(str_board)
    return board


def winning_move(board):
    """
    Check for possible winning moves

    :param board: list representation of the tictactoe game
    :returns: True or False
    """
    for row in WINNING_POSITIONS:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            return True

    return False


def move_handler(board):
    """
    Determine which move to make from list of available moves
    Uses the following stategy:
        1. If any corner slots are available, make a move into one of them
        2. If no corner slot is available but center is free, take center spot
        3. Move into an edge iff corners and center not available

    >> move_handler([' ', ' ', 'x', 'x', 'o', ' ', ' ', 'o', ' ', ' '])
    1

    :param board: list representaion of the tictactoe board
    :returns: int - the index to make a move to
    """
    if win(board):
        return win(board)
    elif block_x_win(board):
        return block_x_win(board)
    else:
        available_moves = [
            idx for idx, letter in enumerate(board) if letter == EMPTY and idx != 0
        ]

        # if board elements read from 0, this condition fails - if 0: False
        # yet 0 is a valid position in a 0-indexed list
        if play_corners(available_moves):
            return play_corners(available_moves)

        if play_center(available_moves):
            return play_center(available_moves)

        if play_edges(available_moves):
            return play_edges(available_moves)


def win(board):
    """
    Make a winning move for O if its obvious to do so

    :param board: list representaion of the tictactoe board
    :returns: int - the index to make a move to
    """
    return check_for_possible_win(board, O)


def block_x_win(board):
    """
    Block X's move if no winning move available for O

    :param board: list representaion of the tictactoe board
    :returns: int - the index to make a move to
    """
    return check_for_possible_win(board, X)


def check_for_possible_win(board, letter):
    """
    Given a letter, check whether it occurs one after the other e.g
    ['x', 'x', ' ']

    :param board: list representaion of the tictactoe board
    :param letter: str to check for
    :returns: int - the index to make a move to
    """
    for row in WINNING_POSITIONS:
        if letter == board[row[0]] == board[row[1]]:
            move = row[2]
            break
        elif letter == board[row[0]] == board[row[2]]:
            move = row[1]
            break
        elif letter == board[row[1]] == board[row[2]]:
            move = row[0]
            break

    return move


def play_corners(possible_moves):
    """
    Check if there is a possible move in list of corner indices [1, 3, 7, 9]
    If any corner slots are available, make a move into one of them

    >> play_corners([1, 4, 7, 8])
    1 (or 7)

    :param possible_moves: list - empty slots on the board
    :returns: int - randomly selected position to be occupied
    """
    corners = [1, 3, 7, 9]
    available_corners = []

    for idx in possible_moves:
        if idx in corners:
            available_corners.append(idx)

    if len(available_corners) > 0:
        return select_any(available_corners)


def play_edges(possible_moves):
    """
    Check if there is a possible move in list of edge indices [2, 4, 6, 8]
    If any edge slots are available, make a move into one of them

    >> play_edges([1, 2, 5])
    2

    :param possible_moves: list - empty slots on the board
    :returns: int - randomly selected position to be occupied
    """
    edges = [2, 4, 6, 8]
    available_edges = []

    for idx in possible_moves:
        if idx in edges:
            available_edges.append(idx)

    if len(available_edges) > 0:
        return select_any(available_edges)


def play_center(possible_moves):
    """
    Check if there is a possible move corresponding to center index - 4
    If center slot is available, make a move into it

    >> play_center([5, 8])
    5

    :param possible_moves: list - empty slots on the board
    :returns: int - center spot
    """
    if 5 in possible_moves:
        return 5


def select_any(lst):
    """
    Return random value from list

    >>select_any([1, 3, 5])
    1 (or 3 or 5)

    :param lst: list - available edges/corners
    :returns: int - where to move to
    """
    r = random.randrange(0, len(lst))
    return lst[r]


def play(board):
    """
    Given a move, update the board and return a string representation
    of the board

    >> play([' ', ' ', 'x', 'x', 'o', ' ', ' ', 'o', ' ', ' '])
    ' xxo  o  o'

    :param board: list representation of the tictactoe board
    :returns: str - string representation of the tictactoe board
    """
    pos = move_handler(board)

    if pos:
        board[pos] = O

    # return string of 9 elements, rem our array has 10 elements
    return "".join(board[1:])


def is_safe_to_play(str_board):
    """
    A couple of checks ascertaining whether its safe to play
    Checks are done against the string representation of the tictactoe board
        1. Expected characters are: ' ' or 'x' or 'o'
        2. String has to be of nine characters, no more no less
        3. If there's already a winner, no point to play
        4. Players take turns to play, one can only be one move ahead
        5. Board should not be full

    >> is_safe_to_play(" xxo  o x")
    True

    :param str_board: str - string representation of the tictactoe board
    :returns: Boolean - True if safe to play, otherwise False
    """
    if not set(str_board).issubset({X, O, EMPTY}):
        return False

    if len(str_board) != NUM_BOARD_POSITIONS:
        return False

    board = create_board(str_board)

    if winning_move(board):
        return False

    x_count = (board[1:]).count(X)
    o_count = (board[1:]).count(O)

    if (x_count - o_count > 1) or (o_count - x_count > 1):
        return False

    if (board[1:]).count(EMPTY) == 0:
        return False

    return True


def main():
    board_state = input("Enter the board state: ")

    if is_safe_to_play(board_state):
        board = create_board(board_state)
        return play(board)
    else:
        return "Invalid board state!"


if __name__ == "__main__":
    main()
