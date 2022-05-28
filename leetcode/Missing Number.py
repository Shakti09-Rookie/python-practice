# Daily Challenge 28-05-2022
# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        N = len(nums)
        for i in range(N+1):
            if i not in c:
                return i