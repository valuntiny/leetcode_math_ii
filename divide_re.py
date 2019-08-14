"""
Quest:
    Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
    Return the quotient after dividing dividend by divisor.
    The integer division should truncate toward zero.

    Example 1:
    Input: dividend = 10, divisor = 3
    Output: 3

    Example 2:
    Input: dividend = 7, divisor = -3
    Output: -2

    Note:
    Both dividend and divisor will be 32-bit signed integers.
    The divisor will never be 0.
    Assume we are dealing with an environment which could only store integers within
    the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem,
    assume that your function returns 231 − 1 when the division result overflows.

Solution:
    - in order to speed up, we keep multiple the divisor
    - no +, but we can use << 1
    - use flag to keep track of positive or negative
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        flag = (dividend < 0) == (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0

        while dividend >= divisor:
            # use geo_divisor to speed up the extract
            geo_divisor, i = divisor, 1
            while dividend >= geo_divisor:
                dividend -= geo_divisor
                res += i
                i <<= 1
                geo_divisor <<= 1

        if not flag:
            res = -res

        # keep it within range
        return min(max(res, -2147483648), 2147483647)


test = Solution()
dividend = 7
divisor = -3
print(test.divide(dividend, divisor))