class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        visitSet = set()

        #build an adjacency list
        for course, prereq in prerequisites:
            if course not in adjList:
                adjList[course] = []
            if prereq not in adjList:
                adjList[prereq] = []
            adjList[course].append(prereq)
        
        #define our dfs function 
        def dfs(course):

            #if our course is in our set, we have a cycle
            if course in visitSet:
                return False

            #if our course prereq's list is empty we can complete this course
            if len(adjList[course]) == 0:
                return True
            
            visitSet.add(course)

            for prereqs in adjList[course]:
                if not dfs(prereqs):
                    return False

            #we have explored this courses is preqreq's and are no longer visiting this course
            visitSet.remove(course)
            #we can confirm this course and all its preqreq's can be completed.
            adjList[course] = []

            #we can return true from this course
            return True
        
        for course, pre in prerequisites:
            if not dfs(course):
                return False
        return True
                



        

