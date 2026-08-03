class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        n = len(candidates)

        def dfs(i, target):
            if target == 0:
                ans.append(path[:])
                return

            if i == n or target < 0:
                return

            # Take current candidate
            path.append(candidates[i])
            dfs(i, target - candidates[i])
            path.pop()

            # Skip current candidate
            dfs(i + 1, target)

        dfs(0, target)
        return ans
        