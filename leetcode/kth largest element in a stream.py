# Daily Challenge 08-04-2022
# https://leetcode.com/problems/kth-largest-element-in-a-stream/
#  solved with the help of heapq (default max heap), and discussion section

from typing import List
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k, self.nums = k, nums
        heapq.heapify(self.nums)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        
        return self.nums[-self.k]
        
        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)