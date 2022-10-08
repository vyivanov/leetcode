# https://leetcode.com/problems/maximum-subarray/

from typing import List


class Solution:

    # T = O(N), S = O(1)
    #   N - length of the 'nums' list
    @staticmethod
    def max_sub_array(nums: List[int]) -> int:
        max_sum, cur_acc = nums[0], 0
        for item in nums:
            cur_acc = cur_acc + item
            max_sum = max(max_sum, cur_acc)
            cur_acc = 0 if (cur_acc < 0) else cur_acc
        return max_sum


if __name__ == '__main__':

    assert Solution.max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert Solution.max_sub_array([-1]) == -1
    assert Solution.max_sub_array([5, 4, -1, 7, 8]) == 23
    assert Solution.max_sub_array([-1, 1]) == 1
