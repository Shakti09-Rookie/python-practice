# https://leetcode.com/problems/sum-of-left-leaves/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sum = 0
        if root==None:
            return 0

        if root.left and root.left.left==None and root.left.right==None:
            sum+=root.left.val
        else:
            sum+=self.sumOfLeftLeaves(root.left)

        if root.right:
            sum+=self.sumOfLeftLeaves(root.right)


        return sum