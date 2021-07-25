""" Merge Two Sorted Lists
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.
Test with: python -m unittest merge_two_sorted_lists.py
"""

import unittest
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ListNodeFactory:
    def create(self, source: list[int]) -> ListNode:
        false_head = ListNode()
        current_head = false_head

        for item in source:
            node = ListNode(item)
            current_head.next = node
            current_head = current_head.next

        return false_head.next

    def create_list(self, head: ListNode) -> List[int]:
        if head is None:
            return []

        output_list = [head.val]
        current = head.next

        while current is not None:
            output_list.append(current.val)
            current = current.next

        return output_list


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        merged_list = ListNode()
        head = merged_list
        while l1 and l2 is not None:
            if l1.val < l2.val:
                head.next = l1
                head = head.next
                l1 = l1.next
            else:
                head.next = l2
                head = head.next
                l2 = l2.next
        head.next = l1 or l2

        return merged_list.next


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.list_node_factory = ListNodeFactory()
        self.solution = Solution()

    def test_two_element_sort(self):
        l1 = self.list_node_factory.create([1, 2, 4])
        l2 = self.list_node_factory.create([1, 3, 4])
        expected_answer = [1, 1, 2, 3, 4, 4]
        answer = self.solution.mergeTwoLists(l1, l2)
        answer_as_list = self.list_node_factory.create_list(answer)
        self.assertEqual(expected_answer, answer_as_list)


if __name__ == 'main':
    unittest.main()
