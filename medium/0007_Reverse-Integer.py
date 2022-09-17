# https://leetcode.com/problems/reverse-integer/

class Solution:

    MAX = 2**31 - 1
    MIN = -(MAX + 1)

    # T = O(N), S = O(1)
    @staticmethod
    def reverse(x: int) -> int:
        is_negative = False
        if x < 0:
            is_negative = True
            x = abs(x)
        inverted = 0
        while x > 0:
            digit = x % 10
            inverted = inverted * 10 + digit
            if is_negative:
                if abs(Solution.MIN) < inverted:
                    return 0
            else:
                if Solution.MAX < inverted:
                    return 0
            x = x // 10
        return -inverted if is_negative else inverted


if __name__ == '__main__':

    assert Solution.reverse(+123) == +321
    assert Solution.reverse(-123) == -321
    assert Solution.reverse(+120) == +21

    assert Solution.reverse(+1534236469) == 0
    assert Solution.reverse(-8463848412) == 0
