from typing import List
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        # Frequency of each value
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        # pairs_div[g] = number of pairs whose gcd is divisible by g
        pairs_div = [0] * (mx + 1)

        for g in range(1, mx + 1):
            cnt = 0
            for multiple in range(g, mx + 1, g):
                cnt += freq[multiple]
            pairs_div[g] = cnt * (cnt - 1) // 2

        # exact[g] = number of pairs whose gcd is exactly g
        exact = [0] * (mx + 1)

        for g in range(mx, 0, -1):
            exact[g] = pairs_div[g]
            for multiple in range(2 * g, mx + 1, g):
                exact[g] -= exact[multiple]

        # Prefix counts of gcd values in sorted order
        prefix = []
        values = []
        total = 0

        for g in range(1, mx + 1):
            if exact[g]:
                total += exact[g]
                prefix.append(total)
                values.append(g)

        # Answer queries
        ans = []
        for q in queries:
            idx = bisect_right(prefix, q)
            ans.append(values[idx])

        return ans