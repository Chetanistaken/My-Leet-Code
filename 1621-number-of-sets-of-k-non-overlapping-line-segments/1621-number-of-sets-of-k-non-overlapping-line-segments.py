class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        def comb(n, r):
            result = 1

            for i in range(1, r + 1):
                result = result * (n - r + i) // i

            return result

        return comb(n + k - 1, 2 * k) % MOD