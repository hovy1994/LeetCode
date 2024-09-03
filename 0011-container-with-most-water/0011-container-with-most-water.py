class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height)-1
        result =0
        
        while l<r:
            if height[l]<height[r]:
                result = max(result, (r-l)*height[l])
                l+=1
            else:
                result = max(result, (r-l)*height[r])
                r-=1
                
        return result 