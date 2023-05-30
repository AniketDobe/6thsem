import sys

def dijkstraMST(graph):
    num_vertices = len(graph)
    key = [sys.maxsize] * num_vertices
    parent = [-1] * num_vertices
    MSTSet = set()

    # Set the first vertex as the root
    key[0] = 0

    for _ in range(num_vertices):
        # Find the vertex with the minimum key value
        u = minKey(key, MSTSet)
        MSTSet.add(u)

        # Update key and parent values of adjacent vertices
        for v in range(num_vertices):
            if graph[u][v] > 0 and v not in MSTSet and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    return parent


def minKey(key, MSTSet):
    min_value = sys.maxsize
    min_index = -1

    for v in range(len(key)):
        if key[v] < min_value and v not in MSTSet:
            min_value = key[v]
            min_index = v

    return min_index


# Example usage
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

mst_parent = dijkstraMST(graph)
print("Edge \tWeight")
for i in range(1, len(graph)):
    print(mst_parent[i], "-", i, "\t", graph[i][mst_parent[i]])
