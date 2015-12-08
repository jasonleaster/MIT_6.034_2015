from search import Edge, UndirectedGraph, do_nothing_fn, make_generic_search
import read_graphs

all_graphs = read_graphs.get_graphs()
GRAPH_0 = all_graphs['GRAPH_0']
GRAPH_1 = all_graphs['GRAPH_1']
GRAPH_2 = all_graphs['GRAPH_2']
GRAPH_3 = all_graphs['GRAPH_3']
GRAPH_FOR_HEURISTICS = all_graphs['GRAPH_FOR_HEURISTICS']

#Change this to True if you want to run additional local tests for debugging:
RUN_ADDITIONAL_TESTS = False

#### PART 1: Helper Functions #########################################

def path_length(graph, path):
    
    if len(path) <= 1:
        return 0

    length = 0

    i = 1
    for i in range(1, len(path)):
        startNode = path[i-1]
        endNode = path[i]
        edge = graph.get_edge(startNode, endNode)
        length += edge.length

    return length


def has_loops(path):
    viewed = []
    for i in path:
        if not (i in viewed):
            viewed.append(i)
        else:
            return True

    return False



def extensions(graph, path):

    neighbors = graph.get_neighbors(path[-1])
    exten = [path + [i] for i in neighbors]
    i = 0
    while i < len(exten):
        if has_loops(exten[i]):
            exten.remove(exten[i])
            continue
        else:
            i += 1
    return exten


def sort_by_heuristic(graph, goalNode, nodes):
    dic = {}
    for n in nodes:
        dic[n] = graph.get_heuristic_value(n, goalNode)

    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            if dic[nodes[i]] > dic[nodes[j]]:
                nodes[i], nodes[j] = nodes[j], nodes[i]

    return nodes

# You can ignore the following line.  It allows generic_search (PART 3) to 
# access the extensions and has_loops functions that you defined in PART 1.
generic_search = make_generic_search(extensions, has_loops)  # DO NOT CHANGE

#### PART 2: Search Algorithms #########################################

# Note: Optionally, you may skip to Part 3: Generic Search,
# then complete Part 2 using your answers from Part 3.

def dfs(graph, startNode, goalNode):
    visited = []
    S = [startNode]
    path = []
    while len(S) != 0:
        node = S.pop(0)
        path.append(node)
        visited.append(node)
        if graph.get_edge(node, goalNode):
            return path + [goalNode]

        neighbors = graph.get_neighbors(node)
        i = 0

        while i < len(neighbors):
            if neighbors[i] in S or neighbors[i] in visited:
            #if neighbors[i] in visited:
                neighbors.remove(neighbors[i])
            else:
                i += 1

        if len(neighbors) == 0:
            path.pop()
        else:
            neighbors.sort()
            S = neighbors + S
    return None

def bfs(graph, startNode, goalNode):
    Q = [startNode]
    visited = []
    path = []
    while len(Q) != 0:
        node = Q.pop(0)
        path.append(node)
        if node in visited:
            path.pop()
        else:
            visited.append(node)
            if graph.get_edge(node, goalNode):
                return path
            neighbors = graph.get_neighbors(node)
            for n in neighbors:
                if not(n in visited):
                    Q.append(n)

    return None
            



def hill_climbing(graph, startNode, goalNode):
    raise NotImplementedError


def best_first(graph, startNode, goalNode):
    raise NotImplementedError


def beam(graph, startNode, goalNode, beam_width):
    raise NotImplementedError


def branch_and_bound(graph, startNode, goalNode):
    raise NotImplementedError


def branch_and_bound_with_heuristic(graph, startNode, goalNode):
    raise NotImplementedError


def branch_and_bound_with_extended_set(graph, startNode, goalNode):
    raise NotImplementedError


def a_star(graph, startNode, goalNode):
    raise NotImplementedError


#### PART 3: Generic Search #######################################

# Define your custom path-sorting functions here.  
# Each path-sorting function should be in this form:

# def my_sorting_fn(graph, goalNode, paths):
#     # YOUR CODE HERE
#     return sorted_paths




generic_dfs = [None, None, None, None]

generic_bfs = [None, None, None, None]

generic_hill_climbing = [None, None, None, None]

generic_best_first = [None, None, None, None]

generic_branch_and_bound = [None, None, None, None]

generic_branch_and_bound_with_heuristic = [None, None, None, None]

generic_branch_and_bound_with_extended_set = [None, None, None, None]

generic_a_star = [None, None, None, None]

# Here is an example of how to call generic_search (uncomment to run):
#my_dfs_fn = generic_search(*generic_dfs)
#my_dfs_path = my_dfs_fn(GRAPH_2, 'S', 'G')
#print my_dfs_path

# Or, combining the first two steps:
#my_dfs_path = generic_search(*generic_dfs)(GRAPH_2, 'S', 'G')
#print my_dfs_path


### OPTIONAL: Generic Beam Search
# If you want to run local tests for generic_beam, change TEST_GENERIC_BEAM to True:
TEST_GENERIC_BEAM = False

# The sort_agenda_fn for beam search takes fourth argument, beam_width:
# def my_beam_sorting_fn(graph, goalNode, paths, beam_width):
#     # YOUR CODE HERE
#     return sorted_beam_agenda

generic_beam = [None, None, None, None]

# Uncomment this to test your generic_beam search:
#print generic_search(*generic_beam)(GRAPH_2, 'S', 'G', beam_width=2)


#### PART 4: Heuristics ###################################################

def is_admissible(graph, goalNode):
    raise NotImplementedError


def is_consistent(graph, goalNode):
    raise NotImplementedError


### OPTIONAL: Picking Heuristics
# If you want to run local tests on your heuristics, change TEST_HEURISTICS to True:
TEST_HEURISTICS = False

# heuristic_1: admissible and consistent

[h1_S, h1_A, h1_B, h1_C, h1_G] = [None, None, None, None, None]

heuristic_1 = {'G': {}}
heuristic_1['G']['S'] = h1_S
heuristic_1['G']['A'] = h1_A
heuristic_1['G']['B'] = h1_B
heuristic_1['G']['C'] = h1_C
heuristic_1['G']['G'] = h1_G


# heuristic_2: admissible but NOT consistent

[h2_S, h2_A, h2_B, h2_C, h2_G] = [None, None, None, None, None]

heuristic_2 = {'G': {}}
heuristic_2['G']['S'] = h2_S
heuristic_2['G']['A'] = h2_A
heuristic_2['G']['B'] = h2_B
heuristic_2['G']['C'] = h2_C
heuristic_2['G']['G'] = h2_G


# heuristic_3: admissible but A* returns non-optimal path to G

[h3_S, h3_A, h3_B, h3_C, h3_G] = [None, None, None, None, None]

heuristic_3 = {'G': {}}
heuristic_3['G']['S'] = h3_S
heuristic_3['G']['A'] = h3_A
heuristic_3['G']['B'] = h3_B
heuristic_3['G']['C'] = h3_C
heuristic_3['G']['G'] = h3_G


# heuristic_4: admissible but not consistent, yet A* finds optimal path

[h4_S, h4_A, h4_B, h4_C, h4_G] = [None, None, None, None, None]

heuristic_4 = {'G': {}}
heuristic_4['G']['S'] = h4_S
heuristic_4['G']['A'] = h4_A
heuristic_4['G']['B'] = h4_B
heuristic_4['G']['C'] = h4_C
heuristic_4['G']['G'] = h4_G


#### SURVEY ###################################################

NAME = None
COLLABORATORS = None
HOW_MANY_HOURS_THIS_LAB_TOOK = None
WHAT_I_FOUND_INTERESTING = None
WHAT_I_FOUND_BORING = None
SUGGESTIONS = None


###########################################################
### Ignore everything below this line; for testing only ###
###########################################################

# The following lines are used in the tester. DO NOT CHANGE!

generic_dfs_sort_new_paths_fn = generic_dfs[0]
generic_bfs_sort_new_paths_fn = generic_bfs[0]
generic_hill_climbing_sort_new_paths_fn = generic_hill_climbing[0]
generic_best_first_sort_new_paths_fn = generic_best_first[0]
generic_branch_and_bound_sort_new_paths_fn = generic_branch_and_bound[0]
generic_branch_and_bound_with_heuristic_sort_new_paths_fn = generic_branch_and_bound_with_heuristic[0]
generic_branch_and_bound_with_extended_set_sort_new_paths_fn = generic_branch_and_bound_with_extended_set[0]
generic_a_star_sort_new_paths_fn = generic_a_star[0]

generic_dfs_sort_agenda_fn = generic_dfs[2]
generic_bfs_sort_agenda_fn = generic_bfs[2]
generic_hill_climbing_sort_agenda_fn = generic_hill_climbing[2]
generic_best_first_sort_agenda_fn = generic_best_first[2]
generic_branch_and_bound_sort_agenda_fn = generic_branch_and_bound[2]
generic_branch_and_bound_with_heuristic_sort_agenda_fn = generic_branch_and_bound_with_heuristic[2]
generic_branch_and_bound_with_extended_set_sort_agenda_fn = generic_branch_and_bound_with_extended_set[2]
generic_a_star_sort_agenda_fn = generic_a_star[2]
