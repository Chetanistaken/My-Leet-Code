class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending in 0 (except 0 itself)
        # cannot be palindromes.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        rev = 0

        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10

        # Even digits: x == rev
        # Odd digits: x == rev // 10 (middle digit ignored)
        return x == rev or x == rev // 10