class Node(object):
    def __init__(self):
        self.childs = [None for _ in range(10)]
    
    
class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        result = 0
        rootNodes = [None for _ in range(10)]
        
        for num in arr1:
            numstr = str(num)
            if rootNodes[int(numstr[0])]==None:
                rootNodes[int(numstr[0])] = Node()
            curNode = rootNodes[int(numstr[0])]
            for i in range(1, len(numstr)):
                next = int(numstr[i])
                if curNode.childs[next]==None:
                    curNode.childs[next] = Node()
                curNode = curNode.childs[next]
            
        for num in arr2:
            count = 1
            numstr = str(num)
            if rootNodes[int(numstr[0])]==None:
                continue
            curNode = rootNodes[int(numstr[0])]
            for i in range(1, len(numstr)):
                next = int(numstr[i])
                if curNode.childs[next]:
                    curNode = curNode.childs[next]
                    count+=1
                    result = max(result, count)
                else:
                    result = max(result, count)
                    break
        return result