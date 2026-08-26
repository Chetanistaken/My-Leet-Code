class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        heights = [0] * cols
        answer = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            stack = [-1]

            for j in range(cols + 1):
                current = heights[j] if j < cols else 0

                while stack[-1] != -1 and heights[stack[-1]] > current:
                    h = heights[stack.pop()]
                    width = j - stack[-1] - 1
                    answer = max(answer, h * width)

                stack.append(j)

        return answer