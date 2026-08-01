from functools import lru_cache

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        @lru_cache(None)
        def dp(i, j):
            if i == j:
                return nums[i]

            left = nums[i] - dp(i + 1, j)
            right = nums[j] - dp(i, j - 1)

            return max(left, right)

        return dp(0, len(nums) - 1) >= 0