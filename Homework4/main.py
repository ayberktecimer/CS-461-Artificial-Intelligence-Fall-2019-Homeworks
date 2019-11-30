"""
CS461 Homework4
Fall 2019

Adahan Yalçınkaya 21502369
Bengi Dönmez 21602237
Emre Sülün 21502214
Eray Şahin 21502758
Kazım Ayberk Tecimer 21502531
"""
import copy

# The first example as a adjacency list
example1_graph = {
    "CAIVehicle": ["CPuppet"],
    "CPuppet": ["CPipeUser"],
    "CAIPlayer": ["CAIActor"],
    "CPipeUser": ["CAIActor"],
    "CAIActor": ["CAIObject"],
    "CAIObject": ["Everything"],
    "Everything": []
}

# The second example as a adjacency list
example2_graph = {
    "fstream": ["iostream"],
    "iostream": ["istream", "ostream"],
    "ifstream": ["istream"],
    "ofstream": ["ostream"],
    "istream": ["ios"],
    "ostream": ["ios"],
    "ios": ["Everything"],
    "Everything": []
}

# The third example as a adjacency list
example3_graph = {
    "Consultant Manager": ["Consultant", "Manager"],
    "Director": ["Manager"],
    "Permanent Manager": ["Manager", "Permanent Employee"],
    "Consultant": ["Temporary Employee"],
    "Manager": ["Employee"],
    "Permanent Employee": ["Employee"],
    "Temporary Employee": ["Employee"],
    "Employee": ["Everything"],
    "Everything": []
}


def compute_class_precedence(graph, initial_node):
    '''
    Class precedence list code is adapted from Winston Chapter 9 pg.197
    To compute an instance's class-precedence list
    Create fish-hook pairs
    Until all the fish-hook pairs are eliminated:
        Find the exposed classes
        Select the exposed class that is a direct superclass of the lowest-precedence class on the emerging class-precedence list
        Add the selected class to the emerging class-precedence list
        Strike all fish-hook pairs that contain the newly added class
    '''
    # Create fish-hook pairs
    fish_hook_pairs = create_fish_hook_pairs(graph, initial_node)

    # Define a predence list (initially empty)
    precedence_list = []

    # Count the number of fish-hook pairs
    fish_hook_pairs_len = calculate_dict_length(fish_hook_pairs)

    # Get the list of all possible names (e.g. ["Crazy", "Professors", "Eccentrics", ...])
    class_list = list(fish_hook_pairs.keys())

    # Until all the fish-hook pairs are eliminated
    while fish_hook_pairs_len > 0:

        # Find the exposed classes
        exposed_class_list = find_exposed_classes(fish_hook_pairs, class_list)

        # If there are more than one class to expose, select the one that is a direct superclass of the lowest-precedence class on the emerging class-precedence list
        new_exposed_class = select_exposed_class(exposed_class_list, precedence_list, graph)

        # Append the selected (exposed) class to the end of the precedence list
        precedence_list.append(new_exposed_class)

        # Strike the fish-hook pairs which include the exposed class
        strike_fish_hook_pairs(fish_hook_pairs, new_exposed_class)
        class_list.remove(new_exposed_class)

        # Get the number of fish-hook pairs, again
        fish_hook_pairs_len = calculate_dict_length(fish_hook_pairs)

    return precedence_list

# Strike all fish-hook pairs that contain the newly added class
def strike_fish_hook_pairs(fish_hook_pairs, class_instance):

    for key in fish_hook_pairs.keys():
        value_list = fish_hook_pairs[key]
        new_value_list = []
        # Maintain only those pairs which do not include "class_instance"
        for value in value_list:
            if not value[0] == class_instance:
                new_value_list.append(value)
        # Update the fish-hook pairs (the pairs containing the exposed class are removed)
        fish_hook_pairs[key] = new_value_list

# Return the number of fish-hook pairs
def calculate_dict_length(dict):
    dict_len = 0
    for key, value in dict.items():
        dict_len+=len(value)
    return dict_len


# Find the exposed classes
def find_exposed_classes(fish_hook_pairs,class_list):
    class_list_temp = copy.deepcopy(class_list)
    for key, value_list in fish_hook_pairs.items():
        for value in value_list:
            if value[1] in class_list_temp:
                class_list_temp.remove(value[1])
    return class_list_temp


# Select the exposed class that is a direct superclass of the lowest-precedence class on the emerging class-precedence list.
def select_exposed_class(exposed_class_list, precedence_list, graph):
    # If there is one option, then that class is the one to expose
    if len(exposed_class_list) == 1:
        return exposed_class_list[0]
    # When there are multiple classes that can be exposed, select the one which is a direct superclass of the lowest-precedence class
    else:
        # Traverse the precedence list, starting with the lowest-precedence
        p_list_value = len(precedence_list)
        while p_list_value > 0:
            for class_instance in exposed_class_list:
                is_superclass = is_direct_superclass(class_instance,graph,precedence_list[p_list_value-1])
                if is_superclass:
                    return class_instance
            p_list_value -= 1
        
def create_fish_hook_pairs(graph, node):
    """ This function creates fish hook pairs for a given graph adjacency list
    and initial node by following the parents of target node
    """
    pairs = {} # Fish hook pairs that will be returned
    queue = [] # Queue of nodes that will be processed
    visited = set([]) # Mark nodes as visited to avoid unnecessary processing

    queue.append(node)
    while len(queue) != 0:
        targetNode = queue[0]
        combinedList = [targetNode] + graph[targetNode]

        # Add parents of the target node to queue
        for parent in graph[targetNode]:
            if parent not in visited:
                queue.append(parent)
                visited.add(parent)
        
        # Create fish hook pairs of the target node
        for i, value in enumerate(combinedList):
            if i != len(combinedList) - 1:
                if targetNode in pairs:
                    pairs[targetNode].append((value, combinedList[i+1]))    
                else:
                    pairs[targetNode] = [(value, combinedList[i+1])]

        # Remove processed node from queue
        del queue[0]
    
    pairs['Everything'] = []
    return pairs

# Checks whether a node is a direct superclass of another one
def is_direct_superclass(class_instance, graph, lowest_precedence_class):
    superclasses = graph[lowest_precedence_class]
    if class_instance in superclasses:
        return True
    else:
        return False

# Code starts from here
print('\nResults for Example 1: ')
print('\nInitial Node is CAIVehicle')
print(' -> '.join(compute_class_precedence(example1_graph,'CAIVehicle')))
print('\nInitial Node is CAIPlayer')
print(' -> '.join(compute_class_precedence(example1_graph,'CAIPlayer')))

print('\nResults for Example 2: ')
print('\nInitial Node is ifstream')
print(' -> '.join(compute_class_precedence(example2_graph,'ifstream')))
print('\nInitial Node is fstream')
print(' -> '.join(compute_class_precedence(example2_graph,'fstream')))
print('\nInitial Node is ofstream')
print(' -> '.join(compute_class_precedence(example2_graph,'ofstream')))

print('\nResults for Example 3: ')
print('\nInitial Node is Consultant Manager')
print(' -> '.join(compute_class_precedence(example3_graph,'Consultant Manager')))
print('\nInitial Node is Director')
print(' -> '.join(compute_class_precedence(example3_graph,'Director')))
print('\nInitial Node is Permanent Manager')
print(' -> '.join(compute_class_precedence(example3_graph,'Permanent Manager')))