class Solution(object):
    seg = []
    
    def update(self, pos, val, node, x, y):
        if y<pos or pos<x:
            return self.seg[node]
        
        if x==y:
            self.seg[node] = [val, pos]
            return self.seg[node]
        
        mid = (x+y)>>1
        
        leftMax = self.update(pos, val, node*2, x, mid)
        rightMax = self.update(pos, val, node*2+1, mid+1, y)
        
        self.seg[node] = rightMax if leftMax[0] < rightMax[0] else leftMax
        
        return self.seg[node]
        
    def query(self, start, end, node, x, y):
        if y<start or end<x:
            return [-100000,0]
        
        if start<= x and y<=end:
            return self.seg[node]
        
        mid = (x+y)>>1
        
        leftMax = self.query(start, end, node*2, x, mid)
        rightMax = self.query(start, end, node*2+1, mid+1, y)
        
        return rightMax if leftMax[0]< rightMax[0] else leftMax
        
    def jump(self, nums):
        numLen = len(nums)
        if numLen == 1:
            return 0
        self.seg = [[0,0] for _ in range(numLen*4)]
        for i in range(numLen):
            self.update(i, nums[i]-(numLen-i), 1, 0, numLen-1)
            
        position = 0
        result=1
        while position < numLen-1:
            if position + nums[position]>= numLen-1:
                break
            position= self.query(position+1,position+nums[position], 1, 0, numLen-1)[1]
            result+=1
            
        return result