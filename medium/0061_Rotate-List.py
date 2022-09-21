# https://leetcode.com/problems/rotate-list/
# mypy: ignore-errors

from typing import Optional, Tuple


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # T = O(N), S = O(1)
    def rotate_right(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n, tail = self.__len_and_tail(head)
        if n < 1:
            return head
        idx = n - (k % n)
        if idx < n:
            return self.__break_and_swap(head, tail, idx)
        else:
            return head

    # T = O(N), S = O(1)
    def __len_and_tail(self, node: Optional[ListNode]) -> Tuple[int, ListNode]:
        counter, tail = 0, None
        while node:
            counter = counter + 1
            tail = node
            node = node.next
        return counter, tail

    # T = O(N), S = O(1)
    def __break_and_swap(self, head: ListNode, tail: ListNode, idx: int) -> ListNode:
        this, prev = head, tail
        for _ in range(idx):
            prev, this = this, this.next
        prev.next = None
        tail.next = head
        tail = prev
        head = this
        return head


if __name__ == '__main__':

    node_5 = ListNode(5)
    node_4 = ListNode(4, node_5)
    node_3 = ListNode(3, node_4)
    node_2 = ListNode(2, node_3)
    node_1 = ListNode(1, node_2)
    node_0 = ListNode(0, node_1)

    out, ref = Solution().rotate_right(node_0, 4), [2, 3, 4, 5, 0, 1]
    for itm in ref:
        assert out.val == itm
        out = out.next

    assert Solution().rotate_right(None, 0) == None
