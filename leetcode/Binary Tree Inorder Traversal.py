# Daily Challenge 08-09-2022
# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        li = []
        if not root:
            return
        def trav(node):
            if node:
                trav(node.left)
                li.append(node.val)
                trav(node.right)
            else:
                return
        
        trav(root)
        return li