class Solution(object):
    def findDifferentBinaryString(self, nums):
        n = len(nums)
        result = "".join("1" if nums[i][i] == "0" else "0" for i in range(n))
        return result