# https://leetcode.com/problems/remove-element/

from typing import List


class Solution:

    # T = O(N), S = O(1)
    @staticmethod
    def remove_element(nums: List[int], val: int) -> int:
        n = len(nums)
        idx_1, idx_2 = 0, n - 1
        while idx_1 <= idx_2:
            if nums[idx_1] == val:
                nums[idx_1], nums[idx_2] = nums[idx_2], nums[idx_1]
                idx_2 = idx_2 - 1
            else:
                idx_1 = idx_1 + 1
        return idx_1


if __name__ == '__main__':

    inp: List[int] = []
    k = Solution.remove_element(inp, 0)
    assert k == 0
    assert inp == []

    inp = [0]
    k = Solution.remove_element(inp, 0)
    assert k == 0
    assert inp == [0]

    inp = [1]
    k = Solution.remove_element(inp, 0)
    assert k == 1
    assert inp == [1]

    inp, out = [4, 0, 3, 4, 4, 5, 0, 0], [0, 0, 3, 0, 5]
    k = Solution.remove_element(inp, 4)
    assert k == len(out)
    for idx in range(k):
        assert inp[idx] == out[idx]
