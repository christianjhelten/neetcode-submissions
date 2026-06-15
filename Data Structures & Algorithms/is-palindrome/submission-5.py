class Solution:
    def isPalindrome(self, s: str) -> bool:
        test = ''.join(c for c in s if c.isalnum())

        test = test.lower()

        return test == test[::-1]