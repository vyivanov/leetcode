# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import List, Optional


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class Solution:

    # T = O(N), S = O(N)
    def merge_two_lists(self, list_1: Optional[ListNode], list_2: Optional[ListNode]) -> Optional[ListNode]:
        ptr_1, ptr_2 = list_1, list_2
        merge = list()
        while ptr_1 and ptr_2:
            itm_1, itm_2 = ptr_1.value, ptr_2.value
            if itm_1 < itm_2:
                merge.append(itm_1)
                ptr_1 = ptr_1.next
            elif itm_1 == itm_2:
                merge.extend([itm_1, itm_2])
                ptr_1 = ptr_1.next
                ptr_2 = ptr_2.next
            else:
                merge.append(itm_2)
                ptr_2 = ptr_2.next
        assert (not ptr_1 and not ptr_2) or (not ptr_1) or (not ptr_2)
        if not ptr_1 and ptr_2:
            while ptr_2:
                merge.append(ptr_2.value)
                ptr_2 = ptr_2.next
        if not ptr_2 and ptr_1:
            while ptr_1:
                merge.append(ptr_1.value)
                ptr_1 = ptr_1.next
        return self.__to_list_node(merge)

    # T = O(N), S = O(N)
    def __to_list_node(self, inp: List) -> Optional[ListNode]:
        n = len(inp)
        if n == 0:
            return None
        out = ListNode(inp[0])
        ptr = out
        for idx in range(1, n):
            ptr.next = ListNode(inp[idx])
            ptr = ptr.next
        return out


if __name__ == '__main__':

    list_1_node_2 = ListNode(5)
    list_1_node_1 = ListNode(2, list_1_node_2)
    list_1_node_0 = ListNode(1, list_1_node_1)

    list_2_node_3 = ListNode(7)
    list_2_node_2 = ListNode(3, list_2_node_3)
    list_2_node_1 = ListNode(2, list_2_node_2)
    list_2_node_0 = ListNode(1, list_2_node_1)

    lst = list()
    ptr = Solution().merge_two_lists(list_1_node_0, list_2_node_0)
    while ptr:
        lst.append(ptr.value)
        ptr = ptr.next
    assert lst == [1, 1, 2, 2, 3, 5, 7]
