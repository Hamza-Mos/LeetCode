class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = { i: [] for i in range(numCourses) }

        for crs, pre in prerequisites:
            adjList[crs].append(pre)

        path = set()
        visited = set()
        res = []

        # returns True for cycle
        def dfs(crs):
            if crs in path:
                return True

            if crs in visited:
                return False

            path.add(crs)

            for pre in adjList[crs]:
                if dfs(pre):
                    return True

            path.remove(crs)
            visited.add(crs)
            res.append(crs)

            return False

        for i in range(numCourses):
            if dfs(i):
                return []

        return res if len(res) == numCourses else []
        