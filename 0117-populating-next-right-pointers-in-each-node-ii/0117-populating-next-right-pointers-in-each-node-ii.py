class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        curr = root

        while curr:
            dummy = Node(0)
            tail = dummy

            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next

                if curr.right:
                    tail.next = curr.right
                    tail = tail.next

                curr = curr.next

            curr = dummy.next

        return root