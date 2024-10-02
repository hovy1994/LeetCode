class Solution(object):
    def canArrange(self, arr, k):
        dict = {}
        for num in arr:
            mod = num%k
            dict[mod] = dict.get(mod, 0)+1
            
        for key in dict:
            complement = (k-key)%k
            repeat = dict[key]
            if key==complement:
                repeat = int(repeat/2)
            for _ in range(repeat):
                dict[key]-=1
                if dict.get(complement,0)>0:
                    dict[complement]-=1
                else:
                    return False
        
        return True