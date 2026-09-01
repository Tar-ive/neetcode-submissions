class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT, window = {}, {}
        for char in t: 
            countT[char] = 1+ countT.get(char,0)

        have, need = 0, len(countT)
        result, resultLength = [-1, -1], float("infinity")
        l=0 
        for r in range(len(s)): 
            char = s[r]
            window[char] = 1 + window.get(char, 0)
            if char in countT and window[char] == countT[char]: # check if we are meeting the requirement of need or not, if yes, we can increment have
                have +=1 
            
            while have == need: # while we are meeting both conditions
                #update our result 
                if (r-l+1)< resultLength: 
                    result = [l,r]
                    resultLength = (r-l+1) 
                # pop from the left of our window -> our goal is to make the smallest window possible
                window[s[l]] -=1 # decrement value of s[l] from window hashmap as we are going to. be removing that char from the left
                if s[l] in countT and window[s[l]] < countT[s[l]]:# since we have removed it 
                    have -=1
                l +=1 # move pointer to right 
        l,r = result # update result to l,r pointer as this is the best that we can get. 
        return s[l:r+1] if resultLength != float("infinity") else ""
        
        