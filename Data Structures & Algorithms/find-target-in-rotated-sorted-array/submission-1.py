class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # need to find middle point, then check if target < pivot, search in left side, if on right side, search in right side of mid point, until we get the target. if finished and not found, return -1

        l,r = 0, len(nums) -1 

        while l <= r: 
            m = (l+r) // 2 
            if nums[m] == target: 
                return m 
            if nums[l] <= nums[m]: 
                if target >= nums[l] and target <= nums[m]: 
                    r= m-1
                else: 
                    l = m+1 
            else: 
                if target >= nums[m] and target <= nums[r]: 
                    l = m+1
                else: 
                    r = m-1

        return -1