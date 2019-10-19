xList = [0, 1, 2, 3]
yList = [0, 1, 2, 3]
bList = [0, 1]
stateSpace = []
print('')
'''i = 0
for x in xList:
    for y in yList:
        for b in bList:
            state = {
                'x': x,
                'y': y,
                'b': b
            }
            stateSpace.append(state)
'''


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
            possibleChildren.append(State(self.m - 2, self.c, 0, self, None))
            possibleChildren.append(State(self.m, self.c - 2, 0, self, None))
            possibleChildren.append(State(self.m - 1, self.c - 1, 0, self, None))
            possibleChildren.append(State(self.m - 1, self.c, 0, self, None))
            possibleChildren.append(State(self.m, self.c - 1, 0, self, None))
        else:
            possibleChildren.append(State(self.m + 2, self.c, 1, self, None))
            possibleChildren.append(State(self.m, self.c + 2, 1, self, None))
            possibleChildren.append(State(self.m + 1, self.c + 1, 1, self, None))
            possibleChildren.append(State(self.m + 1, self.c, 1, self, None))
            possibleChildren.append(State(self.m, self.c + 1, 0, self, None))

        for child in possibleChildren:
            if child.isStateValid():
                self.children.append(child)

    def isStateValid(self):
        y = self.c
        x = self.m
        b = self.b

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


initialState = {
    'x': 3,
    'y': 3,
    'b': 1,
    'isVisited': False
}

graph = {}

create_possible_edges(initialState, graph)

print(graph)

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

    beforeLeftCount = fromState['x'] + fromState['y']
    afterLeftCount = toState['x'] + toState['y']

    if abs(afterLeftCount - beforeLeftCount) > 2:
        return False

    return True
'''

'''
for state1 in validSpaceState:
    for state2 in validSpaceState:
        if state1 != state2:
            print(isTransitionValid(state1, state2), "from:", state1, "to:", state2)

print(stateSpace)
'''
