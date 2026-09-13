class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]

        for i in range(rowIndex):
            row.append(0)

            for j in range(i + 1, 0, -1):
                row[j] += row[j - 1]

        return row