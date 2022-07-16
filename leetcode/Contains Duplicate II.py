https://leetcode.com/problems/contains-duplicate-ii/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index = {}
        for ind,val in enumerate(nums):
            if val in index and ind - index[val] <= k:
                return True
            index[val] = ind
        return False