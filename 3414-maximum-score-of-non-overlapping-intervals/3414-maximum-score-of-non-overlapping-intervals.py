from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        arr = sorted(
            [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)]
        )

        starts = [x[0] for x in arr]

        # First interval with start > current end
        nxt = [
            bisect_right(starts, arr[i][1])
            for i in range(n)
        ]

        # dp[k][i] = best answer using at most k intervals
        # from index i onward.
        dp = [[(0, []) for _ in range(n + 1)] for _ in range(5)]

        for k in range(1, 5):
            for i in range(n - 1, -1, -1):

                # Skip this interval
                best_score, best_indices = dp[k][i + 1]

                # Take this interval
                next_score, next_indices = dp[k - 1][nxt[i]]

                take_score = arr[i][2] + next_score
                take_indices = sorted(
                    [arr[i][3]] + next_indices
                )

                # Better score
                if take_score > best_score:
                    best_score = take_score
                    best_indices = take_indices

                # Same score -> lexicographically smaller
                elif take_score == best_score:
                    if take_indices < best_indices:
                        best_indices = take_indices

                dp[k][i] = (best_score, best_indices)

        return dp[4][0][1]