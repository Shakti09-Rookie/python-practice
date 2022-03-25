class Solution:
    def isValid(self, s: str) -> bool:
        li = []
        #grp = {')' : '(' , ']' : '[' , '}' : '{'}
        for i in s:
            if i in (["(","[","{"]):
                li.append(i)
                print(li)
            if i in ([")","]","}"]):
                print("entered ->", i)
                pair = {")": "(", "]": "[", "}":"{"}
                print(li)
                print("pair of what i want", pair[i])
                if not li:
                    print("entered here", li)
                    return False
                elif li.pop() != pair[i]:
                    print("entered in pop")
                    return False
                else:
                    print("only in else", li)
                    continue
        if not li:
            return True
        else:
            return False

s = "{[()]}{]{}}"
obj1 = Solution()
ans = obj1.isValid(s)
print(ans)