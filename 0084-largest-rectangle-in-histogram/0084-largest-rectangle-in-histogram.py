class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maximum = 0

        heights.append(0)

        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] > height:
                h = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                maximum = max(maximum, h * width)

            stack.append(i)

        heights.pop()

        return maximum