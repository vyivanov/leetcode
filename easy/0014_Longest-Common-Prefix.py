# https://leetcode.com/problems/longest-common-prefix/

from typing import List


class Solution:

    # T = O(N*M), S = O(1)
    @staticmethod
    def longest_common_prefix(strs: List[str]) -> str:
        assert len(strs) > 0
        ref_str, ref_len = strs[0], len(strs[0])
        if ref_len == 0:
            return ''
        for idx in range(ref_len):
            for cur_str in strs:
                if len(cur_str) <= idx:
                    return ref_str[:idx]
                if cur_str[idx] != ref_str[idx]:
                    return ref_str[:idx]
        return ref_str


if __name__ == '__main__':

    assert Solution.longest_common_prefix(['flower', 'flow', 'flight']) == 'fl'
    assert Solution.longest_common_prefix(['hey']) == 'hey'
    assert Solution.longest_common_prefix(['dog', 'racecar', 'car']) == ''
    assert Solution.longest_common_prefix(['']) == ''
