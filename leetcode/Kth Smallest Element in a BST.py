# Daily Challenge 18-04-2022
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        return self.inorder(root)
    
    def inorder(self,root):
        if not root:
            return 0
        element = self.inorder(root.left)
        if element:
            return element
        self.k-=1
        if self.k == 0:
            return root.val
        return self.inorder(root.right)