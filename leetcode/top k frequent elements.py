# Daily Challenge 09-04-2022
# https://leetcode.com/problems/top-k-frequent-elements/

from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [x[0] for x in Counter(nums).most_common(k)]

nums = [1,1,1,2,2,3]
k = 2
obj1 = Solution().topKFrequent(nums, k)
print(obj1)

"""
to do without using counter 
from GFG
def CountFrequency(my_list):
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
 
    for key, value in freq.items():
        print ("% d : % d"%(key, value))
 
if __name__ == "__main__":
    my_list =[1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
 
    CountFrequency(my_list)
"""