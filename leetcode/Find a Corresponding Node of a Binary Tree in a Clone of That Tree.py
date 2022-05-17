# Daily Challenge 17-05-2022
# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def traverse(orig, bt):
            if not orig:
                return None
            elif orig == target:
                return bt
            
            return traverse(orig.left, bt.left) or traverse(orig.right, bt.right)
                
        return traverse(original, cloned)

    # the below solution works correctly also and passes all the test cases.
    # However, if the nodes are not cloned and you want to still find refrence, then below will not work,

    # def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    #     def traverse(bt):
    #         if not bt:
    #             return
    #         elif bt.val == target.val:
    #             return bt
            
    #         return traverse(bt.left) or traverse(bt.right)
                
    #     return traverse(cloned)