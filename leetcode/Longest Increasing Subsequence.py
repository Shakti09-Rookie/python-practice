# https://leetcode.com/problems/longest-increasing-subsequence/

def binarySearch(nums,start,end,target):
    while start<=end:
        mid=(start+end)//2
        if nums[mid]==target:
            return mid
        if nums[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans=[]
        ans.append(nums[0])
        n=len(nums)
        for i in range(1,n):
           if ans[-1]<nums[i]:
                ans.append(nums[i])
           else:
                index=binarySearch(ans,0,len(ans)-1,nums[i])
                ans[index]=nums[i]

        return len(ans)