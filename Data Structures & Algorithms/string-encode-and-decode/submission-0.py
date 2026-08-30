class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs: 
            res = res + str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:

        res = []
        i = 0 # keep track of which part of the string we are in
        while i < len(s): 
            j = i # introducing another pointer j so that we can do list comprehension 
            # need to only get the integer, and j should be at the # delimiter
            while s[j] != "#": # we know that it will be a # delimiter as that is how we encoded it
                j +=1 
            length = int(s[i:j]) # because when the while loop ends we know that j is at delimiter 
            res.append(s[j+1:j+1+length])

            i = j+ 1+ length 
        
        return res

