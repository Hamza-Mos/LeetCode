class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)

        adjList = defaultdict(list)
        for src, dest in tickets:
            adjList[src].append(dest)

        result = []

        def dfs(src):
            while adjList[src]:
                nextDest = adjList[src].pop()
                dfs(nextDest)

            result.append(src)


        dfs("JFK")

        return result[::-1]
        