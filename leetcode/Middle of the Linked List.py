# https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        
        mid_node = None
        total = 0
        
        def middle(node, count):
            
            if not node:
                nonlocal total
                total = count
                return
            
            middle(node.next, count+1)
            
            if count == total//2:
                nonlocal mid_node
                mid_node = node
            
        middle(head, 0)
        return mid_node