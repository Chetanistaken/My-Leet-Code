class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        # Find middle node
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Single node
        if prev:
            prev.next = None
        else:
            head = None

        root = TreeNode(slow.val)

        if prev:
            root.left = self.sortedListToBST(head)

        root.right = self.sortedListToBST(slow.next)

        return root