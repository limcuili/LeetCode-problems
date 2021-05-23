""" Merge Two Sorted Lists
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.
Test with: python -m unittest Merge_Two_Sorted_Lists.py
"""

import unittest


class ListNode:
    def init(self, val=0, next=None):
        self.val = val
        self.next = next

    def to_list(self) -> list[int]:
        output_list = [self.val]
        current = self.next

        while current is not None:
            output_list.append(current.val)
            current = current.next

        return output_list


class ListNodeFactory:
    def create(self, source: list[int]) -> ListNode:
        false_head = ListNode()
        current_head = false_head

        for item in source:
            node = ListNode(item)
            current_head.next = node
            current_head = current_head.next

        return false_head.next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # write here :)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_two_element_sort(self):
        l1 = self.list_node_factory.create([1, 2, 4])
        l2 = self.list_node_factory.create([1, 3, 4])
        expected_answer = [1, 1, 2, 3, 4, 4]
        answer = self.solution.mergeTwoLists(l1, l2).to_list()
        self.assertEqual(expected_answer, answer)


if __name__ == 'main':
    unittest.main()