# Daily Challenge 19-04-2022
# https://leetcode.com/problems/recover-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.temp = []
        def Inorder(node):
            if node:
                Inorder(node.left)
                self.temp.append(node)
                Inorder(node.right)
            return
        Inorder(root)
        srt = sorted(n.val for n in self.temp)
        for i in range(len(srt)):
            self.temp[i].val = srt[i]

# Preferred way
# https://leetcode.com/problems/recover-binary-search-tree/discuss/1962833/Beginner-Level-Illustration-and-11-line-Solution