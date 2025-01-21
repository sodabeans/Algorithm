# Codes based off https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append(([u, v, w]))

    def find(self, parent, i):
        # recursively find parent of input i and reassign the parent
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, i, j):
        # find connect trees according to rank, by setting parent of one as the other
        if rank[i] < rank[j]:
            parent[i] = j
        elif rank[j] < rank[i]:
            parent[j] = i
        else:
            parent[j] = i
            rank[i] += 1

    def KruskalMST(self):
        minimum_cost = 0 # answer of this problem
        # mst = [] # final minimum spanning tree
        mst_size = 0
        idx = 0 # index keeping track of edge

        # sort each edge based on weight
        self.graph = sorted(self.graph, key=lambda x: x[2])

        parent = [i for i in range(self.V + 1)] # track parent of each node
        rank = [0] * (self.V + 1) # track the rank of each node

        while mst_size < self.V:
            n1, n2, w = self.graph[idx]
            idx += 1
            x = self.find(parent, n1)
            y = self.find(parent, n2)

            if x != y:
                # mst.append([n1, n2, w])
                mst_size += 1
                self.union(parent, rank, x, y)
                minimum_cost += w
        return minimum_cost


T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    g = Graph(V)

    for _ in range(E):
        n1, n2, w = map(int, input().split())
        g.addEdge(n1, n2, w)

    answer = g.KruskalMST()

    print(f"#{test_case} {answer}")
