class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        def backtrack(index, parts):
            if len(parts) == 4:
                if index == len(s):
                    result.append(".".join(parts))
                return

            # Remaining characters must be enough
            # and not too many for the remaining parts
            remaining = len(s) - index
            slots = 4 - len(parts)

            if remaining < slots or remaining > slots * 3:
                return

            for length in range(1, 4):
                if index + length > len(s):
                    break

                part = s[index:index + length]

                # Leading zero
                if len(part) > 1 and part[0] == '0':
                    break

                # Value must be <= 255
                if int(part) > 255:
                    break

                parts.append(part)
                backtrack(index + length, parts)
                parts.pop()

        backtrack(0, [])

        return result