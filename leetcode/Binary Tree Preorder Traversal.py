# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes = [] # arr to store nodes
        def helper(root, arr): 
            if root: # if there is root traverse
                arr.append(root.val)
                helper(root.left,arr)
                helper(root.right,arr)
        
        helper(root,nodes)

        return nodes