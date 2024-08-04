class Solution(object):

    MOD = 10**9 + 7

    def rangeSum(self, nums, n, left, right):
        subarray = []

        for i in range(n):
            total = 0
            for j in range(i, n):
                total = (total + nums[j]) % self.MOD
                subarray.append(total)

        subarray.sort()
        
        subsum = [0]
        curSum = 0
        for num in subarray:
            curSum = (curSum + num) % self.MOD
            subsum.append(curSum)

        return subsum[right] - subsum[left - 1]