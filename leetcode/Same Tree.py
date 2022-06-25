# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def checksame(p,q):
            if p is None and q is None:
                return True
            
            if p is None or q is None or p.val != q.val:
                return False
            
            left = checksame(p.left, q.left)
            right = checksame(p.right, q.right)
            
            return left and right
        
        return checksame(p,q)