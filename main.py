# ilya yaverbaum, Dijkstra algorithm implementation, 16.11.22
# Based on code from stackoverflow.com

# first graph
nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
distances = {
    'A': {'B': 1.5, 'E': 2},
    'B': {'C': 2},
    'D': {'G': 4},
     'G': {},
    'C': {'D': 3},
    'E': {'F': 3},
    'F': {'G': 2}}

# # second graph
# nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
# distances = {
#     'A': {'B': 9, 'C': 15, 'D': 14},
#     'B': {'H': 24},
#     'D': {'H': 18, 'C': 5, 'E': 30},
#     'G': {},
#     'C': {'G': 44, 'E': 20},
#     'E': {'G': 16, 'F': 11},
#     'F': {'H': 6, 'G': 6},
#     'H': {'C': 2, 'G': 19}}

# # third graph
# nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J')
# distances = {
#     'A': {'B': 6, 'F': 3, 'D': 14},
#     'B': {'C': 3, 'D': 2,},
#     'D': {'E': 8},
#     'G': {'I': 3},
#     'C': {'E': 5, 'D': 1},
#     'E': {'J': 5},
#     'F': {'H': 7, 'G': 1},
#     'H': {'I': 2},
#     'I': {'J': 3, 'E': 5},
#     'J': {}}




unvisited = {node: None for node in nodes} #using None as +inf
visited = {}
current = 'A'
currentDistance = 0
unvisited[current] = currentDistance

while True:
    for neighbour, distance in distances[current].items():
        if neighbour not in unvisited: continue
        newDistance = currentDistance + distance
        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
            unvisited[neighbour] = newDistance
    visited[current] = currentDistance
    del unvisited[current]
    if not unvisited: break
    candidates = [node for node in unvisited.items() if node[1]]
    current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

print(visited)