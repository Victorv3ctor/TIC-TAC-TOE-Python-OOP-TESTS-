class Player:
    def __init__(self,symbol: str):
        self.symbol = symbol

    def move(self,game_board,field):
        game_board[field-1] = self.symbol

    def __str__(self):
        return f'{self.symbol} player'

