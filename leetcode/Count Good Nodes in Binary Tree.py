# Daily Challenge 01-09-2022
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxx = float("-inf")
        op = []
        
        def dfs(root, maxx):
            if not root: return
            if root.val >= maxx:
                maxx = root.val
                op.append(root.val)
            
            dfs(root.left, maxx)
            dfs(root.right, maxx)
        dfs(root, maxx)
        return len(op)