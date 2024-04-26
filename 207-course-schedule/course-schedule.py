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
        
        #create a set to detect cycles
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            #we have already checked this course and it can be completed
            if len(adjList[course]) == 0:
                return True
            
            #add course to set of courses we are currently checking
            visited.add(course)
            
            #check if all the prerequisite courses can be completed
            for prereq in adjList[course]:
                if not dfs(prereq):
                    return False
            
            #remove course from the set since we have finished checking it can be done
            visited.remove(course)
            #set the course prerequisites to empty since we know this course can be completed
            adjList[course] = []
            return True
        
        #run the dfs for every edge since it is possible we have a disconnected graph
        #e.g 0 -> 1, 2 -> 3
        for course, pre in prerequisites:
            if not dfs(course):
                return False
        return True

