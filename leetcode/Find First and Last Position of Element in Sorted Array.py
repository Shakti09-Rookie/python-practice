# Daily Challenge 25-07-2022
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = -1
        last = -1
        
        i = 0
        
        while i < len(nums):
            if nums[i] == target:
                first = i
                break
            i += 1
        
        j = i
        while j < len(nums) and nums[j] == target:
            last = j
            j += 1
            
            
        return [first, last]