class Solution:
    MOD = 10**9 + 7
    
    def rangeSum(self, nums, n, left, right):
        subArrSum = []
        for i in range(n):
            sum_ = 0
            for j in range(i, n):
                sum_ += nums[j]
                subArrSum.append(sum_)
        subArrSum.sort()
        return sum(subArrSum[left - 1:right]) % self.MOD