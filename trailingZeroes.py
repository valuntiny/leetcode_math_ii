'''
Quest:
    Given an integer n, return the number of trailing zeroes in n!.

    Example 1:
    Input: 3
    Output: 0
    Explanation: 3! = 6, no trailing zero.

    Example 2:
    Input: 5
    Output: 1
    Explanation: 5! = 120, one trailing zero.

    Note: Your solution should be in logarithmic time complexity.

Solution:
    using prime factorization, we can tell zero comes from 10 = 2 * 5
    - see how many multiples of 5 are there (there will be enough 2)
    - 5^1 counts as 1, 5^2 count as 2, ...
'''


class Solution:
    def trailingZeroes(self, n: int) -> int:
        i = 0 # counting exponent
        res = 0
        while True:
            i = i + 1
            if n / (5 ** i) >= 1:
                res += n // (5 ** i)
            else:
                return res
