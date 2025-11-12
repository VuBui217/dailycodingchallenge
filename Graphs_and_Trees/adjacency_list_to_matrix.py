"""
                                                Build an Adjacency List to Matrix Converter
Build a function that converts an adjacency list representation of a graph into an adjacency matrix. An adjacency list is a dictionary where each key represents a node, and the corresponding value is a list of nodes that the key node is connected to. An adjacency matrix is a 2D array where the entry at position [i][j] is 1 if there's an edge from node i to node j, and 0 otherwise.

For example, given the adjacency list:

Example Code
{
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [2]
}
The corresponding adjacency matrix would be:

Example Code
[
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 1, 0]
]       
"""

def adjacency_list_to_matrix(adjacency_list):
    n = len(adjacency_list)
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    # Build matrix
    for v, neighbors in adjacency_list.items():
        for nei in neighbors:
            matrix[v][nei] = 1
    
    # Print matrix:
    for r in range(n):
        print(matrix[r])
    
    return matrix

