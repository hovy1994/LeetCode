class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        prefixSet = set()
        result = 0
        for num in arr1:
            prefixSet.add(num)
            while num>0:
                num = int(num/10)
                prefixSet.add(num)
                
        sortedArr = sorted(arr2, reverse=True)
        for num in sortedArr:
            if num in prefixSet:
                if result > len(str(num)):
                    return result
                else:
                    result = len(str(num))
            while num>0:
                num = int(num/10)
                if num in prefixSet and num>0:
                    result = max(result, len(str(num)))
                    break
                
        return result
                        
        
        
if __name__=="__main__":
    solution = Solution()
    arr1 = [5]
    arr2 = [32,22]
    result = solution.longestCommonPrefix(arr1, arr2)
    print(result)