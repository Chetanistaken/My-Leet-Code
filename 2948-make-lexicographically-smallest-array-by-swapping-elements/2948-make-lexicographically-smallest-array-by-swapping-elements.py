class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)

        # Store (value, original index)
        arr = sorted((nums[i], i) for i in range(n))

        result = nums[:]

        i = 0

        while i < n:
            j = i

            # Find all values belonging to the same group
            while j + 1 < n and arr[j + 1][0] - arr[j][0] <= limit:
                j += 1

            # Original indices in this group
            indices = []

            for k in range(i, j + 1):
                indices.append(arr[k][1])

            indices.sort()

            # Values are already sorted
            for k in range(j - i + 1):
                result[indices[k]] = arr[i + k][0]

            i = j + 1

        return result
        