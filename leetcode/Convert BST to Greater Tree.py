# Daily Challenge 16-04-2022
# https://leetcode.com/problems/convert-bst-to-greater-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def cbst(node, tot):
            if node is not None:
                node.val+= cbst(node.right, tot)
                return cbst(node.left, node.val)
            return tot
    
        cbst(root, 0)
        return root