class Solution:
    def romanToInt(self, s: str) -> int:
        slen = len(s)
        tot =0
        dict = {"I" : 1,
                "V": 5,
                "X" : 10,
                "L" : 50,
                "C" : 100,
                "D" : 500,
                "M" : 1000
                }
        dictpair = {"IV" : 4, "IX" : 9,
                    "XL" : 40, "XC" : 90,
                    "CD" : 400, "CM" : 900
                }
        i=0
        while i < slen:
            if(i >= (slen-1)):
                tot+= dict[key]
                print(tot)
                i+=1
                return tot
            co = s[i]+s[i+1]
            if(co in dictpair):
                tot+= dictpair[co]
                print(tot)
                i+=2
            elif(s[i] in dict):
                key = s[i]
                tot+= dict[key]
                print(tot)
                i+=1
        return tot

obj1 = Solution().romanToInt("MMMCMXC")
print("returned total=>",obj1)