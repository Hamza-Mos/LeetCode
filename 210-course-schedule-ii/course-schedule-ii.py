class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {}

        for i in range(numCourses):
            adjList[i] = []

        for crs, pre in prerequisites:
            adjList[crs].append(pre)

        res = []
        visited = set()
        path = set()

        # True if cycle
        # False otherwise
        def dfs(course):
            if course in path:
                return True

            if course in visited:
                return False

            path.add(course)

            for reqs in adjList[course]:
                if dfs(reqs):
                    return True

            path.remove(course)
            visited.add(course)
            res.append(course)

            return False

        for crs in adjList:
            if dfs(crs):
                return []

        return res if len(res) == numCourses else []