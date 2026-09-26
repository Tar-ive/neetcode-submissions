class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # brute force would be : 
        # check each prefix, maybe start with smallest length word, check get all of its prefixes and check if it exists or not in all the other strs. max_length of successful str will be max of max_prefix and current prefix which passes all the conditions if yes, return that prefix, continue doing that and at the end return max_prefix, if not return empty string.
        res = ""
        for i in range(len(strs[0])): 
            for s in strs: 
                if i ==len(s) or s[i] != strs[0][i]: 
                    return res 
            res += strs[0][i]
        return res
                    
            