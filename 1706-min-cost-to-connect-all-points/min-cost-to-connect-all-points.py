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

            # if dest point has been visited then move onto next element in heap
            if dest in visited:
                continue

            # mark the dest point as visited
            visited.add(dest)

            res += dist

            # loop over all neighbouring points from destination point
            for nextPoint, nextDist in adjList[dest]:
                # if point is already visited then continue to next iteration of loop
                if nextPoint in visited:
                    continue

                # dest now becomes new src point, and we append the distance to next along with next point to heap
                heapq.heappush(minHeap, [nextDist, dest, nextPoint])


        return res

        