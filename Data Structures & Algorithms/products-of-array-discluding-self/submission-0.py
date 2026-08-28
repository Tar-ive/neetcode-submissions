class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
          # 2 pass solution 
        res = [1] * len(nums) # initialize result array 
        prefix = 1
        for n in range(len(nums)): 
            res[n] = prefix
            prefix *= nums[n]
        postfix = 1
        # loop backwards 
        for n in range(len(nums)-1, -1, -1): 
            res[n] *= postfix
            postfix *= nums[n]

        return res
            