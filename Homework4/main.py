"""
CS461 Homework4
Fall 2019

Adahan Yalçınkaya 21502369
Bengi Dönmez 21602237
Emre Sülün 21502214
Eray Şahin 21502758
Kazım Ayberk Tecimer 21502531
"""

graph = {
    'Crazy': ['Professors','Hackers'],
    'Professors': ['Eccentrics', 'Teachers'],
    'Hackers': ['Eccentrics','Programmers'],
    'Eccentrics': ['Dwarfs'],
    'Teachers': ['Dwarfs'],
    'Programmers': ['Dwarfs'],
    'Dwarfs': ['Everything'],
    "Everything": []
}

def get_reachable_path():
    return -1

def create_fish_hook_pairs(node):
    pairs = {}
    queue = []
    visited = set([])

    queue.append(node)
    while len(queue) != 0:
        targetNode = queue[0]
        combinedList = [targetNode] + graph[targetNode]
        for parent in graph[targetNode]:
            if parent not in visited:
                queue.append(parent)
                visited.add(parent)
        
        for i, value in enumerate(combinedList):
            if i != len(combinedList) - 1:
                if targetNode in pairs:
                    pairs[targetNode].append((value, combinedList[i+1]))    
                else:
                    pairs[targetNode] = [(value, combinedList[i+1])]


        del queue[0]
    
    print("Pairs", pairs)

def print_topological_sort(initial_node,graph):
    pass

create_fish_hook_pairs("Crazy")


