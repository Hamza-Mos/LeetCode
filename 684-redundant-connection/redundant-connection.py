class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, n):
        while self.parent[n] != n:
            self.parent[n] = self.parent[self.parent[n]]
            n = self.parent[n]

        return n

    # returns true if already connected
    # false otherwise
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        # belong to same component
        if p1 == p2:
            return True

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]

        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]

        return False

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n + 1) # because nodes are from 1 to n (not 0 to n - 1)

        redundantEdge = [-1, -1]

        for n1, n2 in edges:
            # already connected (returns true) then this means that this connection is redundant
            if uf.union(n1, n2):
                redundantEdge = [n1, n2]

        return redundantEdge
        