class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #brute force
        # use counter to get elements
        # remove that many of the value from the number and reconstruct the array 
        # or we can do a 1 pointer, array, where we change at that spot, 
        l = 0 
        for r in range(len(nums)): 
            if nums[r] != val: 
                nums[l] = nums[r]
                l +=1 
        return l 