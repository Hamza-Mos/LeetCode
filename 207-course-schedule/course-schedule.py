class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)

        for crs, pre in prerequisites:
            adjList[crs].append(pre)

        path = set()
        visit = set()

        res = []

        # returns True if cycle is detected
        # False otherwise
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

        for crs in range(numCourses):
            if dfs(crs):
                return False

        return True if len(res) == numCourses else False
        