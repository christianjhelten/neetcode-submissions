import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = []

        for i in range(len(nums)):
            results.append(math.prod(nums[:i]) * math.prod(nums[i+1:]))

        return results 