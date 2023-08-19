# Write a program to check if a given graph is complete graph. represent the graph using the Adjacency Matrix representation 



def is_complete_graph(adjacency_matrix):
    num_vertices = len(adjacency_matrix)
    
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i != j and adjacency_matrix[i][j] != 1:
                return False
    
    return True

# Example adjacency matrix for a graph (5 vertices)
# 0 means no edge, 1 means edge exists
graph_adjacency_matrix = [
    [0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0]
]

if is_complete_graph(graph_adjacency_matrix):
    print("The given graph is a complete graph.")
else:
    print("The given graph is not a complete graph.")
