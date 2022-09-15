# https://leetcode.com/problems/3sum/

from typing import Dict, List, Set, Tuple


class Solution:

    # T = O(N**3), S = O(K)
    def three_sum_1(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        hasht: Dict[Tuple[int, ...], List[int]] = dict()
        for i in range(0, n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n-0):
                    a, b, c = nums[i], nums[j], nums[k]
                    if a + b + c == 0:
                        self.__insert(hasht, [a, b, c])
        return self.__to_list(hasht)

    # T = O(N**2), S = O(N+K)
    def three_sum_2(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        hasht: Dict[Tuple[int, ...], List[int]] = dict()
        cache: Set[int] = set()
        for i in range(0, n-1):
            a = nums[i]
            for j in range(i+1, n-0):
                b = nums[j]
                c = -(a + b)
                if c in cache:
                    self.__insert(hasht, [a, b, c])
            cache.add(a)
        return self.__to_list(hasht)

    # T = O(N**3), S = O(K)
    def three_sum_3(self, nums: List[int]) -> List[List[int]]:
        n, nums = len(nums), sorted(nums)
        hasht: Dict[Tuple[int, ...], List[int]] = dict()
        for idx_1 in range(n-2):
            idx_2 = idx_1 + 1
            idx_3 = n - 1
            while idx_2 < idx_3:
                a, b, c = nums[idx_1], nums[idx_2], nums[idx_3]
                acc = a + b + c
                if acc == 0:
                    self.__insert(hasht, [a, b, c])
                    idx_2 = idx_2 + 1
                elif acc < 0:
                    idx_2 = idx_2 + 1
                else:
                    idx_3 = idx_3 - 1
        return self.__to_list(hasht)

    # T = O(1), S = O(1)
    def __insert(self, hasht: Dict[Tuple[int, ...], List[int]], triplet: List[int]) -> None:
        key = sorted(triplet)
        hasht[tuple(key)] = triplet

    # T = O(N), S = O(1)
    def __to_list(self, hasht: Dict[Tuple[int, ...], List[int]]) -> List[List[int]]:
        out = list()
        for _, val in hasht.items():
            out.append(val)
        return out


if __name__ == '__main__':

    assert Solution().three_sum_1([-1, 0, 1, 2, -1, -4]) == [[0, 1, -1], [-1, 2, -1]]
    assert Solution().three_sum_2([-1, 0, 1, 2, -1, -4]) == [[1, -1, 0], [2, -1, -1]]
    assert Solution().three_sum_3([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
