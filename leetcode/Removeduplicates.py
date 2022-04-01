from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #head can be None(one if the cases)
        if head is None:
            return head
        temp = head
        nextval = temp.next
        preval = head
        while temp is not None and nextval is not None:
            if head.val == head.next.val:
                head = head.next
                temp = head
                nextval = temp.next
                preval = head
                print(head)
            elif temp.val == nextval.val:
                preval.next = nextval
                temp = temp.next
                nextval = temp.next
            else:
                print("entered here")
                preval = temp
                temp = temp.next
                nextval = nextval.next

        return head