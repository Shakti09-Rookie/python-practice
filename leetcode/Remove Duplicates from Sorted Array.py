# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nl = []
        stk = [nums[0]]
        length = len(nums)
        for i in range(length -1):
            if nums[i] != nums[i+1]:
                nl.append(stk[0])
                stk = []
                stk.append(nums[i+1])
        if stk[0] not in nl:
            nl.append(stk[0])
            
        for i in range(len(nl)):
            nums[i] = nl[i]
            
        return len(nl)