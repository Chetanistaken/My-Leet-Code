class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)

        left_sum = 0
        right_sum = 0
        left_q = 0
        right_q = 0

        for i in range(n // 2):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])

        for i in range(n // 2, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])

        q_diff = left_q - right_q
        sum_diff = left_sum - right_sum

        if q_diff % 2 != 0:
            return True

        return abs(sum_diff * 2 + q_diff * 9) != 0