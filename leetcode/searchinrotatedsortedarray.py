from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        for i in nums:
            if i == target:
                return True
        return False

nums = [2,5,6,0,0,1,2]
obj1 = Solution().search(nums, 0)
print(obj1)