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
        #       For instance i: 2, j: 1 means 2 missionaries and 1 cannibal will cross

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

    def isStateGoal(self):
        """
        Checks if the current state is the goal state.
        :return: True if it is the goal state, False otherwise
        """
        if self.m == 0 and self.c == 0 and self.b == 0:
            return True
        else:
            return False


class Path:

    def __init__(self):
        self.stateList = []  # sequence of states that form the path

    def path_from_root(self, state):
        self.stateList.append(state)

    def copyStateList(self):
        return self.stateList.copy()  # returns a copy of the state list

    def compare(self, other):
        return self.calculateF_n() - other.calculateF_n()

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

    def calculateHeuristic(self):

        # Our heuristic function is h = (number of people on the initial bank) divided by (the size of the boat)
        # TODO: explain why this is admissible
        # TODO: move to node class
        terminatingNode = self.stateList[len(self.stateList) - 1]
        return (terminatingNode.c + terminatingNode.m) / State.boat_size

    def calculateF_n(self):
        cost = self.calculateCost()
        heuristic_value = self.calculateHeuristic()
        return cost + heuristic_value

    def get_terminating_node(self):
        return self.stateList[len(self.stateList) - 1]

    def print_path(self):

        length = len(self.stateList)
        for i in range(length):
            if i == length - 1:
                print(self.stateList[i])
            else:
                print(self.stateList[i], end='')
                print(" -> ", end='')

    def is_loop_free(self):
        seen_states = set()
        for state in self.stateList:
            state_id = str(state)
            if state_id in seen_states:
                return False
            seen_states.add(state_id)
        return True


def is_goal_found(path):
    # Get the terminating node of the path
    terminating_node = path.get_terminating_node()
    if terminating_node.isStateGoal():
        return True
    else:
        return False


def a_star(root):
    """
    Performs A* search algorithm
    """

    a_star_queue = Queue()  # Constructs an empty queue

    # Adds the root to the queue (as a "zero-length path")
    initial_path = Path()
    initial_path.path_from_root(root)
    a_star_queue.enqueue(initial_path)

    while a_star_queue.isEmpty() is False:
        path_in_front = a_star_queue.dequeue()

        if is_goal_found(path_in_front):
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
