class Solution(object):
    def minimumMountainRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsLen = len(nums)
        increaseNums = [0 for _ in range(numsLen)]
        reversedIncreaseNums = [0 for _ in range(numsLen)]
        maxTop = 0
        for i in range(numsLen):
            increaseNums[i]=1
            
            for k in range(i):
                if nums[k]<nums[i]:
                    increaseNums[i]= max(increaseNums[i], increaseNums[k]+1)


        for i in range(numsLen-1, -1, -1):
            reversedIncreaseNums[i]=1
            for k in range(numsLen-1, i,-1):
                if nums[k]<nums[i]:
                    reversedIncreaseNums[i]= max(reversedIncreaseNums[i], reversedIncreaseNums[k]+1)
            
            if increaseNums[i]>=2 and reversedIncreaseNums[i]>=2:
                maxTop = max(maxTop, increaseNums[i]+reversedIncreaseNums[i])
        
        return numsLen-maxTop+1