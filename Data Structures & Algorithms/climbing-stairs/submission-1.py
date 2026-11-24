class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def go(rem):
            if rem == 0: 
                return 1 
            if rem < 0:
                return 0 
            if rem in memo:
                return memo[rem]
        
            memo[rem] = go(rem - 1) + go(rem - 2)
            return memo[rem] 

        return go(n)