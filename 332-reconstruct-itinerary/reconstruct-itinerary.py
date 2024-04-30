class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # sort tickets in reverse order since we are popping from back of adjacency list
        tickets.sort(reverse=True)

        adjList = defaultdict(list)

        for src, dest in tickets:
            adjList[src].append(dest)

        res = []

        def dfs(source):

            while adjList[source]:
                nextDest = adjList[source].pop()
                dfs(nextDest)

            res.append(source)

        dfs("JFK")

        return res[::-1]
        