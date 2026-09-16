class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')

        def dfs(node):
            nonlocal ans

            if not node:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            # Path passing through current node
            current = node.val + left + right
            ans = max(ans, current)

            # Maximum path that can be extended to parent
            return node.val + max(left, right)

        dfs(root)
        return ans