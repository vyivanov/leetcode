# https://leetcode.com/problems/path-sum/

from typing import Optional


class TreeNode:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left  = left
        self.right = right


class Solution:

    # T = O(N), S = O(1)
    #   N - amount of tree nodes
    def has_path_sum(self, root: Optional[TreeNode], target: int) -> bool:
        return self.__process(root, 0, target)

    # T = O(N), S = O(1)
    #   N - amount of tree nodes
    def __process(self, node: Optional[TreeNode], accm: int, target: int) -> bool:
        if not node:
            return False
        result = False
        if node.left is None and node.right is None:
            if accm + node.value == target:
                result = True
        else:
            accm = accm + node.value
            result = \
                self.__process(node.left,  accm, target) or \
                self.__process(node.right, accm, target)
        return result


if __name__ == '__main__':

    node_02 = TreeNode(2)
    node_07 = TreeNode(7)
    node_11 = TreeNode(11, node_07, node_02)
    node_04 = TreeNode(4, node_11)
    node_01 = TreeNode(1)
    node_44 = TreeNode(4, None, node_01)
    node_13 = TreeNode(13)
    node_08 = TreeNode(8, node_13, node_44)
    node_05 = TreeNode(5, node_04, node_08)

    assert Solution().has_path_sum(node_05, 22)    == True
    assert Solution().has_path_sum(None, 0)        == False
    assert Solution().has_path_sum(TreeNode(1), 1) == True
    assert Solution().has_path_sum(TreeNode(0), 1) == False
