from math import gcd
from typing import List

class Solution:
    def gcdSum(self, nums: List[int]) -> int:
        prefixGcd = []
        mx = 0

        for x in nums:
            mx = max(mx, x)
            prefixGcd.append(gcd(x, mx))

        prefixGcd.sort()

        ans = 0
        l, r = 0, len(prefixGcd) - 1

        while l < r:
            ans += gcd(prefixGcd[l], prefixGcd[r])
            l += 1
            r -= 1

        return ans