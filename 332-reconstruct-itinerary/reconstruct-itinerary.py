class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src: [] for src, dst in tickets}
        res = []

        for src, dst in tickets:
            adj[src].append(dst)

        for key in adj:
            adj[key].sort()

        def dfs(src):
            if src in adj:
                destinations = adj[src][:]
                while destinations:
                    dest = destinations[0]
                    adj[src].pop(0)
                    dfs(dest)
                    destinations = adj[src][:]
            res.append(src)

        dfs("JFK")
        res.reverse()

        return res

#Code works fine just not on leetcode due to TLE
# adjList = {}

#         res = ["JFK"]

#         tickets.sort()

#         for src, dest in tickets:
#             if src not in adjList:
#                 adjList[src] = []
#             if dest not in adjList:
#                 adjList[dest] = []
#             adjList[src].append(dest)

#         def dfs(src):
#             if len(res) == len(tickets) + 1:
#                 return True
            
#             if src not in adjList:
#                 return False
            
#             for i, v in enumerate(adjList[src]):
#                 if v == -1:
#                     continue
#                 adjList[src][i] = -1
#                 res.append(v)
#                 if dfs(v):
#                     return True
#                 adjList[src][i] = v
#                 res.pop()
#             return False
        
#         dfs("JFK")
#         return res