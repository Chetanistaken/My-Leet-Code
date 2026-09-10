class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        curr = root

        while curr:
            if curr.left:
                # Find the rightmost node of left subtree
                prev = curr.left

                while prev.right:
                    prev = prev.right

                # Attach original right subtree
                prev.right = curr.right

                # Move left subtree to right
                curr.right = curr.left
                curr.left = None

            curr = curr.right