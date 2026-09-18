class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j = 0, 0 
        # run loop until both i and j are not bigger than len of s and t, if its bigger than s, which means that we have already gone through and gotten all chars in str s so its ok to terminate. 
        while i < len(s) and j < len(t): 
            # check elements in that specfic position 
            if s[i] == t[j]: # if equal
                i+=1 # increment i which is pointer related to string s (smaller) usually 
            j+=1 # increment j regardless 
        return len(s) == i # i will only advance when a match character is there, and if there are matches in each character, we can conclude as true otherwise false 
        