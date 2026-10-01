from collections import Counter 
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        l = 0 

        for r in range(len(nums)):
            if r - l > k: # as long as invalid window
                window.remove(nums[l]) # remove left
                l+=1
            if nums[r] in window: # since we are checking before adding r.  
                return True 
            window.add(nums[r]) # in case valid add
            
        return False


        # why is this a sliding window problem? 
        # in what situation should we slide left pointer? 


        