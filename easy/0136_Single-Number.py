# https://leetcode.com/problems/single-number/

from typing import Dict, List


class Solution:

    # T = O(N+K), S = O(K)
    #   N - amount of initial numbers in array
    #   K - amount of unique numbers in array
    @staticmethod
    def single_number(nums: List[int]) -> int:
        counters: Dict[int, int] = dict()
        for item in nums:
            if item in counters:
                counters[item] = counters[item] + 1
            else:
                counters[item] = 1
        for item, acc in counters.items():
            if acc == 1:
                return item
        assert False


if __name__ == '__main__':

    assert Solution.single_number([0])             == 0
    assert Solution.single_number([2, 2, 1])       == 1
    assert Solution.single_number([4, 1, 2, 1, 2]) == 4
