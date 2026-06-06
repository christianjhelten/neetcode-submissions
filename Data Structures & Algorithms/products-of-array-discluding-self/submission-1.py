''' import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            result.append(int(math.prod(nums[:i]) * math.prod(nums[i+1:])))
        return result '''


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        prefix = 1
        for i in range(n):                 # result[i] = product of everything before i
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):     # multiply in product of everything after i
            result[i] *= suffix
            suffix *= nums[i]

        return result