class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1 #read 
        r = 1 # write

        while r < len(nums): 
            if nums[l-1] != nums[r]: 
                nums[l] = nums[r]
                l += 1
            r +=1 
        return l

#nums[read]= 2
#nums[write -1 ] = 1
# read = 2
# write = 2
# nums = [1,2,3,4]
        