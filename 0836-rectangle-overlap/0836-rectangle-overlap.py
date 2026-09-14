class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        a1, b1, a2, b2 = rec2

        return (
            max(x1, a1) < min(x2, a2)
            and
            max(y1, b1) < min(y2, b2)
        )