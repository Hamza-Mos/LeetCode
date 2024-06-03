class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, node):
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]

        return node

    # true for cycle
    def union(self, node1, node2):
        p1, p2 = self.find(node1), self.find(node2)

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
        # both requirements must be satisfied for it to be a valid tree:
        # 1) one single connected component
        # 2) no cycles

        uf = UnionFind(n)
        numComponents = n

        for node1, node2 in edges:
            if uf.union(node1, node2):
                return False

            numComponents -= 1

        return numComponents == 1
        