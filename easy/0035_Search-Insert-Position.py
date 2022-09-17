# https://leetcode.com/problems/search-insert-position/

from typing import List


class Solution:

    # T = O(logN), S = O(1)
    @staticmethod
    def search_insert(nums: List[int], target: int) -> int:
        n = len(nums)
        assert n > 0
        idx_1, idx_2 = 0, n - 1
        while idx_1 <= idx_2:
            mid = (idx_1 + idx_2) // 2
            if target < nums[mid]:
                idx_2 = mid - 1
            elif target > nums[mid]:
                idx_1 = mid + 1
            else:
                return mid
        return idx_1


if __name__ == '__main__':

    assert Solution.search_insert([1, 3, 5, 6], 5) == 2
    assert Solution.search_insert([1, 3, 5, 6], 2) == 1
    assert Solution.search_insert([1, 3, 5, 6], 7) == 4
