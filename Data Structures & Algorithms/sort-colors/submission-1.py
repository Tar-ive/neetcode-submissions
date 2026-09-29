class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # run 2 pointes, if 2 move to right, if 0 move to left
        l = 0 
        r = len(nums) - 1 
        current = 0 
        while current <= r: 
            if nums[current] == 2: 
                nums[r], nums[current] = nums[current], nums[r]
                r-=1 
            elif nums[current] == 0: 
                nums[l], nums[current] = nums[current], nums[l]
                l+=1
                current +=1
            else: 
                current +=1
        return nums