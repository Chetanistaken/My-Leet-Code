class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = []

        for i in range(len(s)):
            if s[i] == '1':
                ones.append(i)

        if len(ones) < k:
            return ""

        best = None

        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]

            candidate = s[start:end + 1]

            if best is None:
                best = candidate
            elif len(candidate) < len(best):
                best = candidate
            elif len(candidate) == len(best) and candidate < best:
                best = candidate

        return best