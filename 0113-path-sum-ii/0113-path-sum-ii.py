class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(node, remaining, path):
            if not node:
                return

            path.append(node.val)
            remaining -= node.val

            # Check only at a leaf
            if not node.left and not node.right:
                if remaining == 0:
                    result.append(path.copy())
            else:
                dfs(node.left, remaining, path)
                dfs(node.right, remaining, path)

            path.pop()

        dfs(root, targetSum, [])

        return result