class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        results = [1] * len(s)

        for i in range(len(s)):
            seen = {s[i]}
            j = i + 1
            while j < len(s):
                if s[j] not in seen:
                    seen.add(s[j])
                    results[i] += 1
                    j += 1
                else:
                    break

        return max(results, default=0)
