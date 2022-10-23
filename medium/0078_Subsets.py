# https://leetcode.com/problems/subsets/

from typing import List


class Solution:

    # T = O(N**2), S = O(N**2)
    #   N - length of the 'nums' list
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.__backtrack([], [], nums, 0)

    # T = O(N**2), S = O(N**2)
    #   N - length of the 'nums' list
    def __backtrack(self, out: List[List[int]], subset: List[int], nums: List[int], k: int) -> List[List[int]]:
        out.append(subset)
        for idx in range(k, len(nums)):
            self.__backtrack(out, subset + [nums[idx]], nums, idx + 1)
        return out


if __name__ == '__main__':

    assert Solution().subsets([])     == [[]]
    assert Solution().subsets([1])    == [[], [1]]
    assert Solution().subsets([1, 2]) == [[], [1], [1, 2], [2]]

    assert Solution().subsets([1, 2, 3]) == [
        [],
        [1],
        [1, 2],
        [1, 2, 3],
        [1, 3],
        [2],
        [2, 3],
        [3]]

    assert Solution().subsets([1, 2, 3, 4]) == [
        [],
        [1],
        [1, 2],
        [1, 2, 3],
        [1, 2, 3, 4],
        [1, 2, 4],
        [1, 3],
        [1, 3, 4],
        [1, 4],
        [2],
        [2, 3],
        [2, 3, 4],
        [2, 4],
        [3],
        [3, 4],
        [4]]
