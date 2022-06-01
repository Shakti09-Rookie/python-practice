# Daily Challenge 01-06-2022
# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = [nums[0]]
        for i in range(1, len(nums)):
            output.append(nums[i]+output[-1])
        
        return output