class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, n):
        while self.parent[n] != n:
            self.parent[n] = self.parent[self.parent[n]] # path compression
            n = self.parent[n]

        return n

    # returns 0 if already connected
    # returns 1 if not already connected and successfully merged
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return 0

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]

        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]

        return 1

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        res = n

        for i in range(n):
            for j in range(n):
                node1, node2 = i, j

                if isConnected[i][j]:
                    res -= uf.union(node1, node2)

        return res
        