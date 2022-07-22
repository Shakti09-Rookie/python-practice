# https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        current = head
        prev = None
        
        while current is not None:
            if current.val != val:
                prev = current
            else:
                if current == head:
                    head = current.next
                else:
                    prev.next = current.next
            current = current.next
            
        return head