from project.player import Player
from project.board import Board


def test_player_symbol():
    player = Player('x')

    assert player.symbol == 'x'


def test_player_move():
    player = Player('X')

    board = Board()

    player.move(board.game_board, 2)

    assert board.game_board[1] == 'X'










