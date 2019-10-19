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

    def isStateGoal(self):
        if self.m == 0 and self.c == 0 and self.b == 0:
            return True
        else:
            return False

initialState = State(3, 3, 1, None, [])
print("aaa")
initialState.create_possible_edges()
for each in initialState.children:
    each.create_possible_edges()
    print("M: ", each.m)
    print("C: ", each.c)
    print("B: ", each.b)
    print("TRANSITIOOOON")
    print()
    for child in each.children:
        print("M: ", child.m)
        print("C: ", child.c)
        print("B: ", child.b)
        print("children: ", child.children)
        print("transition over")




'''
ilk yaptigimiz system yani her state ve transitioni bulup sonra valid olanlari filtreleyerek
graph yaratmak ve o graph uzerinden bfs calistirmak

initial stateden dinamik sekilde check ederek graphi olustur dfs kostur
3 DEGIL 6
GRAPHI OLUSTUR ERAY'S METHOD
ERAY'S METHODA DFS AT
'''
'''
validSpaceState = []
for state in stateSpace:
    if ifStateValid(state):
        validSpaceState.append(state)
'''

'''
def isTransitionValid(fromState, toState):
    if fromState['b'] == toState['b']:
        return False


initial_state = State(4,4,1,None,None)


def bfs_tree_search(root):
    bfs_queue = queue.Queue()
    bfs_queue.put(root)
    while not bfs_queue.empty():
        current_state = bfs_queue.get()
        if current_state.isStateGoal():
            print('Solution Bulundu')
        else:
            '''
            call create children function
            '''
            for child in current_state.children:
                bfs_queue.put(child)
    print('No Solution')