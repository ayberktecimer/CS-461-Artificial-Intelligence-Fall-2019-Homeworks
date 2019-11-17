import math
"""
CS461 Homework3
Fall 2019

Adahan Yalçınkaya 21502369
Bengi Dönmez 21602237
Emre Sülün 21502214
Eray Şahin 21502758
Kazım Ayberk Tecimer 21502531
"""
import copy


class Board:

    def __init__(self):
        self.current_state = None
        self.children = []
        self.parent = []
        self.next_turn = None
        self.score = None
        self.depth = 0

    @staticmethod
    def get_initial_board():

        board = Board()

        board_state = [['', '', ''], ['', '', ''], ['', '', '']]
        board.current_state = board_state
        board.children = []
        board.parent = None
        board.next_turn = 'X'
        return board

    def copy_board(self):

        copied_board = Board()
        copied_board.current_state = copy.deepcopy(self.current_state)
        copied_board.next_turn = copy.deepcopy(self.next_turn)
        copied_board.depth = copy.deepcopy(self.depth)
        return copied_board

    def is_game_tie(self):

        count = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] != '':
                    count += 1
        if count == 9:
            return True
        return False

    def is_there_a_winner(self):
        """
        Checks whether there is a winner in the current board situation. Returns true if there is a winner.

        It checks all 8 possible lines (horizontal, vertical and diagonal ones).
        :return:
        """

        # Check the horizontal lines (3 lines)
        for i in range(3):
            s = set()
            for j in range(3):
                s.add(self.current_state[i][j])
            if len(s) == 1:
                if '' not in s:
                    return True

        # Check the vertical lines (3 lines)
        for j in range(3):
            s = set()
            for i in range(3):
                s.add(self.current_state[i][j])
            if len(s) == 1:
                if '' not in s:
                    return True

        # Check the diagonal (the one from top-left to bottom-right)
        s = set()
        for i in range(3):
            s.add(self.current_state[i][i])
        if len(s) == 1:
            if '' not in s:
                return True

        # Check the other diagonal (the one from top-right to bottom-left)
        s = set()
        for i in range(3):
            s.add(self.current_state[i][2 - i])
        if len(s) == 1:
            if '' not in s:
                return True

        return False

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
        self.score = total_score
        return self.score


'''
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
'''


class Tree:

    def __init__(self):
        self.root = Board.get_initial_board()
        self.depth = 0

    def generate_full_tree(self):
        self.create_children(self.root)

    def create_children(self, board):

        if board.is_game_tie() or board.is_there_a_winner():
            return
        else:
            for i in range(3):
                for j in range(3):
                    if board.current_state[i][j] == '':

                        child = board.copy_board()
                        child.make_move(i, j)
                        child.parent = board
                        child.depth = child.parent.depth + 1
                        board.children.append(child)
                        self.create_children(child)
'''
CODE IS ADAPTED FROM http://web.mit.edu/dxh/www/adverse/index.html
Alpha-Beta-search(node, maximizing?, α, β, α-node, β-node)
    If α and β are undefined:
        Set α = −∞ and β = +∞.
    If node has children:
        For each child child of node:
            Set ⟨result_value, result_node⟩ = Alpha-Beta-search(child, not maximizing?, α, β, α-node, β-node)
            If maximizing?:
                If result_value > α:
                    Set ⟨α, α-node⟩ = ⟨result_value, result_node⟩.
            Else:
                If result_value < β:
                    Set ⟨β, β-node⟩ = ⟨result_value, result_node⟩.
            If α ≥ β: // if node can be pruned
                Exit the for loop early.
        End For.
        If maximizing?:
            Return ⟨α, α-node⟩.
        Else:
            Return ⟨β, β-node⟩.
    Else:
        Return node and the static value of node.
'''


def alpha_beta(Board, alpha, beta, alpha_node, beta_node):
    depth = Board.depth
    is_max_level = True if depth%2 == 0 else False
    if alpha is None and beta is None:
        alpha =  - math.inf
        beta = math.inf
    children = Board.children
    if len(children) > 0 :
        for child in children:
            result_value, result_node = alpha_beta(child, alpha, beta, alpha_node, beta_node)
            if is_max_level:
                if result_value > alpha:
                    alpha = result_value
                    alpha_node = result_node
            else:
                if result_value < beta:
                    beta = result_value
                    beta_node = result_node
            if alpha >= beta:
                break
        if is_max_level:
            return alpha,alpha_node
        else:
            return beta,beta_node
    else:
        return Board.calculate_current_state_score(), Board



t = Tree()
t.generate_full_tree()
result = alpha_beta(t.root, None, None, None, None)
print()
