# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pointer1 = head
        pointer2 = head

        while pointer2 != None and pointer2.next != None:
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next

            if pointer1 == pointer2:
                return True

        return False


# Time complexity: O(length of list)
# Space complexity: O(1)
