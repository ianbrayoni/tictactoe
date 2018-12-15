import random


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
    board = [' '] + list(str_board)
    return board


def winning_move(board, letter):
    """
    All possible winning moves

    :param board: list representation of the tictactoe game
    :param letter: str
    :returns: True or False
    """
    return (
        (board[1] == letter and board[2] == letter and board[3] == letter)
        or (board[4] == letter and board[5] == letter and board[6] == letter)
        or (board[7] == letter and board[8] == letter and board[9] == letter)
        or (board[1] == letter and board[4] == letter and board[7] == letter)
        or (board[2] == letter and board[5] == letter and board[8] == letter)
        or (board[3] == letter and board[6] == letter and board[9] == letter)
        or (board[3] == letter and board[5] == letter and board[7] == letter)
        or (board[1] == letter and board[5] == letter and board[9] == letter)
    )


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
    available_moves = [
        idx for idx, letter in enumerate(board) if letter == " " and idx != 0
    ]

    # if board elements read from 0, this condition fails - if 0: False
    # yet 0 is a valid position in a 0-indexed list
    if play_corners(available_moves):
        return play_corners(available_moves)

    if play_center(available_moves):
        return play_center(available_moves)

    if play_edges(available_moves):
        return play_edges(available_moves)


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
        board[pos] = "o"

    # return string of 9 elements, rem our array has 10 elements
    return "".join(board[1:])


def is_safe_to_play(str_board):
    """
    A couple of checks ascertaining whether its safe to play
    Checks are done against the string representation of the tictactoe board
        1. String has to be of nine characters, no more no less
        2. Board should not be full
        3. Can only play if x's > o's
        4. Expected characters are: ' ' or 'x' or 'o'

    >> is_safe_to_play(" xxo  o x")
    True

    :param str_board: str - string representation of the tictactoe board
    :returns: Boolean - True if safe to play, otherwise False
    """
    if set(str_board) not in [{'x', 'o', ' '}, {' '}, {'x', 'o'}, {'x'}]:
        return False

    if len(str_board) != 9:
        return False

    board = create_board(str_board)

    if winning_move(board, "x") or winning_move(board, "o"):
        return False

    # board has extra element at beginning, check if board is full
    if (board[1:]).count(" ") == 0:
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
