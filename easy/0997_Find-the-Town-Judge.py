# https://leetcode.com/problems/find-the-town-judge/

from typing import Dict, List, Tuple, TypedDict


class Stats(TypedDict):
    inp: int
    out: int


class Solution:

    # T = O(N+K), S = O(N)
    #   N = amount of people
    #   K = amount of trusts
    @staticmethod
    def find_judge(n: int, trust: List[Tuple[int, int]]) -> int:
        assert n >= 1
        stats: Dict[int, Stats] = {
            1: {
                'inp': 0,
                'out': 0,
            }
        }
        for a, b in trust:
            if a in stats:
                stats[a]['out'] += 1
            else:
                stats[a] = {
                    'inp': 0,
                    'out': 1,
                }
            if b in stats:
                stats[b]['inp'] += 1
            else:
                stats[b] = {
                    'inp': 1,
                    'out': 0,
                }
        for idx, ref in stats.items():
            if ref['inp'] == (n-1) and ref['out'] == 0:
                return idx
        return (-1)


if __name__ == '__main__':

    assert Solution.find_judge(2, [(1, 2)]) == 2
    assert Solution.find_judge(3, [(1, 3), (2, 3)]) == 3
    assert Solution.find_judge(3, [(1, 3), (2, 3), (3, 1)]) == -1
    assert Solution.find_judge(1, []) == 1
