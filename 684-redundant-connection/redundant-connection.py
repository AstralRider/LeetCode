class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        
        #no. of nodes = no. of edges
        for node in range(1, n+1):
            self.parent[node] = node
            self.rank[node] = 0
        
    def find(self, node):
        p = self.parent[node]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
    
    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)

        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1
        return True
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = UnionFind(len(edges))

        for node, edge in edges:
            if not dsu.union(node, edge):
                return [node, edge]
        