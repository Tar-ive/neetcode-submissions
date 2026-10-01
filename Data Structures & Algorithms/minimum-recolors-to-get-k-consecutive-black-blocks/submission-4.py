class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # add r until invalid, when valid, keep shrinking l until valid 
        # how to determine how many blocks to replace. 
        # can slide a fixed sliding window through the array, and check no of black blocks, and also curr_min, which comes from k - cb

        hash = Counter(blocks[:k])
        min_black = k - hash["B"]
        for i in range(k, len(blocks)): 
            hash[blocks[i]] +=1 
            hash[blocks[i-k]] -=1
            curr_black = k - hash["B"]
            min_black = min(min_black, curr_black)

        return min_black

