# Daily Challenge 07-06-2022
# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        length = len(nums2)
        c = abs(len(nums1)-n)
        for i in range(length):
            nums1[c+i] = nums2[i]
            
        nums1.sort()