class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = {i: [] for i in range(numCourses)}

        for pre, crs in prerequisites:
            adjList[crs].append(pre)

        # no cycles - this graph is always valid
        prereqList = {i: set() for i in range(numCourses)}
        visited = set()

        def dfs(crs):
            if crs in visited:
                return

            for pre in adjList[crs]:
                dfs(pre)
                prereqList[crs].update(prereqList[pre])
                prereqList[crs].add(pre)

            visited.add(crs)

        for i in range(numCourses):
            dfs(i)

        print(prereqList)

        res = []
        for pre, crs in queries:
            if pre in prereqList[crs]:
                res.append(True)

            else:
                res.append(False)

        return res
        