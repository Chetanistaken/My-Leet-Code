class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            l, r = i + 1, n - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if abs(s - target) < abs(closest - target):
                    closest = s

                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return target

        return closest