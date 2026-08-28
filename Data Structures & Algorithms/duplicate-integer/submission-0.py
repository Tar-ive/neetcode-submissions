class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashset 
        hash = set()

        for n in nums: 
            if n in hash: 
                return True 
            hash.add(n) # add elements in hashset 
        return False
        