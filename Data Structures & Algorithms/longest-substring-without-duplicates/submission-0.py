class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        best = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])      # evict the left char as the window shrinks
                left += 1
            seen.add(s[right])            # now the duplicate is gone, safe to add
            best = max(best, right - left + 1)
        return best