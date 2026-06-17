class Solution:
    def climbStairs(self, n: int) -> int:
        #this is a fibonacci-style problem, we could compute all the fibonacci numbers
        #to reach our result but that will explode so we just keep the last two


        l_one, l_two = 1,1

        for i in range(n-1):
            temp = l_one
            l_one = l_one + l_two
            l_two = temp

        return l_one