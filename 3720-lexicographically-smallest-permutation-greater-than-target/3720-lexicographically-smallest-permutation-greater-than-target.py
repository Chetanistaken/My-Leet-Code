class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Try each position as the first position
        # where our answer is greater than target.
        for i in range(n - 1, -1, -1):

            # Fresh frequency count
            count = [0] * 26

            for ch in s:
                count[ord(ch) - ord('a')] += 1

            # Use the same prefix as target
            possible = True

            for j in range(i):
                idx = ord(target[j]) - ord('a')

                if count[idx] == 0:
                    possible = False
                    break

                count[idx] -= 1

            if not possible:
                continue

            # Find the smallest character greater than target[i]
            current = ord(target[i]) - ord('a')

            for c in range(current + 1, 26):
                if count[c] > 0:
                    count[c] -= 1

                    # Prefix + larger character
                    result = target[:i] + chr(c + ord('a'))

                    # Put remaining characters in sorted order
                    for x in range(26):
                        result += chr(x + ord('a')) * count[x]

                    return result

        return ""