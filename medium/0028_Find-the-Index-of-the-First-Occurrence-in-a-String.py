# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution:

    # T = O(N*K), S = O(1)
    #   N - length of the 'haystack' string
    #   K - length of the 'needle' string
    @staticmethod
    def str_str(haystack: str, needle: str) -> int:
        len_h, len_n = len(haystack), len(needle)
        idx_h, idx_n, ptr_h = (0, 0, 0)
        while idx_h < len_h:
            if haystack[idx_h] == needle[idx_n]:
                idx_h, idx_n = (idx_h + 1), (idx_n + 1)
            else:
                ptr_h = (ptr_h + 1)
                idx_h, idx_n = ptr_h, 0
            if idx_n == len_n:
                return ptr_h
        return (-1)


if __name__ == '__main__':

    assert Solution.str_str('sadbutsad'  , 'sad')              == (+0)
    assert Solution.str_str('mississippi', 'issip')            == (+4)
    assert Solution.str_str('abcdefg'    , 'abcdefghijklmnop') == (-1)
    assert Solution.str_str('a'          , 'a')                == (+0)
    assert Solution.str_str('qwerty'     , 'rt')               == (+3)
    assert Solution.str_str('qwerty'     , 'rt')               == (+3)
    assert Solution.str_str('abcdefg'    , 'z')                == (-1)
