class Solution(object):
    def __init__(self):
        self.result = 0
        
        
    def splitString(self, s, pos, curS, str_map):
        if pos >= len(s):
            if curS=="":
                return len(str_map)
            else:
                return 0
        
        curS+=s[pos]
        if curS not in str_map:
            self.result = max(self.result, self.splitString(s, pos+1, curS, str_map))
            str_map.add(curS) 
            self.result = max(self.result, self.splitString(s, pos+1, "", str_map))
            str_map.remove(curS)
            return self.result
        else:
            return self.splitString(s, pos+1, curS, str_map)
            
            
        
    
    def maxUniqueSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.splitString(s, 0, "", set())
        return self.result