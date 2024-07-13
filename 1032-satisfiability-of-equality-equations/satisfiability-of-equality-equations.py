class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.notEqualTo = defaultdict(set)

    def addNode(self, n):
        if n not in self.parent and n not in self.rank:
            self.parent[n] = n
            self.rank[n] = 1

    def find(self, node):
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]

        return node

    def checkConnection(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return True

        return False

    def notEqual(self, n1, n2):
        self.notEqualTo[n1].add(n2)
        self.notEqualTo[n2].add(n1)

        p1, p2 = self.find(n1), self.find(n2)

        self.notEqualTo[p1].add(p2)
        self.notEqualTo[p2].add(p1)

    # return true for successful union
    # false for already connected
    def union(self, n1, n2):
        if n1 in self.notEqualTo[n2] or n2 in self.notEqualTo[n1]:
            return False

        p1, p2 = self.find(n1), self.find(n2)

        if p1 in self.notEqualTo[p2] or p2 in self.notEqualTo[p1]:
            return False

        if p1 == p2:
            return True

        if self.rank[p1] > self.rank[p2]:
            self.rank[p1] += self.rank[p2]
            self.parent[p2] = p1

        else:
            self.rank[p2] += self.rank[p1]
            self.parent[p1] = p2

        return True

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # union find?

        uf = UnionFind()

        for eq in equations:
            equal = eq[1] == "="
            uf.addNode(eq[0])
            uf.addNode(eq[3])

            if equal:
                uf.union(eq[0], eq[3])

        for eq in equations:
            equal = eq[1] == "="

            if not equal:
                if uf.checkConnection(eq[0], eq[3]):
                    return False

        print(uf.parent)
        print(uf.rank)

        return True
