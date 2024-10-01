from collections import defaultdict


class Solution(object):
    def maxPossibleString(self, str_list, k):
        l = 0
        r = 1
        mid_count = 0
        result = str_list[0][1]+k
        
        while r<len(str_list):
            distance = str_list[r][0]-str_list[r][1]-str_list[l][0]-mid_count
            if mid_count>0:
                distance+=str_list[l][1]-1
                
            if distance<=k:
                result = max(result, str_list[r][0]-str_list[l][0]+str_list[l][1]+(k-distance))
                mid_count+=str_list[r][1]
                r+=1
            else:
                mid_count-=str_list[l][1]
                l+=1
            
            if l>=r:
                mid_count=0
                result = max(result, str_list[r][1]+k)
                r=l+1
            
        return result
        
    def characterReplacement(self, s, k):
        char_dict = defaultdict(list)
        pos = 0
        while pos<len(s):
            cur_str = s[pos]
            next_idx = pos+1
            while next_idx < len(s):
                if cur_str != s[next_idx]:
                    break
                next_idx+=1
    
            char_dict[cur_str].append([next_idx-1, next_idx-pos]) # [마지막 index, 연속된 개수]
            pos=next_idx
            
        result =1
        for key in char_dict:
            result = max(result, self.maxPossibleString(char_dict[key],k))
        
        return min(len(s), result)