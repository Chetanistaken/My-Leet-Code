class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = {}

        for i in range(n - k + 1):
            window = set(nums[i:i + k])

            for num in window:
                count[num] = count.get(num, 0) + 1

        answer = -1

        for num, freq in count.items():
            if freq == 1:
                answer = max(answer, num)

        return answer