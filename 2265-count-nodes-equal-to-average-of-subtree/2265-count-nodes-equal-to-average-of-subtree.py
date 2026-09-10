class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0

        def dfs(node):
            nonlocal count

            if not node:
                return 0, 0

            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            total_sum = node.val + left_sum + right_sum
            total_count = 1 + left_count + right_count

            if total_sum // total_count == node.val:
                count += 1

            return total_sum, total_count

        dfs(root)
        return count