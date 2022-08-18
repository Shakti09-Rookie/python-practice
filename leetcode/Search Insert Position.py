# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        count = 0
        for i in nums:
            if target > i:
                count += 1
            elif target == i:
                break
        return count