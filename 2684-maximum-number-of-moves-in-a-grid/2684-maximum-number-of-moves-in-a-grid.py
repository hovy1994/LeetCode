from collections import deque


class Solution(object):
    dx = [-1,0,1] 
    
    class Coordinate(object):
        def __init__(self, x, y, value, move):
            self.x = x
            self.y = y
            self.value = value
            self.move = move

    def findMaxMoves(self, grid, first_coordinate, row_len, col_len):
        deq = deque()
        deq.append(first_coordinate)
        result = 0
        while deq:
            cur = deq.pop()
            
            if cur.y+1>=col_len:
                continue
            
            for i in range(3):
                if cur.x+self.dx[i]<0 or cur.x+self.dx[i]>=row_len or cur.value>=grid[cur.x+self.dx[i]][cur.y+1]:
                    continue
                deq.append(self.Coordinate(cur.x+self.dx[i], cur.y+1, grid[cur.x+self.dx[i]][ cur.y+1], cur.move+1))
                result = max(result, cur.move+1)
                
        return result
    
    
    def maxMoves(self, grid):
        row_len = len(grid)
        col_len = len(grid[0])
        deq = deque()
        for i in range(row_len):
            deq.append(self.Coordinate(i,0,grid[i][0],0))    
        
        result = 0
        while deq:
            cur = deq.pop()
            
            if cur.y+1>=col_len:
                continue
            
            for i in range(3):
                if cur.x+self.dx[i]<0 or cur.x+self.dx[i]>=row_len or cur.value>=grid[cur.x+self.dx[i]][cur.y+1]:
                    continue
                deq.append(self.Coordinate(cur.x+self.dx[i], cur.y+1, grid[cur.x+self.dx[i]][ cur.y+1], cur.move+1))
                result = max(result, cur.move+1)
                
        return result