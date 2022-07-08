# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        li = []
        if not root:
            return
        def trav(node):
            if node:
                trav(node.left)
                trav(node.right)
                li.append(node.val)
            else:
                return
        
        trav(root)
        return li