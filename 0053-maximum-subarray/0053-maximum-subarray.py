class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        maximum = nums[0]

        for i in range(1, len(nums)):
            current = max(nums[i], current + nums[i])
            maximum = max(maximum, current)

        return maximum