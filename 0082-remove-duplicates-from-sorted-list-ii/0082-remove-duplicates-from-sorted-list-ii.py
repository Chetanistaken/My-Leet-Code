class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:
            # Check whether current value is duplicated
            if curr.next and curr.val == curr.next.val:
                value = curr.val

                # Skip all nodes with this value
                while curr and curr.val == value:
                    curr = curr.next

                prev.next = curr

            else:
                prev = curr
                curr = curr.next

        return dummy.next