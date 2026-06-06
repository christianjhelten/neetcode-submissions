class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in seen:
                return [seen[dif], i]
            else:
                seen[nums[i]] = i