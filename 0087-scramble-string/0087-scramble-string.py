class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}

        def dfs(a, b):
            if a == b:
                return True

            key = (a, b)

            if key in memo:
                return memo[key]

            # Different characters → impossible
            if sorted(a) != sorted(b):
                memo[key] = False
                return False

            n = len(a)

            for i in range(1, n):
                # No swap
                if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):
                    memo[key] = True
                    return True

                # Swap
                if dfs(a[:i], b[n-i:]) and dfs(a[i:], b[:n-i]):
                    memo[key] = True
                    return True

            memo[key] = False
            return False

        return dfs(s1, s2)