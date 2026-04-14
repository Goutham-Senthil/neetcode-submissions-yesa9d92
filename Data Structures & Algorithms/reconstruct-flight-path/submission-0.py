from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = defaultdict(list)
        tickets.sort()
        for frm,to in tickets:
            graph[frm].append(to)
            
        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets)+1:
                return True
            if src not in graph:
                return False
            
            neighbors = list(graph[src])
            
            for i,nei in enumerate(neighbors):
                graph[src].pop(i)
                res.append(nei)
                
                if dfs(nei):
                    return True
                
                graph[src].insert(i,nei)
                res.pop()
            return False
        
        dfs("JFK")
                
        return res
            
        
        