# Daily Challenge 07-05-2022
# https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        minVal = nums[0]
        
        for i in range(1,len(nums)):
			# stack should be monotonic decreasing
            while stack and nums[i]>=stack[-1][0]:
                stack.pop()
            
            if stack and nums[i] > stack[-1][1]:
                return True 
            
            stack.append([nums[i],minVal])
			
			# get the minimum value before the current index value
            minVal = min(minVal,nums[i])
            
        return False