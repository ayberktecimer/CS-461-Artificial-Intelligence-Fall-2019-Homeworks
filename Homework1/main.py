xList = [0, 1, 2, 3]
yList = [0, 1, 2, 3]
bList = [0, 1]
stateSpace = []
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

def ifStateValid(state):
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