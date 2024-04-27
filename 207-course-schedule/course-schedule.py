class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #build adjacency list
        adjList = {}
        for course, pre in prerequisites:
            if course not in adjList:
                adjList[course] = []
            if pre not in adjList:
                adjList[pre] = []
            adjList[course].append(pre)
        
        visited = set()
        path = set()

        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True
            
            path.add(course)
            
            for prereq in adjList[course]:
                if not dfs(prereq):
                    return False
            
            path.remove(course)
            visited.add(course)
            return True

        for course, pre in prerequisites:
            if not dfs(course):
                return False
        return True

