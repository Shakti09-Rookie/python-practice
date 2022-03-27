# pallindrome numbers
class Solution:
    def isPalindrome(self, x: int):
        if x<0:
            print("not a pallindrome")
        else:
            reverse = 0
            x1=x
            while x1 > 0:
                digit = x1%10
                reverse = (reverse*10)+digit
                x1=x1//10

            if x == reverse:
                print("pallindrome")
                return
            print("not a pallindrome")

obj1 = Solution()
obj1.isPalindrome(123321)