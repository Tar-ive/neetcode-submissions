class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=2: 
            return n 
        
        step2, step1 = 1, 2
        for i in range(3, n+1): 
            curr = step1 + step2
            step2 = step1
            step1 = curr
        return step1
        