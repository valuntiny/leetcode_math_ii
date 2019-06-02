'''
Quest:
    Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
    If the fractional part is repeating, enclose the repeating part in parentheses.

    Example 1:
    Input: numerator = 1, denominator = 2
    Output: "0.5"

    Example 2:
    Input: numerator = 2, denominator = 1
    Output: "2"

    Example 3:
    Input: numerator = 2, denominator = 3
    Output: "0.(6)"

Solution:
    - use hashmap to store the decimal
    - remainder * 10 / denominator = the next decimal to add to the hashmap
    - negative number
    - overflow (not in python)
    - also might be sth like 0.45(6)
'''


class Solution:
    def fractionToDecimal(self, numerator, denominator):
        quotient, remainder = divmod(abs(numerator), abs(denominator))
        sign = "-" if numerator * denominator < 0 else ""
        res = [sign + str(quotient)]

        if remainder == 0:
            return ''.join(str(x) for x in res)
        res.append(".")

        hashmap = {}
        i = 2
        while remainder not in hashmap:
            hashmap[remainder] = i
            i += 1
            quotient, remainder = divmod(remainder * 10, abs(denominator))
            res.append(quotient)

        res.insert(hashmap[remainder], "(")
        res.append(")")

        return ''.join(str(x) for x in res).replace("(0)", "")

test = Solution()
print test.fractionToDecimal(1,2)
