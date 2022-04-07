# daily challenge 07-04-2022
# https://leetcode.com/problems/last-stone-weight/submissions/

from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n= len(stones)
        if n == 1:
            return stones[0]
        stones.sort()
        while n > 1:
            if stones[-1] == stones[-2]:
                del stones[-2:]
            else:
                ap = stones[-1] - stones[-2]
                del stones[-2:]
                stones.append(ap)
                stones.sort()
            n = len(stones)
        return stones
        # return 0 if n==0 else stones[0]

stones = [1]
obj1 = Solution().lastStoneWeight(stones)
print(obj1)