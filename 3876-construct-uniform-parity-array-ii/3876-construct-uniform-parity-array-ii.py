class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        has_even = False
        has_odd = False

        for x in nums1:
            if x % 2:
                has_odd = True
            else:
                has_even = True

        # Already uniform
        if not (has_even and has_odd):
            return True

        # To make everything odd:
        # An odd number can stay unchanged.
        # An even number needs to subtract an odd smaller number.
        #
        # Therefore, we need the smallest odd number to be
        # smaller than every even number.
        min_odd = min(x for x in nums1 if x % 2)

        for x in nums1:
            if x % 2 == 0 and x < min_odd:
                return False

        return True