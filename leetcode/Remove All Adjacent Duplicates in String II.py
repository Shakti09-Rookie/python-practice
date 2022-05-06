# Daily Challenge 06-05-2022
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in s:
            if stack and stack[-1][0] == i:
                stack[-1][1]+=1
            else:
                stack.append([i,1])
            if stack and stack[-1][1] == k:
                stack.pop() 
        return "".join([i*n for i,n in stack])