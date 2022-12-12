import numpy as np
import networkx as nx

# Convert input into numpy array
graph = [[*line.strip()] for line in open('input.txt')]
graph = np.array(graph)

# Find location of S/E and set their values to a/z
S = tuple(*np.argwhere(graph == 'S'))
graph[S] = 'a'
E = tuple(*np.argwhere(graph == 'E'))
graph[E] = 'z'

# Convert 2-D array to directed graph
d_graph = nx.grid_2d_graph(*graph.shape).to_directed()
d_graph = nx.DiGraph([(i, j) for i,j in d_graph.edges() 
                      if ord(graph[j]) <= ord(graph[i]) + 1])

# Find shortest path length to E
shortest_path = nx.shortest_path_length(d_graph, target=E)

# Part 1
print(shortest_path[S]) 

# Part 2
print(min(shortest_path[a] for a in shortest_path if graph[a] == 'a'))
