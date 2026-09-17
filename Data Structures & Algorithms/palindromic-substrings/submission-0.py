class Solution:
    def countSubstrings(self, s: str) -> int:

        # is palindrome helper function
        #for each substring check that. 

        # this would be the brute force approach leading to O(n^3)

        # a more optimized solution is using dp table, or using 2 pointers 

        res = 0 
        for i in range(len(s)): 
            l,r=i,i
            while l >=0 and r < len(s) and s[l] == s[r]: 
                res +=1 
                l-=1 
                r+=1

        for i in range(len(s)): 
            l,r = i, i+1
            while l >=0 and r < len(s) and s[l] == s[r]: 
                res+=1 
                l-=1 
                r+=1 

        return res        