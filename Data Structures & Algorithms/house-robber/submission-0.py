class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp, simiar to minimum cost question but max
        if not nums: 
            return 0 
        if len(nums) == 1: 
            return nums[0]

        n = len(nums)
        dp = [0] * (n+2)

        for i in range(n-1, -1, -1): 
            dp[i] = max(nums[i] + dp[i+2], dp[i+1]) 
        
        return dp[0]

        