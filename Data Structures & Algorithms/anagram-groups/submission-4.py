from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we will store all the unique chars within a string, make that into a tuple and put that in the hashmap

        # {("a", "c", "t"):["act", "cat"], 
        # ("a", "h", "t"):["hat"]
        # ("p","o", "s", "t"):["stop", "pots", "tops"]}

    # how we get there is by first iterating over each element and adding it in a counter, and then appending the strings of a string as a key, ordered, by ascending order. 
        res = defaultdict(list)
        # default dict is used to initialize an empty dict, but specially using defaultdict as if they are no key in that dict, we can still do lookups there. 
        for string in strs: 
            count=[0] * 26 # initialize a count array to count freq, mapped to 26
            for c in string: # iterate over characters in each string 
                count[ord(c) - ord("a")]+=1 # direct address table hashing
                # for char a it is count[ord("a") - ord("a")]+=1 
                # so count[0] = 1
                # for b count[1]= 1
                # for h count[7] = 1
            res[tuple(count)].append(string)
            # appending to the result dictionary based on the count array that we have

        return list(res.values())# returning its values 

        