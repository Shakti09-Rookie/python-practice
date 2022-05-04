# Daily Challenge 04-05-2022
# https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        left , right = 0, len(nums) -1
        nums.sort()
        count = 0
        while (left<right):
            if nums[left]+nums[right] == k:
                count+=1
                left+=1
                right-=1
            elif nums[left]+nums[right] < k:
                left+=1
            else:
                right-=1
        return count