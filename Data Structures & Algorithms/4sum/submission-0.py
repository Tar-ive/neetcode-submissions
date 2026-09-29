class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # this sounds like the same as 3 sum, only in 3 sum, we had to sum to 0, here we have to sum to the target 
        # let me try solving 3 sum and instead of it summing to  0, will put it to sum to target. 
        # we will use a fixed pointer, and 2 pointers, coming in opposite directions for this solution. 
        # if summ > target: r -=1 
        # elif sum < target: l+=1 
        # if equal, we record to result array and then check for duplicate triplets using: 
        # while l < r and nums[l]== nums[l-1]: l+=1

        # but they want quadruplates. 


        nums.sort()
        result = []
        n = len(nums)

        for i in range(n): 
            #quick skipping of duplicates 
            if i > 0 and nums[i] == nums[i-1]: continue
            for j in range(i+1, n): 
                if j> i+1 and nums[j] == nums[j-1]: continue
            # pointer initialization 
                l,r = j+1, n-1
                while l < r: # as we dont want the pointers to be the same
                    summ = nums[i] + nums[l] + nums[r] + nums[j]
                    if summ > target: 
                        r-=1 
                    elif summ < target: 
                        l+=1 
                    else: 
                        result.append([nums[i], nums[l], nums[r], nums[j]])
                        l+=1 
                        while l < r and nums[l] == nums[l-1]: 
                            l +=1 
        return result


        