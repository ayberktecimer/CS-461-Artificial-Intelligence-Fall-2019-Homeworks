"""
CS461 Homework1
Fall 2019

Adahan Yalçınkaya
Bengi Dönmez
Emre Sülün
Eray Şahin
Kazım Ayberk Tecimer
"""
import queue

tree = ""
class State:
    total_missionaries = 4
    total_cannibals = 4

    """
    This class represents the node in the graph. Each node corresponds to the state of the west coast.
    """

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

    def create_possible_edges(self):
        """
        This function creates possible children for current node.
        :return:
        """
        possibleChildren = []
        if self.b == 1:
            possibleChildren.append(State(self.m - 2, self.c, 0, self, []))
            possibleChildren.append(State(self.m, self.c - 2, 0, self, []))
            possibleChildren.append(State(self.m - 1, self.c - 1, 0, self, []))
            possibleChildren.append(State(self.m - 1, self.c, 0, self, []))
            possibleChildren.append(State(self.m, self.c - 1, 0, self, []))
        else:
            possibleChildren.append(State(self.m + 2, self.c, 1, self, []))
            possibleChildren.append(State(self.m, self.c + 2, 1, self, []))
            possibleChildren.append(State(self.m + 1, self.c + 1, 1, self, []))
            possibleChildren.append(State(self.m + 1, self.c, 1, self, []))
            possibleChildren.append(State(self.m, self.c + 1, 1, self, []))

        for child in possibleChildren:
            if child.isStateValid() and child.isLoopFree(self.parent):
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
        if c < 0 or c > State.total_cannibals or m < 0 or m > State.total_missionaries:
            return False
        if c > m > 0:
            return False
        if State.total_cannibals - c > State.total_missionaries - m > 0:
            return False
        if b == 1 and m == 0 and c == 0:
            return False
        if b == 0 and m == State.total_missionaries and c == State.total_cannibals:
            return False
        return True

    def isLoopFree(self, parent):
        """
        It does the loop checking
        :param parent:
        :return:
        """
        if parent is None:
            return True
        return not (self == parent) and self.isLoopFree(parent.parent)

    def __eq__(self, other):
        return self.m == other.m and self.c == other.c and self.b == other.b

    def __str__(self):
        return str(self.m) + "M" + str(self.c) + 'C' + str(self.b)

    def isStateGoal(self):
        """
        Checks if the current state is the goal state.
        :return:
        """
        if self.m == 0 and self.c == 0 and self.b == 0:
            return True
        else:
            return False


def get_solution_path(goal_state):
    """
    This function prints the solution path if it exists.
    :param goal_state:
    :return:
    """
    path = []
    current_state = goal_state
    while current_state is not None:
        path.append(current_state)
        current_state = current_state.parent
    path = path[::-1]
    for i in range(0, len(path)):
        if i == len(path) - 1:
            print(path[i])
        else:
            print(path[i], end=' -> ')


def bfs_tree_search(root):
    """
    This function applies BFS to the states by forming one element queue consisting only root node
    Until first state in the queue is the goal state or the queue becomes empty, it removes the
    first state in the queue and adds the children of the removed state on the rear of the queue.
    If the goal state is found it announces success otherwise it announce failure.
    :param root: starting node of the bfs
    :return:
    """
    bfs_queue = queue.Queue()
    bfs_queue.put(root)
    #vısualızatıon
    #v = Visualization()

    isSolutionFound = False
    while not bfs_queue.empty():
        current_state = bfs_queue.get()
        #visualızation
        #v.draw_state(current_state)
        if current_state.isStateGoal():
            print('Found a Solution')
            print('One of the solutions paths is as follows:')
            get_solution_path(current_state)
            isSolutionFound = True
            break
        else:
            current_state.create_possible_edges()
            for child in current_state.children:
                bfs_queue.put(child)

    if not isSolutionFound:
        print('No Solution is found by exhaustively searching list of possible paths\n')


def pprint_tree(node, file=None, _prefix="", _last=True):
    """
    Pretty print tree
    Code adapted from https://vallentin.io/2016/11/29/pretty-print-tree
    """
    print(_prefix, "`- " if _last else "|- ", node.value, sep="", file=file)
    _prefix += "   " if _last else "|  "
    child_count = len(node.children)
    for i, child in enumerate(node.children):
        _last = i == (child_count - 1)
        pprint_tree(child, file, _prefix, _last)
        
def print_tree(state, level=0):
    global tree
    path = "\t"*level+ "|___" +repr(state.__str__())+"\n"
    tree+= path
    for each in state.children:
        print_tree(each, level+1)
          

# Code starts from here
initial_state = State(State.total_missionaries, State.total_cannibals, 1, None, [])
bfs_tree_search(initial_state)
print('Tree representing the search space done with Breadth First Search:')
print_tree(initial_state)
print(tree)