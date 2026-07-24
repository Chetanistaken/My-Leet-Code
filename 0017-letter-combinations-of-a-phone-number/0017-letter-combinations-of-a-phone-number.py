class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mp = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        ans = []

        def backtrack(i, path):
            if i == len(digits):
                ans.append(path)
                return

            for ch in mp[digits[i]]:
                backtrack(i + 1, path + ch)

        backtrack(0, "")
        return ans