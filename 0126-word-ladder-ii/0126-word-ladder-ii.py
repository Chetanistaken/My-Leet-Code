from collections import defaultdict, deque

class Solution:
    def findLadders(
        self,
        beginWord: str,
        endWord: str,
        wordList: List[str]
    ) -> List[List[str]]:

        words = set(wordList)

        if endWord not in words:
            return []

        # parents[word] = words that can reach `word`
        # on a shortest path
        parents = defaultdict(list)

        queue = deque([beginWord])
        distance = {beginWord: 0}

        while queue:
            word = queue.popleft()
            d = distance[word]

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == word[i]:
                        continue

                    nxt = word[:i] + c + word[i + 1:]

                    if nxt not in words:
                        continue

                    if nxt not in distance:
                        distance[nxt] = d + 1
                        parents[nxt].append(word)
                        queue.append(nxt)

                    elif distance[nxt] == d + 1:
                        parents[nxt].append(word)

            if endWord in distance and d + 1 > distance[endWord]:
                break

        if endWord not in distance:
            return []

        # Reconstruct all shortest paths
        result = []
        path = [endWord]

        def dfs(word):
            if word == beginWord:
                result.append(path[::-1])
                return

            for parent in parents[word]:
                path.append(parent)
                dfs(parent)
                path.pop()

        dfs(endWord)

        return result