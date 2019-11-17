class Board:

    def __init__(self):
        self.current_state = None
        self.children = None
        self.parent = None
        self.next_turn = None
        self.score = None
        self.is_game_finished = None

    def copy_board(self):
        copy_of_board = Board()
        copy_of_board.current_state = self.current_state.copy()
        copy_of_board.next_turn = self.next_turn
        return copy_of_board

    @staticmethod
    def get_initial_board():

        board = Board()

        board_state = [['', '', ''], ['', '', ''], ['', '', '']]
        board.current_state = board_state
        board.children = []
        board.parent = None
        board.next_turn = 'X'
        return board

    def is_game_tie(self):

        count = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] != '':
                    count += 1
        if self.is_game_finished is None and count == 9:
            self.is_game_finished = 0

    def is_full(self):
        for i in range(3):
            for j in range(3):
                if self.current_state[i][j] == '':
                    return False
        return True

    def alternate_turn(self):
        if self.next_turn == 'X':
            self.next_turn = 'O'
        else:
            self.next_turn = 'X'

    def make_move(self, row, col):
        if self.current_state[row][col] == '':
            self.current_state[row][col] = self.next_turn
            self.alternate_turn()
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
                self.is_game_finished = 1
            if o_count == 1:
                o_score += 1
            elif o_count == 2:
                o_score += 10
            if o_count == 3:
                # ??????
                o_score += 100
                self.is_game_finished = -1

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
                self.is_game_finished = 1
            if o_count == 1:
                o_score += 1
            elif o_count == 2:
                o_score += 10
            if o_count == 3:
                # ??????
                o_score += 100
                self.is_game_finished = -1

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
            self.is_game_finished = 1
        if o_count == 1:
            o_score += 1
        elif o_count == 2:
            o_score += 10
        if o_count == 3:
            # ??????
            self.is_game_finished = -1
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
            self.is_game_finished = 1
        if o_count == 1:
            o_score += 1
        elif o_count == 2:
            o_score += 10
        if o_count == 3:
            # ??????
            o_score += 100
            self.is_game_finished = -1
        total_score = x_score - o_score
        self.score = total_score
        return self.score


initial_board = Board.get_initial_board()
initial_board.make_move(2, 1)
initial_board.make_move(1, 1)
initial_board.make_move(2, 2)
initial_board.make_move(2, 0)
initial_board.make_move(0, 2)
initial_board.make_move(1, 2)
initial_board.make_move(1, 0)
initial_board.make_move(0, 1)
initial_board.make_move(0, 0)
initial_board.is_game_tie()
print(initial_board.calculate_current_state_score())
print(initial_board.is_game_finished)


class Tree:
    def __init__(self):
        self.root = Board.get_initial_board()

    def generate_full_tree(self):
        self.create_children(self.root)

    def create_children(self, board):

        if board.is_full() or board.is_game_over():
            return
        else:
            for i in range(3):
                for j in range(3):
                    if board.current_state[i][j] == '':
                        child = board.copy_board()
                        child.make_move(i, j)
                        board.children.append(child)
                        child.parent = board

                        self.create_children(child)
