class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = {}
        path = set()

        for i in range(numCourses):
            adjList[i] = []
        
        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        
        def dfs(course):
            if course in path:
                return False
            
            if len(adjList[course]) == 0:
                return True
            
            path.add(course)

            for pre in adjList[course]:
                
                if not dfs(pre):
                    return False

            path.remove(course)
            adjList[course] = []
            
            return True

        for course, pre in prerequisites:
            if not dfs(course):
                return False
        return True
