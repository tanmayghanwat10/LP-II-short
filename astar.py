def a_star(start_node, stop_node):
    open_set = set([start_node])  # Initialize the open set with the start node
    closed_set = set()  # Initialize the closed set
    g = {start_node: 0}  # Initialize the g scores with the start node having a g score of 0
    parents = {start_node: start_node}  # Initialize the parent map with the start node being its own parent

    # Loop until the open set is empty
    while open_set:
        # Find the node with the lowest f score from the open set
        n = min(open_set, key=lambda node: g[node] + heuristic(node))

        # Check if the current node is the destination or a dead-end
        if n == stop_node or not Graph_nodes[n]:
            pass  # If so, do nothing and continue to the next iteration
        else:
            # Explore neighbors of the current node
            for m, weight in get_neighbors(n):
                # Calculate the tentative g score for the neighbor
                new_g = g[n] + weight
                
                # If the neighbor is new or a better path is found to it
                if m not in open_set and m not in closed_set:
                    # Add the neighbor to the open set
                    open_set.add(m)
                    # Update its parent and g score
                    parents[m] = n
                    g[m] = new_g
                elif new_g < g[m]:
                    # Update the neighbor's g score and parent
                    g[m] = new_g
                    parents[m] = n
                    if m in closed_set:
                        # If the neighbor was previously explored, move it back to the open set
                        closed_set.remove(m)
                        open_set.add(m)

        # If no path exists or the destination is reached
        if n is None:
            print('Path does not exist!')
            return None
        elif n == stop_node:
            # Reconstruct and return the path
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('Path found:', path)
            return path

        # Remove the current node from the open set and add it to the closed set
        open_set.remove(n)
        closed_set.add(n)

    # If the loop ends without finding a path
    print('Path does not exist!')
    return None


# Function to get neighbors of a node from the graph
def get_neighbors(v):
    return Graph_nodes.get(v, None)


# Heuristic function to estimate distance to the goal
def heuristic(n):
    H_dist = {'A': 11, 'B': 6, 'C': 99, 'D': 1, 'E': 7, 'G': 0}
    return H_dist.get(n, 0)


# Define the graph
Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': None,
    'E': [('D', 6)],
    'D': [('G', 1)],
}

# Call the A* algorithm with start and stop nodes
a_star('A', 'G')
