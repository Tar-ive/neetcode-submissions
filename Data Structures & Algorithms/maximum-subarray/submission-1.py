import math 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -math.inf
        curr_sum = 0 # 0

        for n in nums: # 
            if curr_sum < 0: 
                curr_sum = 0 # 0
            curr_sum = curr_sum + n # 2
            maxSum = max(curr_sum, maxSum) # 4    

        return maxSum
        