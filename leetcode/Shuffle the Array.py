# https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        temp = []
        for i in range(n):
            temp.append(nums[i])
            temp.append(nums[n+i])
        return temp