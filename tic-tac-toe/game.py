class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]    # we will use a single list to rep. the 3x3 board
        self.current_winner = None              # keep track of the winner

    def print_board(self):
        # this is just getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
       pass 