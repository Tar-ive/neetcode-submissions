class Solution:
    def isHappy(self, n: int) -> bool:
        hash = set()
        
        while n not in hash: 
            hash.add(n)
            n = self.getSumSquares(n)

            if n == 1: 
                return True 

        return False 


    def getSumSquares(self, n): 
        # TODO: get sum of squares 
        output = 0 

        while n: 
            digit = n%10
            digit = digit ** 2
            output +=digit
            n = n // 10

        return output



            # cyclical numbers will run forever and will continue to loop. 
            # non cyclical numbers will not loop 
            # we can use a set to check if we have already seen the number or not, if we already have, then we can return False at that point, as it is cyclical. 
            # but 1 should be an exception as if we see 1, then we should return True 
            # if i !=1 and in hash: return True 


        