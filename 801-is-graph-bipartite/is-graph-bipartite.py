class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        numNodes = len(graph)
        partitions = [0] * numNodes

        # returns True if current graph/disjoint set is bipartite
        # False otherwise
        def dfs(node, groupVal):
            if partitions[node]:
                return True

            partitions[node] = groupVal

            for neighbour in graph[node]:
                # same group - cannot be bipartite
                if partitions[neighbour] == partitions[node]:
                    return False

                # graph is not bipartite
                if not dfs(neighbour, groupVal * -1):
                    return False

            return True

        for node in range(numNodes):
            if not dfs(node, 1):
                return False

        return True