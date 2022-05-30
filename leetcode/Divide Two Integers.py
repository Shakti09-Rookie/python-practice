# Daily Challenge 30-05-2022
# https://leetcode.com/problems/divide-two-integers/

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if dividend > 0 and divisor > 0 or dividend < 0 and divisor < 0:
            positiveSign = True
        else:
            positiveSign = False
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0
        for i in reversed(range(dividend.bit_length() - divisor.bit_length() + 1)):
            if dividend >> i >= divisor:
                dividend -= divisor << i
                quotient |= 1 << i
        
        return min(2 ** 31 - 1, quotient) if positiveSign else -quotient

# class Solution:
#     def divide(self, dividend: int, divisor: int) -> int:
#         d = abs(dividend)
#         dv = abs(divisor)
#         output = 0
        
#         while d>=dv:
#             tmp=dv
#             mul=1
#             while d>=tmp:
#                 d-=tmp
#                 output+=mul
#                 mul+=mul
#                 tmp+=tmp
        
#         if(dividend<0 and divisor>=0) or (divisor<0 and divisor>=0):
#             output = -output
            
#         return min(2147483647, max(-2147483648, output))