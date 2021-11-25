class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x< 0:
            return False
        reversed_int = 0
        y= x
        while x:
            reversed_int = reversed_int * 10 + x % 10
            x //= 10
        if reversed_int >= 2 ** 31 - 1 or reversed_int <= -2 ** 31:
            return False
        return True if reversed_int == y else False
