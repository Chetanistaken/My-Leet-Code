class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        pos = {value: i for i, value in enumerate(inorder)}

        def build(in_start, in_end, post_start, post_end):
            if in_start > in_end:
                return None

            root_val = postorder[post_end]
            root = TreeNode(root_val)

            mid = pos[root_val]
            left_size = mid - in_start

            root.left = build(
                in_start,
                mid - 1,
                post_start,
                post_start + left_size - 1
            )

            root.right = build(
                mid + 1,
                in_end,
                post_start + left_size,
                post_end - 1
            )

            return root

        return build(0, len(inorder) - 1, 0, len(postorder) - 1)
        