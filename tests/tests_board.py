from project.board import Board
import pytest


@pytest.mark.parametrize('test_input, expected', [
    (2, True), (1, False), (10, False), (0, False), (-1, False)])
def test_check_move(test_input, expected):
    board = Board()
    board.game_board[0] = 'x'

    assert board.check_move(test_input) is expected


def test_check_board():
    board = Board()

    assert not board.check_board()


def test_check_board_symbol():
    board = Board()

    board.game_board[0] = 'x'
    board.game_board[1] = 'o'
    board.game_board[2] = 'x'

    assert not board.check_board()


def test_check_board_row():
    board = Board()

    board.game_board[0] = 'x'
    board.game_board[1] = 'x'
    board.game_board[2] = 'x'

    assert board.check_board()


def test_check_board_column():
    board = Board()

    board.game_board[1] = 'x'
    board.game_board[4] = 'x'
    board.game_board[7] = 'x'

    assert board.check_board()


def test_check_board_diagonal():
    board = Board()

    board.game_board[0] = 'x'
    board.game_board[4] = 'x'
    board.game_board[8] = 'x'

    assert board.check_board()


def test_check_board_diagonal1():
    board = Board()

    board.game_board[2] = 'x'
    board.game_board[4] = 'x'
    board.game_board[6] = 'x'

    assert board.check_board()


def test_check_draw_empty_board():
    board = Board()

    assert not board.check_draw()


def test_check_draw_full_board():
    board = Board()

    board.game_board[0] = 'x'
    board.game_board[1] = 'x'
    board.game_board[2] = 'o'
    board.game_board[3] = 'o'
    board.game_board[4] = 'o'
    board.game_board[5] = 'x'
    board.game_board[6] = 'x'
    board.game_board[7] = 'o'
    board.game_board[8] = 'x'

    assert not board.check_board()

    assert board.check_draw()


def test_check_no_draw_full_board():
    board = Board()

    board.game_board[0] = 'x'
    board.game_board[1] = 'x'
    board.game_board[2] = 'o'
    board.game_board[3] = 'o'
    board.game_board[4] = 'x'
    board.game_board[5] = 'o'
    board.game_board[6] = 'o'
    board.game_board[7] = 'x'
    board.game_board[8] = 'x'

    assert board.check_board() # Sprawdza czy plansza rzeczywisie zwroci wygrana (True)

    assert not board.check_draw() #Poprawne zlogszenie braku remisu






