# https://leetcode.com/problems/insert-interval/

from typing import List, Optional, Tuple, Union


class Solution:

    LEFT  = 0
    RIGHT = 1

    # T = O(N), S = O(N)
    #   N - length of the 'intervals' list
    def insert(self, intervals: List[Tuple[int, int]], new_interval: Tuple[int, int]) -> List[Tuple[int, int]]:
        out: List[Tuple[int, int]] = [new_interval]
        for item in intervals:
            pop = out.pop()
            overlap, position = self.__is_overlapped(item, pop)
            if overlap:
                out.append(self.__merge(item, pop))
            else:
                if position == Solution.LEFT:
                    out.extend([item, pop])
                else:
                    out.extend([pop, item])
        return out

    # T = O(1), S = O(1)
    def __is_overlapped(self, interval_a: Tuple[int, int], interval_b: Tuple[int, int]) -> Tuple[bool, Optional[int]]:
        if interval_a[1] < interval_b[0]:
            return False, Solution.LEFT
        if interval_b[1] < interval_a[0]:
            return False, Solution.RIGHT
        return True, None

    # T = O(1), S = O(1)
    def __merge(self, interval_a: Tuple[int, int], interval_b: Tuple[int, int]) -> Tuple[int, int]:
        return min(interval_a[0], interval_b[0]), \
               max(interval_a[1], interval_b[1])


if __name__ == '__main__':

    assert Solution().insert(
        [(1, 3), (6, 9)], (2, 5)) == [(1, 5), (6, 9)]

    assert Solution().insert(
        [(1, 2), (3, 5), (6, 7), (8, 10), (12, 16)], (4, 8)) == [(1, 2), (3, 10), (12, 16)]

    assert Solution().insert(
        [(2, 3), (4, 5)], (0, 1)) == [(0, 1), (2, 3), (4, 5)]
