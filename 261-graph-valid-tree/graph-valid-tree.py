class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, node):
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]] # path compression
            node = self.parent[node]

        return node

    # True if redundant connection
    # False otherwise
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return True

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]

        else:
            self.parent[p1] = p2
            self.rank[p2] += p1

        return False

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 2 criteria
        # 1) no redundant connections
        # 2) 1 connected component

        uf = UnionFind(n)
        numComponents = n

        for node1, node2 in edges:
            if uf.union(node1, node2):
                return False

            numComponents -= 1

        return numComponents == 1

        