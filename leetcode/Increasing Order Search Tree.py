# Daily Challenge 17-04-2022
# https://leetcode.com/problems/increasing-order-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def ibst(node):
            if not node:
                return None
            ibst(node.left)
            ans.append(node.val)
            ibst(node.right)
         
        obj1 = newn = TreeNode(None)
        ans = []
        ibst(root)
        for val in ans:
            newn.right = TreeNode(val)
            newn=newn.right
        return obj1.right