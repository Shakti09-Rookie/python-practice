# https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        c2 = 0
        temp = head
        if temp.next is None:
            return head
        while temp:
            count+=1
            temp = temp.next
        
        temp = head
        if count%2 == 0:
            a = count//2
            while temp:
                c2+=1
                if c2 == a:
                    temp = temp.next
                    return temp
                temp = temp.next
            pass
        else:
            a = count//2 + 1
            while temp:
                c2+=1
                if c2 == a:
                    return temp
                temp = temp.next