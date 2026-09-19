class Solution:
    def integerBreak(self, n: int) -> int:
        # 4 = 2 * 2 
        # 4 = 2 + 2 

        # 12 = 3 + 3 + 3 + 3 
        # 12 = 3 * 3 * 3 * 3 

        # backward's dp. 
        # just like house robber I think 
        # 4 = 2 * 2 
        # 4 = 3 + 1 = 3 
        # 5 = 2 + 3 = 6  
        # 5 = 2 + 2 + 1 = 5 
        # 6 = 3 + 3, 4 + 2 = 4 * 8 

        # i think the lowest common multiple might be the key 
        # in even numbers its lowest common denominator 
        # in odd numbers its lowest common denominator + 1 

        # if n ==2: 
        #     return 1 
        # if n == 3: 
        #     return 2 
        
        # remainder = n % 3 
        # threes = n //3 

        # if remainder == 0:
        #     return 3 ** threes 

        # elif remainder == 1: 
        #     return (3 ** (threes -1 )) * 4 
        # else: 
        #     return (3 ** threes) * 2
        #     # how to get its 3 multiple 
        dp = {1 : 1}
        def dfs(num): 
            if num in dp: 
                return dp[num] 
            dp[num] = 0 if num == n else num
            for i in range(1, num): 
                val = dfs(i) * dfs(num-i)
                dp[num] = max(dp[num], val)
            return dp[num] 
        return dfs(n)

        


