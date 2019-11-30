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

def compute_class_precedence(graph):
    fish_hook_pairs = []
    # until al the fish-hook pairs are eliminated
    precedence_list = []
    fish_hook_pairs_len = calculate_dict_length(fish_hook_pairs)
    while fish_hook_pairs_len > 0:
        exposed_class_list = find_exposed_classes(fish_hook_pairs)
        new_exposed_class = select_exposed_class(exposed_class_list,precedence_list,graph)
        precedence_list.append(new_exposed_class)
        strike_fish_hook_pairs(fish_hook_pairs, new_exposed_class)
        fish_hook_pairs_len = calculate_dict_length(fish_hook_pairs)

# strike all fish-hook pairs that contain the newly added class
def strike_fish_hook_pairs(fish_hook_pairs, class_instance):
    for key in fish_hook_pairs.keys():
        value_list = fish_hook_pairs[key]
        new_value_list = []
        for value in value_list:
            if not value[0] == class_instance:
                new_value_list.append(value)
        fish_hook_pairs[key] = new_value_list

def calculate_dict_length(dict):
    dict_len = 0
    for key, value in dict.items():
        dict_len+=len(value)
    return dict_len

    
# find the exposed classes
def find_exposed_classes(fish_hook_pairs):
    class_list = fish_hook_pairs.getkeys()
    for key, value_list in fish_hook_pairs.items():
        for value in value_list:
            if value[1] in class_list:
                class_list.remove(value[1])
    return class_list

#select the exposed class that is a direct superclass of the lowest-recedence class on the emerging class-precedence list.
def select_exposed_class(exposed_class_list,precedence_list,graph):
    if len(exposed_class_list) == 1:
        return exposed_class_list[0]
    else:
        p_list_value = len(precedence_list)
        while p_list_value > 0:
            for class_instance in exposed_class_list:
                is_superclass = is_direct_superclass(class_instance,graph,precedence_list[p_list_value-1])
                if is_superclass:
                    return class_instance
            p_list_value-=1
        
        print('Something is wrong. May god forgive us')


def is_direct_superclass(class_instance,graph,lowest_precedence_class):
    superclasses = graph[lowest_precedence_class]
    if class_instance in superclasses:
        return True
    else:
        return False


