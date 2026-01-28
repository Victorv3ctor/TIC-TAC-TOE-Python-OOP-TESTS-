from project.board import Board
from project.player import Player

class Menu:
    def __init__(self):
        self.board = Board()
        self.player = Player('x')
        self.player1 = Player('o')

    def take_turn(self,player):
        while True:
            print(f'\n{self.board.get_board_view()}')
            try:
                field = int(input(f'{player} turn: '))
                if self.board.check_move(field):
                    player.move(self.board.game_board, field)
                    break
                print('Invalid field, try again')
            except ValueError:
                print('Use digits to place symbol')

    def check_result(self):
        if self.board.check_draw():
            print(f'\nDRAW\n{self.board.get_board_view()}')
            return True
        if self.board.check_board():
            print(f'\nRESULT\n{self.board.get_board_view()}')
            return True
        return False

    def run(self):
        while True:
            self.take_turn(self.player)
            if self.check_result():
                break
            self.take_turn(self.player1)
            if self.check_result():
                break





















        #
        # while True:
        #     self.take_turn(self.player)
        #     if self.board.check_draw():
        #         print('Draw')
        #         break
        #     else:
        #         if self.board.check_board():
        #             print(f'\nResult \n{self.board.show_game_board()}')
        #             break
        #     self.take_turn(self.player1)
        #     if self.board.check_draw():
        #         print('Draw')
        #         break
        #     else:
        #         if self.board.check_board():
        #             print(f'\nResult \n{self.board.show_game_board()}')
        #             break