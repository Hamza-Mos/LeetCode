class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, n):
        while self.parent[n] != n:
            self.parent[n] = self.parent[self.parent[n]]
            n = self.parent[n]

        return n

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        # already connected
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
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)
        res = n

        for n1, n2 in edges:
            # already connected (so invalid tree)
            if uf.union(n1, n2):
                return False

            res -= 1

        return res == 1
        