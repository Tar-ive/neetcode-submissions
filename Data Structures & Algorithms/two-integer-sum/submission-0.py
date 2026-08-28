class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # index:value 
        for i , n in enumerate(nums): # getting i and v of nums 
            diff = target - n #subtraction 
            if diff in prevMap: #if difference is in hashmap already- pair
                return [prevMap[diff], i] # get indices 
            prevMap[n] = i  # need to insert into hashmap
        return 