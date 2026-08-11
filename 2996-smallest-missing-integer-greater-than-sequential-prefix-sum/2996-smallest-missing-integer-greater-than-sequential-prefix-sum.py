class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find the longest sequential prefix
        total = nums[0]

        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            total += nums[i]
            i += 1

        # Find the smallest integer >= total that isn't in nums
        nums_set = set(nums)

        while total in nums_set:
            total += 1

        return total