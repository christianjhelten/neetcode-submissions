class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max, cur_min = nums[0], nums[0]
        cur_res = nums[0]

        for number in nums[1:]:
            old_max = cur_max

            cur_max = max(number, old_max * number, cur_min * number)
            cur_min = min(number, old_max * number, cur_min * number)


            cur_res = max(cur_max, cur_res)
            
        return cur_res