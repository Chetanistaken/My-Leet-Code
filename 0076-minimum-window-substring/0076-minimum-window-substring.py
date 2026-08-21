class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = {}

        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        window = {}

        left = 0
        have = 0
        required = len(need)

        best_length = float('inf')
        best_left = 0

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                have += 1

            # Try shrinking the window
            while have == required:
                length = right - left + 1

                if length < best_length:
                    best_length = length
                    best_left = left

                left_char = s[left]
                window[left_char] -= 1

                if (left_char in need and
                        window[left_char] < need[left_char]):
                    have -= 1

                left += 1

        if best_length == float('inf'):
            return ""

        return s[best_left:best_left + best_length]