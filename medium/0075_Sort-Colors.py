# https://leetcode.com/problems/sort-colors/

from typing import List


class Solution:

    RED = 0
    WHITE = 1
    BLUE = 2

    # T = O(N), S = O(1)
    @staticmethod
    def sort_colors_1(colors: List[int]) -> None:
        counters = {
            Solution.RED: 0, Solution.WHITE: 0, Solution.BLUE: 0
        }
        for color in colors:
            counters[color] = counters[color] + 1
        idx = 0
        for color, counter in counters.items():
            for _ in range(counter):
                colors[idx] = color
                idx = idx + 1

    # T = O(N), S = O(1)
    @staticmethod
    def sort_colors_2(colors: List[int]) -> None:
        n = len(colors)
        idx_0, idx_1, idx_2 = 0, 0, (n-1)
        while idx_1 <= idx_2:
            if colors[idx_1] == Solution.RED:
                colors[idx_0], colors[idx_1] = colors[idx_1], colors[idx_0]
                idx_0, idx_1 = idx_0 + 1, idx_1 + 1
            elif colors[idx_1] == Solution.BLUE:
                colors[idx_1], colors[idx_2] = colors[idx_2], colors[idx_1]
                idx_2 = idx_2 - 1
            else:
                idx_1 = idx_1 + 1


if __name__ == '__main__':

    solutions = [
        Solution.sort_colors_1,
        Solution.sort_colors_2,
    ]

    for pfn in solutions:

        inp, out = [0], [0]
        pfn(inp)
        assert inp == out

        inp, out = [2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]
        pfn(inp)
        assert inp == out

        inp, out = [1, 1, 0, 2, 0, 0, 1, 2, 2, 1], [0, 0, 0, 1, 1, 1, 1, 2, 2, 2]
        pfn(inp)
        assert inp == out

        inp, out = [2, 0, 1], [0, 1, 2]
        pfn(inp)
        assert inp == out
