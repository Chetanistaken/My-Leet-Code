class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # pal[l][r] = 1 if s[l:r+1] is a palindrome
        pal = [bytearray(n) for _ in range(n)]

        for i in range(n):
            pal[i][i] = 1

        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                if s[l] == s[r] and (length == 2 or pal[l + 1][r - 1]):
                    pal[l][r] = 1

        # dp[i] = maximum number of valid palindromes
        # using the first i characters
        dp = [0] * (n + 1)

        for r in range(n):
            # Don't use s[r]
            dp[r + 1] = dp[r]

            for l in range(r + 1):
                if r - l + 1 >= k and pal[l][r]:
                    dp[r + 1] = max(dp[r + 1], dp[l] + 1)

        return dp[n]