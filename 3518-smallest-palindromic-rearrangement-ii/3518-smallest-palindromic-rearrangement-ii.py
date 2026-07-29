from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)

        half = [0] * 26
        mid = ""
        total_half = 0

        for ch, f in freq.items():
            if f % 2:
                mid = ch
            half[ord(ch) - ord("a")] = f // 2
            total_half += f // 2

        CAP = k

        def comb_cap(n, r):
            r = min(r, n - r)
            res = 1
            for i in range(1, r + 1):
                res = res * (n - r + i) // i
                if res > CAP:
                    return CAP
            return res

        def count_perms(cnt):
            rem = sum(cnt)
            ans = 1
            for c in cnt:
                if c:
                    ans *= comb_cap(rem, c)
                    if ans > CAP:
                        return CAP
                    rem -= c
            return ans

        if count_perms(half) < k:
            return ""

        first = []

        for _ in range(total_half):
            for i in range(26):
                if half[i] == 0:
                    continue
                half[i] -= 1
                ways = count_perms(half)
                if ways >= k:
                    first.append(chr(i + ord("a")))
                    break
                k -= ways
                half[i] += 1

        left = "".join(first)
        return left + mid + left[::-1]