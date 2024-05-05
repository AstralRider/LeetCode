class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adjList = {}

        #{1:[0], 0:[1]}

        visited = set()
        res = []
        for i in range(numCourses):
            adjList[i] = []

        for src, pre in prerequisites:
            adjList[src].append(pre)
        
        def dfs(course):
            if course in visited:
                return False
            if course in res:
                return True
            
            visited.add(course)

            for pre in adjList[course]:
                if not dfs(pre):
                    return False

            visited.remove(course)
            res.append(course)
            return True
        
        for course, pre in prerequisites:
            if not dfs(course):
                return False
        return True

