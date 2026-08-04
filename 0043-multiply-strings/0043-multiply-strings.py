from typing import List

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                p1 = i + j
                p2 = i + j + 1

                total = mul + res[p2]
                res[p2] = total % 10
                res[p1] += total // 10

        result = []

        for digit in res:
            if not (len(result) == 0 and digit == 0):
                result.append(str(digit))

        return "".join(result)
        