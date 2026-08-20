class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = list(range(n + 1))

        for i in range(1, m + 1):
            prev = dp[0]
            dp[0] = i

            for j in range(1, n + 1):
                temp = dp[j]

                if word1[i - 1] == word2[j - 1]:
                    dp[j] = prev
                else:
                    dp[j] = 1 + min(
                        dp[j],      # Delete
                        dp[j - 1],  # Insert
                        prev        # Replace
                    )

                prev = temp

        return dp[n]