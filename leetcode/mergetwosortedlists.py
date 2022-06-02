# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        temp1 = list1
        temp2 = list2
        dummy = ListNode(-1)
        templ = dummy
        while temp1 and temp2:
            if temp1.val < temp2.val:
                templ.next = temp1
                temp1 = temp1.next
            else:
                templ.next = temp2
                temp2 = temp2.next
            templ = templ.next
            
        if temp1 is not None:
            templ.next = temp1
        else:
            templ.next = temp2
        return dummy.next