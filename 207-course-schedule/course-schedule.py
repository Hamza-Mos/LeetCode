class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}

        for i in range(numCourses):
            adjList[i] = []

        for crs, pre in prerequisites:
            adjList[crs].append(pre)

        coursesFinished = []
        visited = set()
        path = set()

        # returns True if there is a cycle, false if valid (no cycle)
        def dfs(crs):
            if crs in path:
                return True

            if crs in visited:
                return False

            path.add(crs)

            for prereq in adjList[crs]:
                if dfs(prereq):
                    return True

            # remove from current path and add to visited set
            path.remove(crs)
            visited.add(crs)

            # add to coursesFinished
            coursesFinished.append(crs)

        for crs in adjList:
            if dfs(crs):
                return False
        
        return True if len(coursesFinished) == numCourses else False