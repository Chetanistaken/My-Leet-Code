class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        has_even = any(x % 2 == 0 for x in nums1)
        has_odd = any(x % 2 == 1 for x in nums1)

        # All already have the same parity
        if not (has_even and has_odd):
            return True

        # If both parities exist, choose an odd number as the reference.
        # Every even number - odd number = odd.
        # Every odd number can be kept as it is.
        return True