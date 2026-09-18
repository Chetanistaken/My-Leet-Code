class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        # Find first and last occurrence of every character
        for i, ch in enumerate(s):
            c = ord(ch) - ord('a')
            first[c] = min(first[c], i)
            last[c] = i

        intervals = []

        # Find the smallest valid interval for each character
        for c in range(26):
            if last[c] == -1:
                continue

            l = first[c]
            r = last[c]
            i = l
            valid = True

            while i <= r:
                x = ord(s[i]) - ord('a')

                if first[x] < l:
                    valid = False
                    break

                r = max(r, last[x])
                i += 1

            if valid:
                intervals.append((l, r))

        # Choose maximum number of non-overlapping intervals.
        # Sorting by ending position gives the greedy solution.
        intervals.sort(key=lambda x: x[1])

        result = []
        end = -1

        for l, r in intervals:
            if l > end:
                result.append(s[l:r + 1])
                end = r

        return result