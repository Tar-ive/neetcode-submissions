class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        # we need to do a 2 pass, 1 with suffix and 1 with postfix, and keep multiplying them. 

              # |1 |2 |4 |6 |
# first pass -> |1 |2 |8 |48|
# second pass<- |48|48|24|6 |
            #   |48|24|12|8 |

        prefix = 1
        for i in range(len(nums)): 
            res[i] = prefix 
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1 ): 
            res[i] *= postfix
            postfix *= nums[i]

        return res
            

