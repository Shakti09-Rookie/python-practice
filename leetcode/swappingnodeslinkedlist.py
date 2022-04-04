# daily challenge 04-04-2022
# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

# Definition for singly-linked list. below listnode class is only for refrence
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List, Optional
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        n = 0
        while temp is not None:
            n+=1
            temp = temp.next
        temp = head
        def end(temp, n, k):
            count = 1
            swapval = None
            swapval2 = None
            while temp is not None:
                if count == k and count == (n-k):
                    swapval = temp
                    swapval2 = temp
                elif count == k:
                    swapval = temp
                elif (count == (n-k)):
                    swapval2 = temp
                 
                count+=1
                temp = temp.next
            swapval.val, swapval2.val = swapval2.val, swapval.val
            
        if(n == 1):
            return head
        else:
            end(temp, n+1, k)
            
        return head
            
"""
[1,2,3,4,5]
2
[7,9,6,6,7,8,3,0,9,5]
5
[1]
1
[1,2,3]
2
"""