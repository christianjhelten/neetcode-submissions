class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}  # value -> index
        for i, n in enumerate(numbers):
            if target - n in seen:
                return [seen[target - n] + 1, i + 1]
            seen[n] = i