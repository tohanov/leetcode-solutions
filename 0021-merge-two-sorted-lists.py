# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def min(self, a, b):
        next_a = None
        next_b = None

        if a is not None:
            next_a = a.next
        if b is not None:
            next_b = b.next

        if a is None:
            return b, next_a, next_b
        elif b is None:
            return a, next_a, next_b

        if a.val < b.val:
            return a, next_a, b
        return b, a, next_b

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        new_list_head, list1, list2 = self.min(list1, list2)
        new_list = new_list_head

        while list1 != None or list2 != None:
            min_pointer, list1, list2 = self.min(list1, list2)
            new_list.next = min_pointer
            new_list = min_pointer

        return new_list_head
