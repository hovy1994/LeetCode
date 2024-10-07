class Solution(object):
    def canArrange(self, arr, k):
        dict = {}
        for num in arr:
            mod = num%k
            dict[mod] = dict.get(mod, 0)+1
            
        while dict:
            mod, count = dict.popitem()
            complement = (k-mod)%k
            
            if mod==complement:
                if count%2==0:
                    continue
                else:
                    return False
            if count==dict.get(complement,0):
                dict.pop(complement)
                continue
            else:
                return False
            
        return True