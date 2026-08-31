class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # this is always a character in the input that we are given. 
        # zxyzxyz
        
        # hashset = O(1) time O(n) space complexity 
        # abcabcbb
        # L
        #  R
        # max_length = 3 (r-l) = 4-1 = 3 
        

        hash = set()
        res = 0

        l = 0 
        for r in range(len(s)): # 0 - 8
            while s[r] in hash: 
                hash.remove(s[l])
                l+=1
            hash.add(s[r])
        
            res = max(res, (r-l+1))

        return res
