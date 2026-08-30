class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0, len(heights) - 1

        max_amt = 0
        curr_amt = 0
        while l < r: 
            min_len = min(heights[l], heights[r])
            curr_amt = (r-l) * min_len 

            if heights[l] > heights[r]: 
                r -=1 
            elif heights[r] > heights[l]:
                l +=1 
            else: 
                l +=1 
                r -=1 
            
            max_amt = max(curr_amt, max_amt)

        return max_amt
            
        