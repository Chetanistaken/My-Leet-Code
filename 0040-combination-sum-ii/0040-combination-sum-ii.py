class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        ans = []
        path = []

        def backtrack(start, target):
            if target == 0:
                ans.append(path[:])
                return

            for i in range(start, len(candidates)):

                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # No need to continue if current number is too large
                if candidates[i] > target:
                    break

                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i])  # use each number once
                path.pop()

        backtrack(0, target)
        return ans
        