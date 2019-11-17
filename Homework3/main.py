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
            print("Row:", row, ", Column: ", col, " is occupied.")

    def calculate_current_state_score(self):
        # e30 a biner yan yan gider
        x_score = 0
        o_score = 0

        for i in range(0, 3):
            x_count = 0
            o_count = 0
            for j in range(0, 3):
                if self.current_state[i][j] == 'X':
                    x_count += 1
                elif self.current_state[i][j] == 'O':
                    o_count += 1
                else:  # bos
                    pass
            if x_count == 1:
                x_score += 1
            elif x_count == 2:
                x_score += 10
            if x_count == 3:
                # ??????
                x_score += 100
            if o_count == 1:
                o_score += 1
            elif o_count == 2:
                o_score += 10
            if o_count == 3:
                # ??????
                o_score += 100

        ### dik dik gider
        for j in range(0, 3):
            x_count = 0
            o_count = 0
            for i in range(0, 3):
                if self.current_state[i][j] == 'X':
                    x_count += 1
                elif self.current_state[i][j] == 'O':
                    o_count += 1
                else:  # bos
                    pass
            if x_count == 1:
                x_score += 1
            elif x_count == 2:
                x_score += 10
            if x_count == 3:
                # ??????
                x_score += 100
            if o_count == 1:
                o_score += 1
            elif o_count == 2:
                o_score += 10
            if o_count == 3:
                # ??????
                o_score += 100

        ## saga dogru capraz gider
        x_count = 0
        o_count = 0
        for i in range(0, len(self.current_state)):
            if self.current_state[i][i] == 'X':
                x_count += 1
            elif self.current_state[i][i] == 'O':
                o_count += 1
            else:  # bos
                pass
        if x_count == 1:
            x_score += 1
        elif x_count == 2:
            x_score += 10
        if x_count == 3:
            # ??????
            x_score += 100
        if o_count == 1:
            o_score += 1
        elif o_count == 2:
            o_score += 10
        if o_count == 3:
            # ??????
            o_score += 100

        x_count = 0
        o_count = 0
        left_diagonal_indices = ['0x2', '1x1', '2x0']
        for index in left_diagonal_indices:
            i, j = index.split('x')
            i = int(i)
            j = int(j)
            if self.current_state[i][j] == 'X':
                x_count += 1
            elif self.current_state[i][j] == 'O':
                o_count += 1
            else:  # bos
                pass
        if x_count == 1:
            x_score += 1
        elif x_count == 2:
            x_score += 10
        if x_count == 3:
            # ??????
            x_score += 100
        if o_count == 1:
            o_score += 1
        elif o_count == 2:
            o_score += 10
        if o_count == 3:
            # ??????
            o_score += 100
        total_score = x_score - o_score
        return total_score

initial_board = Board.get_initial_board()
initial_board.put_x(1, 2)
initial_board.put_o(2, 2)
initial_board.put_o(1,1)
initial_board.put_x(1,1)
print(initial_board.calculate_current_state_score())
print()


class Tree:

    def __init__(self):
        self.root = Board()






