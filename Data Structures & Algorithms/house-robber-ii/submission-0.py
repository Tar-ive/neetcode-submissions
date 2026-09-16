class Solution:
    def rob(self, nums: List[int]) -> int: 
        
        
         # if nums[i] and dp[i+2] are not nums[0] and nums[-1] because if they are it would lead to triggering of alarm. 
        
        # this is still true but there is still more to it now. 
        # 1. If there is only 1 house, return its value 
        # 2. define recursive function that: 
        #  Stops when index goes out of bounds 
        # prevents robbing last house if first was robbed 
        # max(nums[i] + dp[n+2], dp[n+1])

        # run recursive function in both the linear cases 
        # return max. 

        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums): 
        rob2, rob1 = 0,0
        for n in nums: 
                maxRob = max(n + rob2, rob1)
                rob2=rob1
                rob1=maxRob

        return rob1

