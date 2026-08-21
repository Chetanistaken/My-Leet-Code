from math import gcd
from functools import reduce

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        # Remove duplicates
        coins = list(set(coins))

        # Remove coins that are multiples of another smaller coin
        coins.sort()
        useful = []

        for coin in coins:
            if not any(coin % x == 0 for x in useful):
                useful.append(coin)

        coins = useful

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            # Count numbers <= x divisible by at least one coin
            total = 0
            m = len(coins)

            for mask in range(1, 1 << m):
                value = 1
                bits = 0
                valid = True

                for i in range(m):
                    if mask & (1 << i):
                        value = lcm(value, coins[i])

                        if value > x:
                            valid = False
                            break

                        bits += 1

                if not valid:
                    continue

                if bits % 2:
                    total += x // value
                else:
                    total -= x // value

            return total

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left