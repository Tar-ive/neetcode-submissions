class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        read = 1 
        write = 1 

        while read < len(nums): 
            if nums[write-1] != nums[read]: 
                nums[write] = nums[read]
                write += 1
            read +=1 

        return write
        