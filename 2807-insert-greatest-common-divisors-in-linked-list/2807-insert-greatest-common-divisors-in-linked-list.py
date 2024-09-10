# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
        
    def gcd(self, a, b):
        while b:
            a, b = b, a%b
        return a
            
            
    def insertGreatestCommonDivisors(self, head):
        leftNode = head
        curNode = head.next
        
        while curNode:
            gcd = self.gcd(leftNode.val, curNode.val)
            leftNode.next = ListNode(gcd, curNode)
            leftNode = curNode
            curNode = curNode.next
            
        return head
        