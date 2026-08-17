class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i = 0
        n = len(words)

        while i < n:
            j = i
            line_length = 0

            # Find how many words fit
            while j < n:
                if line_length + len(words[j]) + (j - i) > maxWidth:
                    break

                line_length += len(words[j])
                j += 1

            word_count = j - i
            spaces = maxWidth - line_length

            # Last line or line with one word
            if j == n or word_count == 1:
                line = ' '.join(words[i:j])
                line += ' ' * (maxWidth - len(line))
                result.append(line)

            else:
                gaps = word_count - 1
                space_each = spaces // gaps
                extra = spaces % gaps

                line = ""

                for k in range(i, j - 1):
                    line += words[k]
                    line += ' ' * (space_each + (1 if k - i < extra else 0))

                line += words[j - 1]

                result.append(line)

            i = j

        return result