class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums) - 1

        while low <= high:  # 5-3 > 1 = True 
            mid = (high + low) // 2 # 4 [6]
            if nums[mid] > target: # [6] > 4 True
                high= mid -1  # 3 [4]
            elif nums[mid] < target: # [2] < 4 True
                low = mid + 1 # 3 [4]
            elif nums[mid] == target: 
                return mid 
        return -1
        