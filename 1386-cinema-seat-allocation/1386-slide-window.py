class Solution:
    MOD = 10**9 + 7

    def indexOfTarget(
        self, nums, n, target
    ):  # target 값이 몇 번째 subsum의 몇 번째 인덱스에 위치해 있는가?
        curSum = position = 0
        i = 0
        for j in range(n):
            curSum += nums[j]
            while target < curSum:
                curSum -= nums[i]
                i += 1
            position += j - i + 1
        return position

    def fSumOfK(
        self, nums, n, target
    ):  # subsum array에서 target보다 작거나 같은 (subsum의)element들의 합과 그 target의 위치 리턴
        # window: 현재 window에 들어있는 element들의 합
        currSum = window = total = position = 0
        i = 0
        for j in range(n):
            currSum += nums[j]
            window += nums[j] * (j - i + 1)  # nums[j]가 몇 번 더해졌는가
            while target < currSum:
                window -= currSum
                currSum -= nums[i]
                i += 1
            total += window
            position += j - i + 1
        return position, total % self.MOD

    def findSum(self, nums, n, k):
        right = sum(nums)
        left = min(nums)
        while left <= right:
            mid = (left + right) // 2
            if self.fSumOfK(nums, n, mid)[0] >= k:
                right = mid - 1
            else:
                left = mid + 1
        count, total = self.fSumOfK(nums, n, left)
        return (total - left * (count - k)) % self.MOD

    def rangeSum(self, nums, n, left, right):
        res = (
            self.findSum(nums, n, right) - self.findSum(nums, n, left - 1)
        ) % self.MOD
        return res


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4]
    n = 4
    left = 1
    right = 10
    answer = solution.rangeSum(nums, n, left, right)

    sumOfK = solution.indexOfTarget(nums, n, 10)
    print("sumOfK: ", sumOfK)
