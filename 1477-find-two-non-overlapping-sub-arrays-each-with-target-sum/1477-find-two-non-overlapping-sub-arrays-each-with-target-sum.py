class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        INF = n + 1

        # best[i] = shortest valid subarray ending at or before i
        best = [INF] * n

        left = 0
        curr_sum = 0
        ans = INF
        shortest = INF

        for right in range(n):
            curr_sum += arr[right]

            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                length = right - left + 1

                # A previous subarray must end before `left`
                if left > 0 and best[left - 1] != INF:
                    ans = min(ans, length + best[left - 1])

                shortest = min(shortest, length)

            best[right] = shortest

        return -1 if ans == INF else ans