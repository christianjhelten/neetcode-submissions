"""
integer array nums where nums[i] represent money house iyh has 

houses in circle 

rob money from houses (dont rob adjacent two houses )

return maximum amount of money that we can rob

"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        elif n == 0:
            return 0

        
        def robbery(left, right):
            memo = {}

            def dfs(i): #ith house 
                if i > right: 
                    return 0 

                if i in memo: 
                    return memo[i]
                
                rob_current = nums[i] + dfs(i+2)

                skip_current = dfs(i+1)

                memo[i] = max(rob_current, skip_current)

                return memo[i]

            return dfs(left)

        return max(robbery(0, n-2), robbery(1, n-1))

    
        