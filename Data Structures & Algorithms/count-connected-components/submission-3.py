class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1]*n

        def find(node):
            rep = node
            while rep!=parent[rep]:
                rep=parent[rep]
            return rep
        
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)

            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2]+=rank[p1]
            else:
                parent[p2] = p1
                rank[p1]+=rank[p2]
            
            return 1
        
        for u,v in edges:
            n-=union(u,v)
        
        return n