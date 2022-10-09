# https://leetcode.com/problems/clone-graph/

from typing import Deque, Dict, List, Optional, Set, Tuple
from collections import deque


class Node:

    def __init__(self, value: int):
        self.value: int = value
        self.neighbors: List = list()


class Solution:

    # T = O(V+E), S = O(V)
    #   V - amount of nodes
    #   E - amount of edges
    def clone_graph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None
        copies: Dict[Node, Node] = dict()
        self.__make_copies(node, copies)
        self.__link_copies(copies)
        return copies[node]

    # T = O(V+E), S = O(V)
    #   V - amount of nodes
    #   E - amount of edges
    def __make_copies(self, node: Node, copies: Dict[Node, Node]) -> None:
        copies[node] = Node(node.value)
        for neighbor in node.neighbors:
            if neighbor not in copies:
                self.__make_copies(neighbor, copies)

    # T = O(V+E), S = O(1)
    #   V - amount of nodes
    #   E - amount of edges
    def __link_copies(self, copies: Dict[Node, Node]) -> None:
        for orig, copy in copies.items():
            for neighbor in orig.neighbors:
                copy.neighbors.append(copies[neighbor])


if __name__ == '__main__':

    class Checker():

        def __init__(self) -> None:
            self.__visited:  Set[Tuple[Node, Node]] = set()
            self.__enqueued: Set[Tuple[Node, Node]] = set()
            self.__queue: Deque[Tuple[Node, Node]] = deque()

        def compare(self, orig: Optional[Node], copy: Optional[Node], size: Optional[int] = None) -> None:
            if orig and copy and size:
                self.__queue.append((orig, copy))
                self.__enqueued.add((orig, copy))
                while len(self.__queue) > 0:
                    node_1, node_2 = self.__queue.popleft()
                    assert node_1 is not node_2
                    assert node_1.value == node_2.value
                    assert len(node_1.neighbors) == len(node_2.neighbors)
                    self.__enqueued.remove((node_1, node_2))
                    self.__visited.add((node_1, node_2))
                    for pair in zip(node_1.neighbors, node_2.neighbors):
                        if pair not in self.__visited and pair not in self.__enqueued:
                            self.__queue.append(pair)
                            self.__enqueued.add(pair)
                assert len(self.__visited)  == size
                assert len(self.__enqueued) == 0
            elif not orig and not copy and not size:
                assert True
            else:
                assert False

    orig = None
    copy = Solution().clone_graph(orig)
    Checker().compare(orig, copy)

    orig = Node(1)
    copy = Solution().clone_graph(orig)
    Checker().compare(orig, copy, 1)

    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)

    node_1.neighbors = [node_2, node_4]
    node_2.neighbors = [node_1, node_3]
    node_3.neighbors = [node_2, node_4]
    node_4.neighbors = [node_1, node_3]

    orig = node_1
    copy = Solution().clone_graph(orig)
    Checker().compare(orig, copy, 4)
