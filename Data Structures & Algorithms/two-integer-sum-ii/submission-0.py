class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1 

        # check if diff is bigger or smaller, if bigger, then shift left pointer towards right, if smaller, shift right pointer towards left. 
            # but bigger than what? - maybe negative positive. 
        while l < r: 
            diff = target - (numbers[l] + numbers [r])
            if diff < 0: 
                r-=1
            elif diff > 0: 
                l+=1
            else: 
                return [l+1, r+1]
        