class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        result = set()

        for i in range(len(digits)):
            if digits[i] == 0:
                continue

            for j in range(len(digits)):
                if j == i:
                    continue

                for k in range(len(digits)):
                    if k == i or k == j:
                        continue

                    if digits[k] % 2 == 0:
                        num = digits[i] * 100 + digits[j] * 10 + digits[k]
                        result.add(num)

        return len(result)