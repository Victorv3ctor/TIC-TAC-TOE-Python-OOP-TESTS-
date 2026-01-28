class Board:
    def __init__(self):
        self.game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def get_board_view(self):
        return (f"""\
{self.game_board[0]} | {self.game_board[1]} | {self.game_board[2]}
--+---+--
{self.game_board[3]} | {self.game_board[4]} | {self.game_board[5]}
--+---+--
{self.game_board[6]} | {self.game_board[7]} | {self.game_board[8]}""")

    def check_board(self):
        row = self.game_board[0:3:1]
        row1 = self.game_board[3:6:1]
        row2 = self.game_board[6:9:1]
        column = self.game_board[0:7:3]
        column1 = self.game_board[1:8:3]
        column2 = self.game_board[2:9:3]
        diagonal = self.game_board[0:9:4]
        diagonal1 = self.game_board[2:7:2]
        fields = [row, row1, row2, column, column1, column2, diagonal, diagonal1]
        for symbol in fields:
            if symbol[0] == symbol[1] == symbol[2] != ' ':
                return True
        return False

    def check_move(self,field):
        if (field > 0) and (field <= 9) and self.game_board[field-1] == ' ':
            return True
        return False

    def check_draw(self):
        if all(i != ' ' for i in self.game_board) and not self.check_board():
            return True
        return False