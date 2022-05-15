# Daily Challenge 15-05-2022
# https://leetcode.com/problems/deepest-leaves-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        di = {}
        sov = 0
        def traverse(bt, di, depth):
            if bt == None:
                return None
            else:
                depth +=1
                for d in di:
                    if d == depth:
                        di[depth] += bt.val
                        break
                    elif depth not in di:
                        di[depth] = bt.val
                        break
                    else:
                        continue
                traverse(bt.left, di, depth)
                traverse(bt.right, di, depth)
                depth-=1
        if root.left or root.right:
            di[0] = root.val
            traverse(root, di, -1)
            return di[max(di)]
        else:
            return root.val