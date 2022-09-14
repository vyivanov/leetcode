# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List


class Solution:

    # T = O(N), S = O(1)
    @staticmethod
    def remove_duplicates(nums: List[int]) -> int:
        n = len(nums)
        assert n
        idx_1, idx_2 = 0, 0
        while idx_2 < n:
            if nums[idx_1] < nums[idx_2]:
                idx_1 = idx_1 + 1
                nums[idx_1] = nums[idx_2]
            else:
                idx_2 = idx_2 + 1
        return idx_1 + 1


if __name__ == '__main__':

    inp = [1]
    k = Solution.remove_duplicates(inp)
    assert k == len(inp)
    assert inp == [1]

    inp, out = [0, 0, 1, 1], [0, 1]
    k = Solution.remove_duplicates(inp)
    assert k == len(out)
    assert inp[0] == out[0] and inp[1] == out[1]

    inp, out = [0, 0, 1, 2, 3, 3, 3, 4, 5], [0, 1, 2, 3, 4, 5]
    k = Solution.remove_duplicates(inp)
    assert k == len(out)
    for idx in range(k):
        assert inp[idx] == out[idx]
