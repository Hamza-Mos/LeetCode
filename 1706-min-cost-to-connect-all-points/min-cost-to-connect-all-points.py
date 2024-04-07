class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res = 0
        adjList = collections.defaultdict(list)
        N = len(points)

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]

                dist = abs(x2 - x1) + abs(y2 - y1)

                # append (destination point, distance to that point)
                adjList[i].append([j, dist])
                adjList[j].append([i, dist])

        # min heap will contain distances to neighbouring points ([dist, src point, dest point])
        # initialize min heap to start at points[0]
        minHeap = [[0, 0, 0]]

        # set to keep track of all visited nodes
        visited = set()

        while len(visited) < N:
            dist, src, dest = heapq.heappop(minHeap)

            if dest in visited:
                continue

            visited.add(dest)
            
            res += dist

            # loop over all neighbouring points from destination point
            for nextPoint, nextDist in adjList[dest]:
                # if point is already visited
                if nextPoint in visited:
                    continue

                heapq.heappush(minHeap, [nextDist, dest, nextPoint])


        return res

        