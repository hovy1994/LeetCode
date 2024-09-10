class Solution(object):
    def countNode(self, head):
        count = 0
        while head:
            head = head.next
            count+=1
        return count
            
    def splitListToParts(self, head, k):
        result = []
        nodeLen = self.countNode(head)
        share, remainder = divmod(nodeLen, k)
        curNode = curHead = head
        for _ in range(k):
            repeat = share
            result.append(curHead)
            curNode = curHead
            if remainder>0:
                repeat +=1
                remainder-=1
            for _ in range(repeat-1):
                curNode = curNode.next
            
            if curNode:
                curHead = curNode.next
                curNode.next = None
            else:
                curHead = None
            
        return result