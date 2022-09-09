# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:

    # T = O(N**3), S = O(1)
    @staticmethod
    def longest_palindrome_1(string: str) -> str:
        n, out = len(string), str()
        for idx_bgn in range(0, n):
            for idx_end in range(idx_bgn, n):
                substring = Solution.__get_substring(string, idx_bgn, idx_end)
                if Solution.__is_palindrome(substring):
                    if len(substring) > len(out):
                        out = substring
        return out

    # T = O(N), S = O(1)
    @staticmethod
    def __is_palindrome(string: str) -> bool:
        assert len(string) > 0
        idx_bgn, idx_end = 0, len(string) - 1
        while idx_bgn < idx_end:
            if string[idx_bgn] != string[idx_end]:
                return False
            idx_bgn += 1
            idx_end -= 1
        return True

    # T = O(1), S = O(1)
    @staticmethod
    def __get_substring(string: str, idx_bgn: int, idx_end: int) -> str:
        assert len(string) >= (idx_end - idx_bgn) + 1
        return string[idx_bgn:idx_end+1]


if __name__ == '__main__':

    assert Solution.longest_palindrome_1('babad') == 'bab'
    assert Solution.longest_palindrome_1('abacdfgdcaba') == 'aba'

    # TODO: Optimize up to T = O(N**2)
