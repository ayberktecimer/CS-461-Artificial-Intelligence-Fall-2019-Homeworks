class Board:

    def __init__(self):
        self.current_state = None
        self.children = None

    @staticmethod
    def get_initial_board():

        board = Board()
        board_state = [['', '', ''], ['', '', ''], ['', '', '']]
        board.current_state = board_state
        board.children = []
        return board

    def put_x(self, row, col):
        self.put_char(row, col, 'X')

    def put_o(self, row, col):
        self.put_char(row, col, 'O')

    def put_char(self, row, col, char):
        if self.current_state[row][col] == '':
            self.current_state[row][col] = char
        else:
            print("Row:", row, ", column: ", col, " is occupied.")


initial_board = Board.get_initial_board()
initial_board.put_x(1, 2)
print()


class Tree:

    def __init__(self):
        self.root = Board()
