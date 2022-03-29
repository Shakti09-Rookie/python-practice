from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        an = (sorted(nums))
        for i in range(len(an)):
            if(an[i]==an[i+1]):
                return an[i]

nums = [3,1,3,4,2]
obj1 = Solution().findDuplicate(nums)
print(obj1)