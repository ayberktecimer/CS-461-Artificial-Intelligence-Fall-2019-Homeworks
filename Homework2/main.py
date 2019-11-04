"""
CS461 Homework2
Fall 2019

Adahan Yalçınkaya 21502369
Bengi Dönmez 21602237
Emre Sülün 21502214
Eray Şahin 21502758
Kazım Ayberk Tecimer 21502531
"""
import queue
class State:
    """
    This class represents the node in the graph. Each node corresponds to the state of the west coast.
    """
    total_missionaries = 4
    total_cannibals = 4
    boat_size = 2
    def __init__(self, m, c, b, parent, children):
        """
        Constructor
        :param m: Number of missionaries on the west coast
        :param c: Number of cannibal on the west coast
        :param b: Boats position( 1 if its on the west, 0 if its on the east)
        :param parent: Previous state
        :param children: List of next states
        """
        self.m = m
        self.c = c
        self.b = b
        self.parent = parent
        self.children = children
        self.value = str(self.m) + "M " + str(self.c) + "C " + str(self.b) + "B"

    # i misyoner, j cannibal
    def possible_children_depending_bot_size(self,size):
        possibleChildren = []
        for i in range(0, size + 1):
            for j in range(0, size + 1):
                if (size >= i + j >= 1 and i >= j) or (i == 0 and j != 0):
                    if self.b == 1:
                        possibleChildren.append(State(self.m - i, self.c - j, 0, self, []))
                    elif self.b==0:
                        possibleChildren.append(State(self.m + i, self.c + j, 1, self, []))
        return possibleChildren

    def create_possible_edges(self):
        """
        This function creates possible children for current node.
        :return:
        """
        possibleChildren = self.possible_children_depending_bot_size(State.boat_size)
        '''
        if self.b == 1:  # if boat is on the west side, possible children are given below
            possibleChildren.append(State(self.m - 2, self.c, 0, self, []))
            possibleChildren.append(State(self.m, self.c - 2, 0, self, []))
            possibleChildren.append(State(self.m - 1, self.c - 1, 0, self, []))
            possibleChildren.append(State(self.m - 1, self.c, 0, self, []))
            possibleChildren.append(State(self.m, self.c - 1, 0, self, []))
        else:  # if boat is on the east side, possible children are given below
            possibleChildren.append(State(self.m + 2, self.c, 1, self, []))
            possibleChildren.append(State(self.m, self.c + 2, 1, self, []))
            possibleChildren.append(State(self.m + 1, self.c + 1, 1, self, []))
            possibleChildren.append(State(self.m + 1, self.c, 1, self, []))
            possibleChildren.append(State(self.m, self.c + 1, 1, self, []))
        '''

        for child in possibleChildren:
            if child.isStateValid() and child.isLoopFree(self.parent):
                """
                isStateValid checks whether the next state is safe and isLoopfree 
                checks the state occurs first time in the current path. If they're both 
                true it appends to the children list of the state 
                """
                self.children.append(child)

    def isStateValid(self):
        """
        It checks whether the state is safe (The number missionaries
        are greater or equal to number of cannibals in one side).
        :return: true if state is safe
        """
        c = self.c
        m = self.m
        b = self.b
        if c < 0 or c > State.total_cannibals or m < 0 or m > State.total_missionaries:  # Check total count
            return False
        if c > m > 0:  # Check the safety of west coast
            return False
        if State.total_cannibals - c > State.total_missionaries - m > 0:  # Check the safety of east coast
            return False
        if b == 1 and m == 0 and c == 0:  # Check the location of boat
            return False
        if b == 0 and m == State.total_missionaries and c == State.total_cannibals:  # Check the location of boat
            return False
        return True

    def isLoopFree(self, parent):
        """
        Checks whether possible children cause a loop. If there is a loop, it does not add possible child as child
        :param parent:
        :return: True if the path is loop free, False if path consists loops
        """
        if parent is None:
            return True
        return not (self == parent) and self.isLoopFree(parent.parent)

    def __eq__(self, other):
        """
        :param other: other state
        :return: True if states are equal
        """
        return self.m == other.m and self.c == other.c and self.b == other.b

    def __str__(self):
        """
        :return: String representation of the state
        """
        return str(self.m) + "M" + str(self.c) + 'C' + str(self.b)

    def isStateGoal(self):
        """
        Checks if the current state is the goal state.
        :return: True if it is the goal state, False otherwise
        """
        if self.m == 0 and self.c == 0 and self.b == 0:
            return True
        else:
            return False


initial_state = State(State.total_missionaries, State.total_cannibals, 1, None, [])  # Root of the tree

initial_state.create_possible_edges()




#possible_bot_size(2)