class Solution:
    def isPalindrome(self, s: str) -> bool:
        reduced = "".join([char.lower() for char in s if char.isalnum()])

        for i in range(len(reduced)):
            if reduced[i] != reduced[len(reduced)-1-i]:
                return False

        return True