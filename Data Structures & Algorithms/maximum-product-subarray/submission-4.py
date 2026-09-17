class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        #need to track max and min product subarray 
        res = max(nums)
        curMax, curMin = 1, 1

        for n in nums: 
            if n == 0: 
                curMax, curMin = 1, 1
                continue
            tmp = n * curMax # to store because we will rewrite in curMax
            curMax = max(n * curMax, n*curMin, n)
            curMin = min(tmp, n * curMin, n)

            res = max(res, curMax, curMin)

        return res

        