class Solution(object):

    def numOfSubarrays(self, arr):
        MOD = 10**9 + 7
        even_count = 1
        odd_count = 0
        result = 0
        cur_sum = 0

        for num in arr:
            cur_sum += num
            if cur_sum % 2 == 1:
                result += even_count
                odd_count += 1
            else:
                result += odd_count
                even_count += 1

        result %= MOD
        return result