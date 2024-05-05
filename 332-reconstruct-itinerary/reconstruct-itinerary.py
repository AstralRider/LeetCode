class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        adjList = {}

        res = []

        for src, dest in tickets:
            if src not in adjList:
                adjList[src] = []
            adjList[src].append(dest)
        
        for key in adjList.keys():
            adjList[key].sort(reverse=True)
        
        #Eulerian Path/Circuit algorithm (Hierholzer's algorithm) 
        #https://www.youtube.com/watch?v=8MpoO2zA2l4&t=658s&ab_channel=WilliamFiset
        #Basic overview of the algo is to dfs every vertex on the way down
        #When we encounter a vertex with no edges, we have found the end
        #We pop back up the recursive stack to check the edges of other vertices.
        #we continue doing this until we have visited every edge
        def dfs(src):
            if src in adjList:
                temp = adjList[src][:]
                while temp and adjList[src]:
                    #remove edge
                    val = adjList[src].pop()
                    dfs(val)
            print(res)
            res.append(src)
        dfs("JFK")

        return res[::-1]
#Time:
#O(E) for Hierholzer's algorithm + O(E*logE) for sorting every edge

#Space
#O(V + E) for the adjacency list
        
            
        
       


        
