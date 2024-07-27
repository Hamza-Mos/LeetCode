class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)

        for src, dest, weight in times:
            adjList[src].append([dest, weight])

        visited = set()
        minHeap = [[0, k]] # weight, node

        while minHeap:
            weight, node = heapq.heappop(minHeap)

            if node in visited:
                continue

            visited.add(node)

            if len(visited) == n:
                return weight

            for nextNode, nextWeight in adjList[node]:
                if nextNode in visited:
                    continue

                heapq.heappush(minHeap, [weight + nextWeight, nextNode])

        return -1

        