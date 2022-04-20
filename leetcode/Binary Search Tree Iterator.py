# Daily Challenge 20-04-2022
# https://leetcode.com/problems/binary-search-tree-iterator/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.inorder=[]
        while root:
            self.inorder.append(root)
            root= root.left
            
    def inorder(self, node):
        if root == None:
            return None
        self.inorder(root.left)
        self.inorder.append(root.val)
        self.inorder(root.right)
        
        
    def next(self) -> int:
        node = self.inorder.pop()
        value = node.val
        if node.right:
            node = node.right
            self.inorder.append(node)
            while node.left:
                node = node.left
                self.inorder.append(node)
        return value

    def hasNext(self) -> bool:
        return bool(self.inorder)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()