class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        for i in range(len(s)):
            seen = set()
            j = i
            while j < len(s) and s[j] not in seen:
                seen.add(s[j])
                j += 1
            best = max(best, j - i)
        return best
        #exploding time complexity O(n**2) but easiest