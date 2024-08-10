class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        # edge cases
        if n <= 2:
            return [i for i in range(n)]

        adjList = [set() for i in range(n)]
        for u, v in edges:
            adjList[u].add(v)
            adjList[v].add(u)

        leaves = []
        for i in range(n):
            if len(adjList[i]) == 1:
                leaves.append(i)

        remainingNodes = n
        while remainingNodes > 2:
            remainingNodes -= len(leaves)
            newLeaves = []

            while leaves:
                leaf = leaves.pop()

                neighbor = adjList[leaf].pop()

                adjList[neighbor].remove(leaf)
                if len(adjList[neighbor]) == 1:
                    newLeaves.append(neighbor)

            leaves = newLeaves


        return leaves