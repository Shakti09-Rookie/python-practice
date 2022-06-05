# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallestLen = 200
        indexOfSmallest = -1
        res = ""
        string = min(strs)

        for num in range (0,len(string)):
            for i in range (0,len(strs)):
                 if(string[num] != strs[i][num]):
                        return res
            res+= string[num]

        return res