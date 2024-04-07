class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res = []
        adjList = collections.defaultdict(list)

        tickets.sort(reverse=True)

        for src, dest in tickets:
            adjList[src].append(dest)

        def dfs(origin):
            # we will be visiting all of the destinations from this origin in sorted order
            # so since we sorted the edges in reverse order, we will start from the end of the array 
            # then make our way to the front (popping the back each time - O(1) operation)

            destList = adjList[origin]

            # while the destination list is not empty
            while destList:
                nextDest = destList.pop()
                dfs(nextDest)

            # after visiting all destinations, we can finally add origin to our list
            res.append(origin)

        dfs("JFK")

        return res[::-1]

        