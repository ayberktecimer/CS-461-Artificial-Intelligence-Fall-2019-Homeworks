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
}

def get_reachable_path():
    return -1

def create_fish_hook_pairs(graph,node):
    pairs = []
    for i in range(0,len(graph[node])):
        
    pairs.append([node, graph[node][0]])
    


def print_topological_sort(initial_node,graph):


