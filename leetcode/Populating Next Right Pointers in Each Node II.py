# Daily Challenge 13-05-200
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        curr, depth = root, 0
        queue = [[curr, depth]]
        while queue:
            curr, depth = queue.pop(0)
            if curr:
                if queue and depth == queue[0][1]:
                    curr.next = queue[0][0]
                if curr.left:
                    queue.append([curr.left, depth+1])
                if curr.right:
                    queue.append([curr.right, depth+1])
        return root