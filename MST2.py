import sys # For INT_MAX

def primMST(graph):
    V = len(graph) # Number of vertices in the graph
    key = [sys.maxsize] * V # Initialize all keys as INFINITE
    parent = [None] * V # To store the resultant MST
    key[0] = 0 # Make key 0 so that this vertex is picked first
    mstSet = [False] * V

    for cout in range(V):
        # Pick the minimum key vertex from the set of vertices
        # not yet included in MST
        u = minKey(key, mstSet)

        # Add the picked vertex to the MST Set
        mstSet[u] = True

        # Update key value and parent index of the adjacent vertices of
        # the picked vertex. Consider only those vertices which are not
        # yet included in MST
        for v in range(V):
            # graph[u][v] is non zero only for adjacent vertices of m
            # mstSet[v] is false for vertices not yet included in MST
            # Update the key only if graph[u][v] is smaller than key[v]
            if graph[u][v] > 0 and mstSet[v] == False and key[v] > graph[u][v]:
                key[v] = graph[u][v]
                parent[v] = u

    # print the constructed MST
    printMST(parent, graph)

# A utility function to find the vertex with minimum key value, from
# the set of vertices not yet included in MST
def minKey(key, mstSet):
    min = sys.maxsize
    for v in range(len(key)):
        if key[v] < min and mstSet[v] == False:
            min = key[v]
            min_index = v
    return min_index

# A utility function to print the constructed MST stored in parent[]
def printMST(parent, graph):
    print("Edge \tWeight")
    for i in range(1, len(graph)):
        print(parent[i], "-", i, "\t", graph[i][parent[i]])

# Test the function with a graph
g = [[0, 2, 0, 6, 0],
     [2, 0, 3, 8, 5],
     [0, 3, 0, 0, 7],
     [6, 8, 0, 0, 9],
     [0, 5, 7, 9, 0]]
primMST(g)
