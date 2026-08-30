class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use a frequency map approach to solve it. 
        # for that we should use hashmaps. 

        res = defaultdict(list) # map which will be used in order to store the freq of words.  

        for strg in strs: # to iterate on individual strings 
            count = [0] * 26 # initialize an array - since we know there are only 26 characters 
            for c in strg: 
                count[ord(c) - ord('a')] +=1 
            res[tuple(count)].append(strg)

        return list(res.values())

