class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}

        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = 0

            rows[row] |= 1 << (seat - 1)

        # Rows with no reserved seats can fit 2 families
        answer = (n - len(rows)) * 2

        for mask in rows.values():
            count = 0

            # Seats 2,3,4,5
            if mask & 0b000011110 == 0:
                count += 1

            # Seats 6,7,8,9
            if mask & 0b111100000 == 0:
                count += 1

            # If neither side works, try seats 4,5,6,7
            if count == 0:
                if mask & 0b001111000 == 0:
                    count = 1

            answer += count

        return answer