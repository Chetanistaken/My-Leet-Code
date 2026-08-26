# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before = ListNode(0)
        after = ListNode(0)

        before_current = before
        after_current = after

        current = head

        while current:
            if current.val < x:
                before_current.next = current
                before_current = before_current.next
            else:
                after_current.next = current
                after_current = after_current.next

            current = current.next

        # End the second list
        after_current.next = None

        # Connect the two lists
        before_current.next = after.next

        return before.next