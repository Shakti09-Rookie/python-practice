# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def swap(ll):
            if not ll:
                return None
            
            # move pointer to the 3rd node
            preserve_next = ll.next and ll.next.next
            new_head = ll
            
            # swap the pairs
            if ll.next:
                new_head = ll.next
                new_head.next = ll
                ll.next = swap(preserve_next)
            
            return new_head

        return swap(head)