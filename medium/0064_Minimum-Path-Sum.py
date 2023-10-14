# https://leetcode.com/problems/minimum-path-sum/

from typing import List, Optional, Tuple


class Solution:

    def minPathSum(self, grid: List[List[int]]) -> Optional[int]:
        assert 1 <= len(grid)    <= 200
        assert 1 <= len(grid[0]) <= 200
        min_sum: List[Optional[int]] = [None]
        self.__backtrack((0, 0), grid, 0, min_sum)
        return min_sum[0]

    def __backtrack(self, pose: Tuple[int, int], grid: List[List[int]], acc: int, min_sum: List[Optional[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        i, j = pose
        if i == rows-1 and j == cols-1:
            acc += grid[i][j]
            min_sum[0] = min(min_sum[0], acc) if min_sum[0] is not None else acc
            return
        if i == rows or j == cols:
            return
        self.__backtrack((i, j+1), grid, acc + grid[i][j], min_sum)
        self.__backtrack((i+1, j), grid, acc + grid[i][j], min_sum)


if __name__ == '__main__':

    assert Solution().minPathSum([
        [0, 0]
    ]) \
    == 0

    assert Solution().minPathSum([
        [0, 1]
    ]) \
    == 1

    assert Solution().minPathSum([
        [0, 1, 2]
    ]) \
    == 3

    assert Solution().minPathSum([
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1],
    ]) \
    == 7

    assert Solution().minPathSum([
        [1, 2, 3],
        [4, 5, 6],
    ]) \
    == 12

    # TODO: Optimize via memoization
    assert Solution().minPathSum([
        [7, 1, 3, 5, 8, 9, 9, 2, 1, 9, 0, 8, 3, 1, 6, 6, 9, 5],
        [9, 5, 9, 4, 0, 4, 8, 8, 9, 5, 7, 3, 6, 6, 6, 9, 1, 6],
        [8, 2, 9, 1, 3, 1, 9, 7, 2, 5, 3, 1, 2, 4, 8, 2, 8, 8],
        [6, 7, 9, 8, 4, 8, 3, 0, 4, 0, 9, 6, 6, 0, 0, 5, 1, 4],
        [7, 1, 3, 1, 8, 8, 3, 1, 2, 1, 5, 0, 2, 1, 9, 1, 1, 4],
        [9, 5, 4, 3, 5, 6, 1, 3, 6, 4, 9, 7, 0, 8, 0, 3, 9, 9],
        [1, 4, 2, 5, 8, 7, 7, 0, 0, 7, 1, 2, 1, 2, 7, 7, 7, 4],
        [3, 9, 7, 9, 5, 8, 9, 5, 6, 9, 8, 8, 0, 1, 4, 2, 8, 2],
        [1, 5, 2, 2, 2, 5, 6, 3, 9, 3, 1, 7, 9, 6, 8, 6, 8, 3],
        [5, 7, 8, 3, 8, 8, 3, 9, 9, 8, 1, 9, 2, 5, 4, 7, 7, 7],
        [2, 3, 2, 4, 8, 5, 1, 7, 2, 9, 5, 2, 4, 2, 9, 2, 8, 7],
        [0, 1, 6, 1, 1, 0, 0, 6, 5, 4, 3, 4, 3, 7, 9, 6, 1, 9],
    ]) \
    == 85
