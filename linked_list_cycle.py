""" Linked List Cycle
Given head, the head of a linked list, determine if the linked list has a cycle in it.
Test with: python -m unittest linked_list_cycle.py
"""

import unittest
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class ListNodeFactory:
    def create(self, source: List[int]) -> ListNode:
        false_head = ListNode(0)
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
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        try:
            while fast.next is not None and fast.next.next is not None:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return True
        except:
            return False


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
        self.list_node_factory = ListNodeFactory()

    def create_looped_linked_list(self, head: ListNode, position=0) -> ListNode:
        i = position
        ptr = head
        loop_target = None
        while ptr.next:
            if i == 0:
                loop_target = ptr
            ptr = ptr.next
            i -= 1
        ptr.next = loop_target
        return head

    def test_has_cycle(self):
        linked_list = self.list_node_factory.create([3, 2, 0, -4])
        pos = 1
        linked_list_with_cycle = self.create_looped_linked_list(linked_list, pos)
        answer = self.solution.hasCycle(linked_list_with_cycle)
        self.assertTrue(answer)

    def test_no_cycle(self):
        linked_list_with_no_cycles = self.list_node_factory.create([1, 2, 3, 4])
        pos = -1
        answer = self.solution.hasCycle(linked_list_with_no_cycles)
        self.assertFalse(answer)


if __name__ == 'main':
    unittest.main()
