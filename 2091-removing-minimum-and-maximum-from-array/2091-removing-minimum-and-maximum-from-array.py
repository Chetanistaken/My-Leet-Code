class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        left = min(min_index, max_index)
        right = max(min_index, max_index)

        # Both from front
        front = right + 1

        # Both from back
        back = n - left

        # One from front, one from back
        both = (left + 1) + (n - right)

        return min(front, back, both)