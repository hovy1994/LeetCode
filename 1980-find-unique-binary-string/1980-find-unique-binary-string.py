class Solution(object):
    def findDifferentBinaryString(self, nums):
        existNumbers = set()
        for num in nums:
            intNum = int(num, 2)
            existNumbers.add(intNum)

        for num in range(2 ** len(nums[0])):
            if num not in existNumbers:
                return bin(num)[2:].zfill(len(nums[0]))