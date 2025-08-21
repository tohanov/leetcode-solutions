# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        left_of_break = head
        right_of_break = head.next
        before_left_of_break = None

        while right_of_break is not None:
            left_of_break.next = before_left_of_break
            left_of_break, right_of_break, before_left_of_break = (
                right_of_break,
                right_of_break.next,
                left_of_break,
            )

        left_of_break.next = before_left_of_break
        return left_of_break


# Time complexity: O(length of list)
# Space complexity: O(1)
