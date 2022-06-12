# Daily Challenge 12-06-2022
# https://leetcode.com/problems/maximum-erasure-value/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        counter=defaultdict(int)
        res=i=tot=0
		
        for j in range(len(nums)):
            x=nums[j]   
            tot+=x
            counter[x]+=1
            while i < j and counter[x]>1: 
                counter[nums[i]]-=1
                tot-=nums[i]
                i+=1
            
            res=max(res, tot)            
        return res