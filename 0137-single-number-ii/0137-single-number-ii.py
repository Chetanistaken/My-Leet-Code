class Solution:
    def singleNumber(self, nums):
        ans = 0

        for i in range(32):
            count = 0

            for num in nums:
                # Convert negative numbers to 32-bit representation
                if num & (1 << i):
                    count += 1

            if count % 3:
                ans |= (1 << i)

        # Convert 32-bit unsigned result back to signed integer
        if ans >= (1 << 31):
            ans -= (1 << 32)

        return ans