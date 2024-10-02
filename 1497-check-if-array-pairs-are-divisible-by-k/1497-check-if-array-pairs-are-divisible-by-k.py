class Solution(object):
    def canArrange(self, arr, k):
        dict = {}
        for num in arr:
            mod = num%k
            dict[mod] = dict.get(mod, 0)+1
            
        for key in dict:
            if dict[key]==0:
                continue
            complement = (k-key)%k
            
            if key==complement:
                if dict[key]%2==0:
                    dict[complement]=0
                    continue
                else:
                    return False
            if dict.get(key, 0)==dict.get(complement,0):
                dict[key]=0
                dict[complement]=0
                continue
            else:
                return False
        
        return True