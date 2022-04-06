# Daily challenge 06-04-2022
#  https://leetcode.com/problems/3sum-with-multiplicity/

from typing import List

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        n = len(arr)
        do=[0]*300
        res=0
        for i in range(n):
            res+=do[target-arr[i]] if target-arr[i]>=0 else 0
            res%=(10**9+7)
            for j in range(i):
                do[arr[i]+arr[j]]+=1
                
        return res % (10**9+17)


# arr = [1,1,2,2,3,3,4,4,5,5]
arr = [1,1,2,2,2,2]
target = 5
obj1 = Solution().threeSumMulti(arr, target)
print(obj1)