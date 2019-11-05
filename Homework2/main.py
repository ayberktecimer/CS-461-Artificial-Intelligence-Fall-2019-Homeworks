"""
CS461 Homework2
Fall 2019

Adahan Yalçınkaya 21502369
Bengi Dönmez 21602237
Emre Sülün 21502214
Eray Şahin 21502758
Kazım Ayberk Tecimer 21502531
"""


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def f_n_value(self, path):
        return path.calculateF_n()

    def print_queue(self):
        print("Items in the queue:\nHead of the queue:")
        for path in self.items:
            path.print_path()
        print("Tail of the queue")

    def sort(self):
        self.items.sort(key=self.f_n_value)


class State:
    """
    This class represents the node in the graph. Each node corresponds to the state of the west coast.
    """
    total_missionaries = 6
    total_cannibals = 6
    boat_size = 5

    def __init__(self, m, c, b):
        """
        Constructor
        :param m: Number of missionaries on the west coast
        :param c: Number of cannibal on the west coast
        :param b: Boats position( 1 if its on the west, 0 if its on the east)
        """
        self.m = m
        self.c = c
        self.b = b
        self.value = str(self.m) + "M " + str(self.c) + "C " + str(self.b) + "B"

    def create_possible_children(self):
        """
        This function creates all possible children for current node. In other words, it generates ALL possible states
        that can follow the current state.
        :return: list of states
        """
        possible_children = []

        # To generate children states, we should send missionaries/cannibals in different configurations
        # For that, i and j represent all crossing configurations
        # For instance i: 2, j: 1 means 2 missionaries and 1 cannibal will cross

        for i in range(0, State.boat_size + 1):
            for j in range(0, State.boat_size + 1):

                # While creating possible children, make sure that
                # - the capacity of the boat is not exceeded,
                # - and missionaries are not outnumbered by cannibals

                if (State.boat_size >= i + j >= 1 and i >= j) or (i == 0 and j != 0):
                    if self.b == 1:
                        possible_children.append(State(self.m - i, self.c - j, 0))
                    elif self.b == 0:
                        possible_children.append(State(self.m + i, self.c + j, 1))

        return possible_children

    def create_possible_edges(self):
        """
        This function calls "create_possible_children", and eliminates the unsafe states. At the end, it returns a list
        of "children" states that are safe.
        :return: list of states
        """
        possible_children = self.create_possible_children()
        valid_states = []

        for child in possible_children:
            if child.isStateValid():  # isStateValid checks whether the "child" state is valid and safe
                valid_states.append(child)

        return valid_states

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

    @staticmethod
    def getGoalState():
        """
        Definition of the GOAL STATE
        """
        return State(0, 0, 0)

    def isGoalState(self):
        """
        Checks if the current state is the goal state.
        :return: True if it is the goal state, False otherwise
        """
        return self == State.getGoalState()

    def calculateHeuristic(self):
        """
        Our heuristic function is h = (number of people on the initial bank) divided by (the size of the boat)
        TODO: explain why this is admissible
        """
        return (self.c + self.m) / State.boat_size


class Path:
    """
    Represents a possible path as a list of states
    """
    def __init__(self):
        """
        Constructor
        """
        self.stateList = []  # sequence of states that form the path

    def appendState(self, state):
        self.stateList.append(state)

    def copyStateList(self):
        """
        Copy constructor
        """
        return self.stateList.copy()

    def extend_path(self):
        terminatingNode = self.get_terminating_node()
        childrenList = terminatingNode.create_possible_edges()

        pathList = []
        for child in childrenList:
            p = Path()
            p.stateList = self.copyStateList()
            p.stateList.append(child)
            pathList.append(p)

        return pathList

    def calculateCost(self):
        return len(self.stateList) - 1

    def calculateF_n(self):
        """
        F_n is the sum of cost and heuristic value
        """
        cost = self.calculateCost()
        terminatingNode = self.stateList[len(self.stateList) - 1]
        heuristic_value = terminatingNode.calculateHeuristic()
        return cost + heuristic_value

    def get_terminating_node(self):
        """
        :return: The last node in the path
        """
        return self.stateList[len(self.stateList) - 1]

    def print_path(self):
        """
        Prints the path in an appealing format
        """
        length = len(self.stateList)
        for i in range(length):
            if i == length - 1:
                print(self.stateList[i])
            else:
                print(self.stateList[i], end='')
                print(" -> ", end='')

    def is_loop_free(self):
        """
        Checks if the path has loop or not
        """
        seen_states = set()
        for state in self.stateList:
            state_id = str(state)
            if state_id in seen_states:
                return False
            seen_states.add(state_id)
        return True

    def is_goal_found(self):
        """
        Checks if the path has reached to goal state or not
        """
        return self.get_terminating_node().isGoalState()


def a_star(root):
    """
    Performs A* search algorithm
    """
    a_star_queue = Queue()  # Constructs an empty queue

    # Adds the root to the queue (as a "zero-length path")
    initial_path = Path()
    initial_path.appendState(root)
    a_star_queue.enqueue(initial_path)

    while a_star_queue.isEmpty() is False:
        path_in_front = a_star_queue.dequeue()

        if path_in_front.is_goal_found():
            print("Success, found a path!")
            path_in_front.print_path()
            return
        else:
            extended_paths = path_in_front.extend_path()

            for path in extended_paths:
                if path.is_loop_free():
                    a_star_queue.enqueue(path)

        a_star_queue.sort()

    print("No path found.")


# Code starts from here
initial_state = State(State.total_missionaries, State.total_cannibals, 1)  # Root of the tree
a_star(initial_state)
