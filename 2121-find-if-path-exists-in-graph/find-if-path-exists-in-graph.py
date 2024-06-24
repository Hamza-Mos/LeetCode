class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjList = { i: [] for i in range(n)}

        for u, v in edges:
            adjList[v].append(u)
            adjList[u].append(v)

        visited = set()

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for nextNode in adjList[node]:
                dfs(nextNode)

        dfs(source)

        return destination in visited
        