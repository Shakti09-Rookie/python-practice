# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        main = [root]
        d = 1
        
        while main:
            tmp = []       
            for each in main:
                if not each.left and not each.right: return d
                if each.left: tmp.append(each.left) 
                if each.right: tmp.append(each.right) 
            d += 1
            main = tmp