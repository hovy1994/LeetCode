class Solution(object):
    def findDifferentBinaryString(self, nums):
        n = len(nums)
        # 칸토어의 대각선 증명
        # 대각선 값들을 반전시키면 유니크한 값이 나오게 됨.
        result = "".join("1" if nums[i][i] == "0" else "0" for i in range(n))
        return result


if __name__ == "__main__":
    solution = Solution()
    nums = ["01", "10"]
    result = solution.findDifferentBinaryString(nums)
    print("result: ", result)
