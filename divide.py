'''
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

Solution:
    just use minus
    but in order to keep it fast, we need a special way to geometrical speed it up
'''


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        flag = (dividend < 0) == (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            tmp, i = divisor, 1

            # geometrical speed up, keep double the divisor until out of range
            # then come back to 1 divisor again, and double
            while dividend >= tmp:
                dividend -= tmp
                res += i
                i <<= 1
                tmp <<= 1

        if not flag:
            res = -res

        return min(max(res, -2147483648), 2147483647)
