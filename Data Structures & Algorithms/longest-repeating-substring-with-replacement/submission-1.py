class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0 
        hash = {}

        l = 0 
        for r in range(len(s)): 
            # need to add in hashmap count 
            hash[s[r]] = hash.get(s[r], 0) +1
            while (r-l+1) - max(hash.values())>k: # valid 
                hash[s[l]]-=1
                l+=1
            res = max(res, r-l+1)
        return res
        