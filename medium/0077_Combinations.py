# https://leetcode.com/problems/combinations/

from typing import List


class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        assert (1 <= n <= 20) and (1 <= k <= n)
        combs: List[List[int]] = list()
        self.__backtrack(combs, [], n, k, 1)
        return combs

    # TODO: Estimate time-to-space complexity
    def __backtrack(self, combs: List[List[int]], mix: List[int], n: int, k: int, j: int) -> None:
        if len(mix) == k:
            combs.append(mix)
        else:
            for digit in range(j+0, n+1):
                self.__backtrack(combs, mix + [digit], n, k, digit + 1)


if __name__ == '__main__':

    assert Solution().combine(n=1, k=1) == [[1]]
    assert Solution().combine(n=2, k=1) == [[1], [2]]
    assert Solution().combine(n=2, k=2) == [[1, 2]]
    assert Solution().combine(n=3, k=1) == [[1], [2], [3]]
    assert Solution().combine(n=3, k=2) == [[1, 2], [1, 3], [2, 3]]
    assert Solution().combine(n=3, k=3) == [[1, 2, 3]]
    assert Solution().combine(n=4, k=1) == [[1], [2], [3], [4]]
    assert Solution().combine(n=4, k=2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    assert Solution().combine(n=4, k=3) == [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
    assert Solution().combine(n=4, k=4) == [[1, 2, 3, 4]]
