from heapq import heappop, heappush

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # find distance from each point to every other point
        # prim's algo
        
        adjList = defaultdict(list)

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)

                adjList[i].append([j, dist])
                adjList[j].append([i, dist])


        # start at point 0
        visited = set()
        minHeap = [[0, 0, 0]] # dist, src, dest
        res = 0

        while len(visited) < len(points):
            dist, src, dest = heappop(minHeap)

            if dest in visited:
                continue

            visited.add(dest)

            res += dist

            for nextPoint, nextDist in adjList[dest]:
                if nextPoint in visited:
                    continue

                heappush(minHeap, [nextDist, dest, nextPoint])

        return res