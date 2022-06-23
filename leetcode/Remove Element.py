# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if nums==0:
            return
        nl = []
        for i in range(len(nums)):
            if nums[i] != val:
                nl.append(nums[i])
                
        ans = len(nl)     
        for i in range(ans):
            nums[i] = nl[i]
        
        return ans