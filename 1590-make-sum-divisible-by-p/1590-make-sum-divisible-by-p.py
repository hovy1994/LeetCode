class Solution(object):

    def minSubarray(self, nums, p):
        nums_len = len(nums)
        total_sum = sum(nums)
        
        result = nums_len
        remainder_set = {0: -1}
        
        remainder = sum(nums)%p
        if remainder==0:
            return 0
        
        if total_sum <= p:
            return -1
        
        cur_sum =0
        for i in range(nums_len):
            cur_sum+=nums[i]
            cur_remainder = cur_sum%p
            target = (cur_remainder-remainder)%p
            if target in remainder_set:
                result = min(result, i-remainder_set[target])
            
            remainder_set[cur_remainder]=i              
    
        if result >= nums_len:
            return -1
        
        return result