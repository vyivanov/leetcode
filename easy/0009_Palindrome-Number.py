# https://leetcode.com/problems/palindrome-number/

class Solution:

    # T = O(N), S = O(1)
    @staticmethod
    def is_palindrome(x: int) -> bool:
        if x < 0:
            return False
        revers_x = 0
        cached_x = x
        while x > 0:
            digit = x % 10
            revers_x = digit + revers_x * 10
            x = x // 10
        return revers_x == cached_x


if __name__ == '__main__':

    assert Solution.is_palindrome(1221) is True
    assert Solution.is_palindrome(1000) is False
    assert Solution.is_palindrome(-999) is False

    assert Solution.is_palindrome(0) is True
    assert Solution.is_palindrome(7) is True

    assert Solution.is_palindrome(1111111222222222333333333444444445555555566666667777777) is False
