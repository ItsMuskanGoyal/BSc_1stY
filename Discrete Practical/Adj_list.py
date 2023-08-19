# Write a program to check if a given graph is complete graph. represent the graph using the Adjacency List representation 


def is_complete_graph(adjacency_list):
    num_vertices = len(adjacency_list)
    
    for vertex in range(num_vertices):
        if len(adjacency_list[vertex]) != num_vertices - 1:
            return False
    
    return True

# Example adjacency list for a graph (5 vertices)
graph_adjacency_list = [
    [1, 2, 3, 4],
    [0, 2, 3, 4],
    [0, 1, 3, 4],
    [0, 1, 2, 4],
    [0, 1, 2, 3]
]

if is_complete_graph(graph_adjacency_list):
    print("The given graph is a complete graph.")
else:
    print("The given graph is not a complete graph.")
