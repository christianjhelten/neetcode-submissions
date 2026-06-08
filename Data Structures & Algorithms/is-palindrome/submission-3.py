class Solution:
    def isPalindrome(self, s: str) -> bool:
       results = ''.join(c for c in s if c.isalnum())
       results = results.lower()
       
       return results == results[::-1]  
