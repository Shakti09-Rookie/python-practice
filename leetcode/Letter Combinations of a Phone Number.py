# Daily Challenge 09-05-2022
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}
        if digits == "":
            return []
        elif int(digits)<10:
            return dic[digits]
        else:
            output = [""]
            for d in digits:
                tmp = []
                for i in dic[d]:
                    for j in output:
                        tmp.append(j+i)
                output = tmp
            return output