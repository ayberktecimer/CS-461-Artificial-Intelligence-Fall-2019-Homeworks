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
    def __init__(self, m, c, b,parent, child):
        self.m = m
        self.c = c
        self.b = b
        self.parent = parent
        self.child = child

def isStateValid(state):
    y = state['y']
    x = state['x']
    b = state['b']

    if y > x > 0:
        return False
    if 3 - y > 3 - x > 0:
        return False
    if b == 1 and x == 0 and y == 0:
        return False
    if b == 0 and x == 3 and y == 3:
        return False
    return True

initialState = {
    'x': 3,
    'y': 3,
    'b': 1,
    'isVisited': False
}

graph ={}
def create_possible_edges(state,graph):
    possible_nstate1 = {
        'x': state['x'] -2 ,
        'y': state['y'],
        'b': 0 if state['b'] == 1 else 1

    }

    possible_nstate2 = {
        'x': state['x'] ,
        'y': state['y'] -2,
        'b': 0 if state['b'] == 1 else 1
    }

    possible_nstate3 = {
        'x': state['x'] -1,
        'y': state['y'] -1,
        'b': 0 if state['b'] == 1 else 1
    }
    valid_states = []
    if isStateValid(possible_nstate1):
         valid_states.append(possible_nstate1)

    if isStateValid(possible_nstate2):
        valid_states.append(possible_nstate2)

    if isStateValid(possible_nstate3):
        valid_states.append(possible_nstate3)

    graph[str(len(graph))] = valid_states
create_possible_edges(initialState,graph)

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