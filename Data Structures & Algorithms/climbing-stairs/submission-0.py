class Solution:
    def climbStairs(self, n: int) -> int:
        #recursion and dp so we need to store the possible combinations so we dont have to check each combination 

        #combination of times
        # generate combination of values of 1 and 2 == n 
        # store each combination in set and return len(set)
        #store so that we dont have to do it each time
        # for the combination part I am thinking of using set
        # base case - 
        if n <=2: 
            return n
        res = [0] * (n+1)
        res[1], res[2] = 1, 2
        for i in range(3, n+1): 
            res[i] = res[i-1] + res[i-2]
        return res[n]

                

