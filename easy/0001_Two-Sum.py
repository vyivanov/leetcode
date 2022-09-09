# https://leetcode.com/problems/two-sum/

from typing import List, Tuple


class Solution:

    # T = O(N**2), S = O(1)
    @staticmethod
    def two_sum_1(nums: List[int], target: int) -> Tuple[int, int]:
        n = len(nums)
        assert n >= 2
        out = (0, 0)
        for ptr_1 in range(0, n-1):
            for ptr_2 in range(ptr_1+1, n):
                if nums[ptr_1] + nums[ptr_2] == target:
                    out = ptr_1, ptr_2
                    break
        return out

    # T = O(N), S = O(N)
    @staticmethod
    def two_sum_2(nums: List[int], target: int) -> Tuple[int, int]:
        out = (0, 0)
        cache = dict()
        for idx, itm in enumerate(nums):
            prt = target - itm
            if prt not in cache:
                cache[itm] = idx
            else:
                out = idx, cache[prt]
                break
        return out


if __name__ == '__main__':

    assert Solution.two_sum_1([3, 2, 4], 6) == (1, 2)
    assert Solution.two_sum_2([8, 0, 3, 5, 2], 10) == (4, 0)
