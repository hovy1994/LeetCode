from collections import defaultdict


class Solution(object):     
    def removeStones(self, stones):
        def dfs(x, y):
            visited.add((x, y))
            
            for dx, dy in rows[x]:
                if (dx,dy) not in visited:
                    dfs(dx, dy)
            
            for dx, dy in cols[y]:
                if (dx,dy) not in visited:
                    dfs(dx, dy)
            
            
        rows = defaultdict(list)
        cols = defaultdict(list)
        for stone in stones:
            rows[stone[0]].append(stone)
            cols[stone[1]].append(stone)
            
        treeCount = 0
        
        visited = set()
        for x, y in stones:
            if (x,y) not in visited:
                treeCount+=1  
            dfs(x, y)
            
        return len(stones)-treeCount