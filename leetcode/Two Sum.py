# two sums
from typing import List

    # def twoSum(self, nums: List[int], target: int) -> List[int]:
def twoSum(nums: List[int], target: int) -> List[int]:
    size = len(nums)
    for i in range(size):
        for j in range(1+i,size):
            if(nums[i]+nums[j] == target):
                print("woow")
                return [i,j]


nums = [3,2,4]
target = 6
print(twoSum(nums, target))