class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        
        for i in range(len(nums)):
            result.append(int(math.prod(nums[:i]) * math.prod(nums[i+1:])))
        return result