"""
Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
"""

# Node class
class Node: 
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors else []

"""
***Clone the graph when given input is node object (first node of the graph)***
Test case format:
For simplicity, each node's value is the same as the node's index (1-indexed). 
For example, the first node with val == 1, the second node with val == 2, and so on. 
The graph is represented in the test case using an adjacency list.
An adjacency list is a collection of unordered lists used to represent a finite graph. 
Each list describes the set of neighbors of a node in the graph.
The given node will always be the first node with val = 1. 
You must return the copy of the given node as a reference to the cloned graph.
"""
def clone_graph1(node):
    # Hint: Use a dictionary with key is the orignal node, and the value is the copy of that node

    # Use BFS to get all the node (DFS also works)
    if not node:
        return None
    
    from collections import deque
    q = deque([node])
    # Node dictionary
    node_dict = {} # original: copys
    node_dict[node] = Node(node.val) # Add first node node_dict
    while q:
        # Pop first node from the queue
        curr = q.popleft()
        # Make a copy of the curr
        # copy = Node(curr.val)  # this copy doesn't have any neighbor, just a deep copy of the current node without neighbors

        # Now Add them to node_dict
        # node_dict[curr] = copy

        # Explore the current node's neighbors, and keep building node_dict
        for nei in curr.neighbors:
            # Only process unvisited neighbors, so we don't add 1 node twice. That's the reason why using dict comes in handy
            # It allows us to check if the node we already process or not, and the key(original node) give us the reference of its neighbors
            # So we can use that to make connections for our copy nodes
            if nei not in node_dict:
                # Append nei of current node to the queue
                q.append(nei)
                # Make a copy of nei
                # Add to node_dict
                node_dict[nei] = Node(nei.val)
            # Neighbor of current also neighbor of copy of current
            node_dict[curr].neighbors.append(node_dict[nei])

    return node_dict[node]

"""
***Input is an adjacency list***
e.g: adj_list = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 4],
    4: [2, 3]
}
"""
def clone_graph2(adj_list):
    # Convert the adjacency list to node object and make the connections

    if not adj_list:
        return None
    
    # First make a dictionary of node objects
    node_dict = {}
    for node_val in adj_list:
        node_dict[node_val] = Node(node_val)

    # Make the connections:
    for node_val, neighbors in adj_list.items():
        for nei in neighbors:
            node_dict[node_val].neighbors.append(node_dict[nei])
    # Get the first node
    first_node = node_dict[list(node_dict.keys())[0]]
    return first_node


