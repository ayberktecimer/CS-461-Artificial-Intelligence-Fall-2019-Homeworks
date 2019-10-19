import queue


class State:
    def __init__(self, m, c, b, parent, children):
        self.m = m
        self.c = c
        self.b = b
        self.parent = parent
        self.children = children

    def create_possible_edges(self):
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
        y = self.c
        x = self.m
        b = self.b
        if y < 0 or y > 3 or x < 0 or x > 3:
            return False
        if y > x > 0:
            return False
        if 3 - y > 3 - x > 0:
            return False
        if b == 1 and x == 0 and y == 0:
            return False
        if b == 0 and x == 3 and y == 3:
            return False
        return True

    def isLoopFree(self, parent):
        if parent is None:
            return True
        return not (self == parent) and self.isLoopFree(parent.parent)

    def __eq__(self, other):
        return self.m == other.m and self.c == other.c and self.b == other.b

    def __str__(self):
        return str(self.m) +"M"+ str(self.c) + 'C' + str(self.b)

    def isStateGoal(self):
        if self.m == 0 and self.c == 0 and self.b == 0:
            return True
        else:
            return False


def get_solution_path(goal_state):
    path = []
    current_state = goal_state
    while current_state is not None:
        path.append(current_state)
        current_state = current_state.parent
    path = path[::-1]
    for state in path:
        print(state)

initial_state = State(3, 3, 1, None, [])


def bfs_tree_search(root):
    bfs_queue = queue.Queue()
    bfs_queue.put(root)
    while not bfs_queue.empty():
        current_state = bfs_queue.get()
        if current_state.isStateGoal():
            #print(current_state)
            print('Solution Bulundu')
            get_solution_path(current_state)
            exit(0)
        else:
            current_state.create_possible_edges()
            for child in current_state.children:
                bfs_queue.put(child)
    print('No Solution')
bfs_tree_search(initial_state)