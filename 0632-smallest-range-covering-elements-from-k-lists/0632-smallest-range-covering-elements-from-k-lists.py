class Solution(object):
    
    def getSmallerRange(self, range1, range2):
        if range1[1]-range1[0] < range2[1]-range2[0]:
            return range1
        elif range1[1]-range1[0]==range2[1]-range2[0]:
            if range1[0]<range2[0]:
                return range1

        return range2
    
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
       
        group_count = len(nums)
        num_list = []
        
        for i in range(group_count):
            for num in nums[i]:
                num_list.append([num, i])
        
        num_list.sort(key=lambda x: x[0])
        group_counter = {}
        result = [num_list[0][0], num_list[len(num_list)-1][0]]
        
        l=0
        for i in range(len(num_list)):
            group_num = num_list[i][1]
            group_counter[group_num] = group_counter.get(group_num, 0)+1
            if len(group_counter)==group_count:
                result = self.getSmallerRange(result, [num_list[l][0], num_list[i][0]])
                while l<i:
                    group_counter[num_list[l][1]]-=1
                    if group_counter[num_list[l][1]]==0:
                        group_counter.pop(num_list[l][1])
                        l+=1
                        break
                    l+=1
                    result = self.getSmallerRange(result, [num_list[l][0], num_list[i][0]])
                    
                    
        return result