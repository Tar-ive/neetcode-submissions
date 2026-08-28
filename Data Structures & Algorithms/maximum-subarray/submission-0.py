class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        max_sum = 0 

        for i in range(len(nums)):
            if max_sum <0:
                max_sum = 0 
            max_sum += nums[i]
            maxSub = max(maxSub, max_sum)

        return maxSub
        