class Solution:
    def isValid(self, s: str) -> bool:
        li = []
        pair = {')' : '(' , ']' : '[' , '}' : '{'}
        for i in s:
            if i in (["(","[","{"]):
                li.append(i)    
            elif i in ([")","]","}"]):
                if not li:
                    return False
                elif li.pop() != pair[i]:
                    return False
                else:
                    continue
        if not li:
            return True
        else:
            return False

s = "{[()]}{[[]]{}}"
obj1 = Solution()
print(obj1.isValid(s))