from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)

        if endWord not in words:
            return 0

        queue = deque([(beginWord, 1)])

        while queue:
            word, steps = queue.popleft()

            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch == word[i]:
                        continue

                    new_word = word[:i] + ch + word[i + 1:]

                    if new_word == endWord:
                        return steps + 1

                    if new_word in words:
                        words.remove(new_word)
                        queue.append((new_word, steps + 1))

        return 0