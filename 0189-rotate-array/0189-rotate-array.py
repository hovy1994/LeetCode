class Solution(object):
    def rotate(self, nums, k):
        numLen = len(nums)
        idx = numLen - (k%numLen)
        nums[:] = nums[idx:] + nums[:idx]