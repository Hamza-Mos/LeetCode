class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)

        for crs, pre in prerequisites:
            adjList[crs].append(pre)

        visit = set()
        path = set()
        res = []

        # returns True for cycle
        # False if valid
        def dfs(crs):
            if crs in path:
                return True

            if crs in visit:
                return False

            path.add(crs)

            for pre in adjList[crs]:
                if dfs(pre):
                    return True

            path.remove(crs)
            visit.add(crs)

            res.append(crs)

            return False

        for i in range(numCourses):
            if dfs(i):
                return []

        return res if len(res) == numCourses else []
        