class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n = len(word1)
        m = len(word2)

        # right[i] = position of word2[i] when matching
        # word2[i:] as far to the right as possible.
        right = [-1] * (m + 1)
        right[m] = n

        j = n - 1

        for i in range(m - 1, -1, -1):
            while j >= 0 and word1[j] != word2[i]:
                j -= 1

            if j < 0:
                break

            right[i] = j
            j -= 1

        ans = []
        j = 0
        used = False

        for i in range(m):
            while j < n:

                # Normal matching
                if word1[j] == word2[i]:
                    ans.append(j)
                    j += 1
                    break

                # Use the one allowed mismatch
                # only if the remaining part can still
                # be matched exactly.
                if not used and right[i + 1] > j:
                    ans.append(j)
                    used = True
                    j += 1
                    break

                j += 1

            else:
                return []

        return ans