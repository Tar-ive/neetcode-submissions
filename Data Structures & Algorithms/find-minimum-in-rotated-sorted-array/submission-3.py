class Solution:
    def findMin(self, nums: List[int]) -> int:
        # we use binary search 
        # to check if the smaller element lies to the left of middle or right of middle we get the middle element and compare it to left and right. 
        # if nums[m] >=l: 
         # l=m
        #else: 
            #r-=1 
        l,r = 0, len(nums)-1
        while l < r:
            if nums[r] > nums[l]: 
                return nums[l]

            m = (l+r)//2
            if nums[m] >= nums[l]: 
                l=m+1
            else: 
                r=m
        return nums[l]