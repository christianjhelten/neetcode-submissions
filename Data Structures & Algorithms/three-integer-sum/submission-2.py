class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:   # skip a repeated fixed value
                    continue
                left, right = i + 1, len(nums) - 1     # Two Sum on the sorted remainder
                while left < right:
                    total = nums[i] + nums[left] + nums[right]
                    if total < 0:
                        left += 1                      # sum too small, need larger
                    elif total > 0:
                        right -= 1                     # sum too big, need smaller
                    else:
                        res.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1                  # skip duplicate lefts after a hit
        return res