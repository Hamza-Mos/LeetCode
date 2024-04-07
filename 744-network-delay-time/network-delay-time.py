class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = collections.defaultdict(list)

        for src, dest, time in times:
            adjList[src].append([dest, time])

        # min heap will contain elements in the form of [time, src, dest]
        minHeap = [[0, k, k]]
        res = 0

        visited = set()

        while minHeap:
            currTime, src, dest = heapq.heappop(minHeap)

            if dest in visited:
                continue

            visited.add(dest)

            # the signal has reached all nodes
            if n == len(visited):
                return currTime

            for nextDest, time in adjList[dest]:
                if nextDest in visited:
                    continue

                heapq.heappush(minHeap, [currTime + time, dest, nextDest])

        return -1

        


        