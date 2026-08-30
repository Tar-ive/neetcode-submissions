class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # can do similar to 2 sum. 
        #where we store k, v in hashmap 
        # if k + 1 or k -1 in hashmap, then curr_seq + 1; 
        # max of max_seq and current_seq

        max_seq = 0

        hash = set()
        curr_seq = 0 
        for n in nums:
            hash.add(n)
        
        for h in hash: 
            if h - 1 in hash: 
                continue
            else: 
                length = 0
                while (h + length) in hash: 
                    length +=1 

            max_seq = max(length, max_seq)

        return max_seq 
