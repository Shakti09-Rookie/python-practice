# Daily Challenge 22-08-2022
# https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        check = 1
        while n >=check:
            if n == check: return True
            check *=4
        return False


# with loop
# class Solution:
#     def isPowerOfFour(self, n: int) -> bool:
#         check = 1
#         while n >=check:
#             if n == check: return True
#             check *=4
#         return False