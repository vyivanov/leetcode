# https://leetcode.com/problems/binary-tree-inorder-traversal/

from typing import Optional, List


class TreeNode:

    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:

    # T = O(N), S = O(N)
    @staticmethod
    def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
        values: List[int] = list()
        Solution.__process_subtree(root, values)
        return values

    # T = O(N), S = O(N)
    @staticmethod
    def __process_subtree(root: Optional[TreeNode], values: List[int]) -> None:
        if root:
            Solution.__process_subtree(root.left, values)
            values.append(root.value)
            Solution.__process_subtree(root.right, values)


if __name__ == '__main__':

    node_5 = TreeNode(5, None, None)
    node_4 = TreeNode(4, None, node_5)
    node_3 = TreeNode(3, None, None)
    node_2 = TreeNode(2, node_3, None)
    node_1 = TreeNode(1, node_2, node_4)
    node_r = TreeNode(0, None, node_1)

    assert Solution().inorder_traversal(node_r) == [0, 3, 2, 1, 4, 5]
