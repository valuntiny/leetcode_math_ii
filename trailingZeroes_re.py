"""
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
    - need count how many 5 we have, because surely there will be enough 2
        m * 5 - 1 zero
        m * 5^2 - 1 + 1 zero
        m * 5^3 - 1 + 1 + 1 zero
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        expo, res = 0, 0
        while True:
            expo += 1
            if n / (5 ** expo) >= 1:
                res += n // (5 ** expo)
            else:
                return res

test = Solution()
n = 5
print(test.trailingZeroes(n))