'''
Quest:
    Given a column title as appear in an Excel sheet, return its corresponding column number.

    For example:
        A -> 1
        B -> 2
        C -> 3
        ...
        Z -> 26
        AA -> 27
        AB -> 28
        ...

    Example 1:
    Input: "A"
    Output: 1

    Example 2:
    Input: "AB"
    Output: 28

    Example 3:
    Input: "ZY"
    Output: 701

Solution:
    consider it as a 26 decimal system
    learn enumerate function
'''


class Solution:
    def titleToNumber(self, s: str) -> int:
        s = s[::-1]
        res = 0
        for exp, val in enumerate(s):
            res += (ord(val) - 64) * (26 ** exp)

        return res