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

        def dfs(src):
            if src in adjList:
                temp = adjList[src][:]
                while temp and adjList[src]:
                    val = adjList[src].pop()
                    dfs(val)
            #an airport has no outgoing flights
            res.append(src)
        dfs("JFK")
        return res[::-1]

        
            
        
       


        
