# Disjoint Set/Union Find/Kruskal's Algorithm (Programiz)

# Any minimum spanning tree algorithm revolves around checking if adding an edge creates a loop or not. 

# The most common way to find this out is an algorithm called Union Find.

# The Union-Find algorithm divides the vertices into clusters and allows us to check if two vertices belong to the same cluster or not and hence decide whether adding an edge creates a cycle.

# Ex
# KRUSKAL(G):
# A = ∅
# For each vertex v ∈ G.V:
    MAKE-SET(v)
# For each edge (u, v) ∈ G.E ordered by increasing order by weight(u, v):
#    if FIND-SET(u) ≠ FIND-SET(v):       
#    A = A ∪ {(u, v)}
#    UNION(u, v)
# return A

# Setting up the Graph class



# Search Function

# Kruskal's algorithm in Python

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])