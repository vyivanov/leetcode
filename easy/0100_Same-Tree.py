# https://leetcode.com/problems/same-tree/

from typing import Deque, List, Optional, Tuple
from collections import deque


class TreeNode:

    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left  = left
        self.right = right


class Solution:

    # T = O(N), S = O(N)
    #   N - amount of nodes in 'tree_a' or 'tree_b'
    def is_same_tree_1(self, tree_a: Optional[TreeNode], tree_b: Optional[TreeNode]) -> bool:
        return self.__dfs_1(tree_a, tree_b)

    # T = O(N), S = O(N)
    #   N - amount of sub-nodes in 'node_a' or 'node_b'
    def __dfs_1(self, node_a: Optional[TreeNode], node_b: Optional[TreeNode]) -> bool:
        if not node_a and not node_b:
            return True
        if not node_a or not node_b:
            return False
        if node_a.value != node_b.value:
            return False
        return self.__dfs_1(node_a.left,  node_b.left) and \
               self.__dfs_1(node_a.right, node_b.right)

    # T = O(N), S = O(N)
    #   N - amount of nodes in 'tree_a' or 'tree_b'
    def is_same_tree_2(self, tree_a: Optional[TreeNode], tree_b: Optional[TreeNode]) -> bool:
        return self.__dfs_2(tree_a, tree_b)

    # T = O(N), S = O(N)
    #   N - amount of sub-nodes in 'node_a' or 'node_b'
    def __dfs_2(self, node_a: Optional[TreeNode], node_b: Optional[TreeNode]) -> bool:
        stack: List[Tuple[Optional[TreeNode], Optional[TreeNode]]] = [(node_a, node_b)]
        while stack:
            node_a, node_b = stack.pop()
            if not node_a and not node_b:
                continue
            if not node_a or not node_b:
                return False
            if node_a.value != node_b.value:
                return False
            stack.extend([
                (node_a.right, node_b.right), (node_a.left, node_b.left)])
        return True

    # T = O(N), S = O(N)
    #   N - amount of nodes in 'tree_a' or 'tree_b'
    def is_same_tree_3(self, tree_a: Optional[TreeNode], tree_b: Optional[TreeNode]) -> bool:
        return self.__bfs(tree_a, tree_b)

    # T = O(N), S = O(N)
    #   N - amount of sub-nodes in 'node_a' or 'node_b'
    def __bfs(self, node_a: Optional[TreeNode], node_b: Optional[TreeNode]) -> bool:
        queue: Deque[Tuple[Optional[TreeNode], Optional[TreeNode]]] = deque([(node_a, node_b)])
        while queue:
            node_a, node_b = queue.popleft()
            if not node_a and not node_b:
                continue
            if not node_a or not node_b:
                return False
            if node_a.value != node_b.value:
                return False
            queue.extend([
                (node_a.left, node_b.left), (node_a.right, node_b.right)])
        return True


if __name__ == '__main__':

    for pfn in [Solution().is_same_tree_1, Solution().is_same_tree_2, Solution().is_same_tree_3]:

        assert pfn(None, None)

        assert not pfn(TreeNode(1), None)
        assert not pfn(None, TreeNode(1))

        a_1, b_1 = TreeNode(1), TreeNode(1)
        a_2, b_2 = TreeNode(2), TreeNode(2)
        a_3, b_3 = TreeNode(3), TreeNode(3)

        a_1.left, a_1.right = a_2, a_3
        b_1.left, b_1.right = b_2, b_3

        assert pfn(a_1, b_1)

        a_1.left, a_1.right = a_2, None
        b_1.left, b_1.right = None, b_2

        assert not pfn(a_1, b_1)

        a_1.left, a_1.right = a_2, a_3
        b_1.left, b_1.right = b_3, b_2

        assert not pfn(a_1, b_1)
