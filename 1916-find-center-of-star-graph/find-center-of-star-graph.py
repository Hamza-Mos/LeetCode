class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # center has most adjacent nodes?

        adjList = defaultdict(list)

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        maxLen = 0
        star = 0

        for node in adjList:
            if len(adjList[node]) > maxLen:
                star = node
                maxLen = len(adjList[node])

        return star
        