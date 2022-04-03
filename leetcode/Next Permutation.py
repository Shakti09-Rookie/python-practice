#  daily challenge 04-04-2022
#  solution worked in local compiler not in leet code due to problem in modifying in in-place
#  accepted solution below

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lx = -1
        n = len(nums)
        for i in range(n-1):
            if nums[i] < nums[i+1]:
                lx = i
        if lx == -1:
            print("entering")
            # nums.sort()
            return sorted(nums)
        
        lj = -1
        for j in range(0,n):
            if(nums[lx]) < nums[j]:
                lj = j


        # singe line swap
        nums[lx], nums[lj] = nums[lj], nums[lx]
        nums2 = nums[lx+1::]
        nums2.reverse()
        nums = nums[:lx+1] + nums2
        return nums


nums = [1,3,2]
obj1 = Solution().nextPermutation(nums)
print(obj1)

"""
    for i in range(len(nums)-1, 0, -1):
            # find the index of the last peak
            if nums[i - 1] < nums[i]:
                nums[i:] = sorted(nums[i:])
                
                # get the index before the last peak
                j = i - 1
                
                # swap the pre-last peak index with the value just large than it
                for k in range(i, len(nums)):
                    if nums[j] < nums[k]:
                        nums[k], nums[j] = nums[j], nums[k]
                        return nums
        return nums.reverse()
"""