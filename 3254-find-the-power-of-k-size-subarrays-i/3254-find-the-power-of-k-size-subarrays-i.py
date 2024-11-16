class Solution(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        incCount = 0
        pre = -1 
        answer = []
        for i in range(len(nums)):
            if pre+1==nums[i]:
                incCount = incCount+1
            else:
                incCount=1
                    
            if i>=k-1:
                if incCount>=k:
                    answer.append(nums[i])
                else:
                    answer.append(-1)
        
            pre = nums[i]
            
        return answer