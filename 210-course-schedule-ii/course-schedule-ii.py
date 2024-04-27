class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []

        #build adjList
        adjList = {}

        #set for tracking courses
        visited = set()
        path = set()

        #build adj list for range of courses first
        #edge case where we have n courses and 0 prereq's
        for course in range(numCourses):
            adjList[course] = []

        for course, prereq in prerequisites:
            if prereq not in adjList:
                adjList[prereq] = []
            adjList[course].append(prereq)
        
        
        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True

            path.add(course)

            for prereqs in adjList[course]:
                if not dfs(prereqs):
                    return False

            path.remove(course)
            visited.add(course)
            res.append(course)

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return res 