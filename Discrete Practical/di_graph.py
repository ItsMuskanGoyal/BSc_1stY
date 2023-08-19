# Write a program to accept a directed graph G and compute the in degree and out degree of each vertex

def compute_degrees(adjacency_list):
    num_vertices = len(adjacency_list)
    in_degrees = [0] * num_vertices
    out_degrees = [0] * num_vertices
    
    for vertex, neighbors in enumerate(adjacency_list):
        out_degrees[vertex] = len(neighbors)
        for neighbor in neighbors:
            in_degrees[neighbor] += 1
    
    return in_degrees, out_degrees

# Example adjacency list for a directed graph (5 vertices)
directed_graph_adjacency_list = [
    [1, 2],
    [2, 3],
    [3],
    [0, 4],
    [1]
]

in_degrees, out_degrees = compute_degrees(directed_graph_adjacency_list)

for vertex in range(len(directed_graph_adjacency_list)):
    print(f"Vertex {vertex}: In-Degree = {in_degrees[vertex]}, Out-Degree = {out_degrees[vertex]}")
