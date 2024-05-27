class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # we will use dfs
        # basically we will introduce "artificial" edges to make each edge/connection between
        # nodes undirected so that we can travel from node 0 to all nodes in any case

        # the artificial edges will have a value of 0 (will not affect our result), but the 
        # original edges will have a value of 1

        # for each dfs call, we only want to check if there is a path between the neighbor and the parent
        # if the current neighbor is not a parent, then we would want to reverse that connection if the edge
        # is original (value 1), otherwise result/count is unaffected if edge is artificial (value 0)

        # if the neighbor is equal to the parent, then we will not call dfs again to avoid getting stuck in a cycle

        self.count = 0
        adjList = collections.defaultdict(list)

        for node1, node2 in connections:
            # original
            adjList[node1].append((node2, 1))

            # artificial
            adjList[node2].append((node1, 0))

        def dfs(currNode, parentNode):
            for neighbor, value in adjList[currNode]:
                if neighbor != parentNode:
                    self.count += value

                    dfs(neighbor, currNode)

        dfs(0, -1)

        return self.count
        