class UnionFind:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]

    # returns the parent/representative node of the disjoint set that the input node is in
    def find(self, node):
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]] # path compression
            node = self.parent[node]

        return node

    # merges 2 disjoint groups/sets
    def union(self, node1, node2):
        par1, par2 = self.find(node1), self.find(node2)

        # they already belong to the same set
        if par1 == par2:
            return 0

        # union by rank
        if self.rank[par1] > self.rank[par2]:
            # par1 becomes the parent of par2
            self.parent[par2] = par1
            self.rank[par1] += self.rank[par2]

        else:
            # par2 becomes the parent of par1
            self.parent[par1] = par2
            self.rank[par2] += self.rank[par1]

        # groups have been merged
        return 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # initially no components are connected (n different components)
        res = n
        uf = UnionFind(n)

        # merge every pair in edges and decrement result by 1 after every successful merge
        # result is unchanged if the pair were already connected
        for node1, node2 in edges:
            res -= uf.union(node1, node2)

        return res
        