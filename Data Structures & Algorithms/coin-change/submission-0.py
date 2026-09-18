import heapq
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # bottom up dp 
        # we can start with the biggest no of coin and check if amount is bigger than that, as that would give us the most amount of reduction in each step. 


        # think what is p[i] here
        # what is the biggest coin I can subtract from the target to make it 0

        # what is recurrance?

        # brute force would be to check if max(coins) > amount, if not reduce that, and keep checking that, with residual value you can check, how it can be broken down with the smallest coins into smaller amounts -> greedy approach
        # moves = 0  
        # while amount:
        #     if amount > max(coins):  
        #         amount -= max(coins) 
        #         moves +=1
        #     else: 
        #         for k in range(len(coins)-1):
        #             other_max = heapq.nlargest(k, coins)[-1]
        #             amount -= other_max 
        #             moves +=1
        
        # return moves

        dp = [amount+1] * (amount+1)
        dp[0] = 0 

        for a in range(1, amount + 1): 
            for c in coins: 
                if a - c >=0: 
                    dp[a] = min(dp[a], 1+dp[a-c])

        return dp[amount] if dp[amount] != amount + 1 else -1


        