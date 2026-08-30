class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # similar to 2 sum 2 but target should be 0. 

        #k can be the iterator (based on 1 to len(nums))

        # need to sort first. 

        # we also need to deal with duplicate triplets 
        # l,r = 0, len(nums) -1 
        # n_nums = sorted(nums)
        # result = []
        # for k in n_nums: 
        #     while l < r: 
        #         sum = n_nums[l] + n_nums[r] + n_nums[k]
        #         if sum < 0: 
        #             l +=1
        #         elif sum > 0: 
        #             r-=1 
        #         else: 
        #             result.append([n_nums[l], n_nums[r] ,n_nums[k]])
        #             l+=1
        #             r-=1

        # return result

        result = []
        nums.sort()
        for i, v in enumerate(nums): 
            if i > 0 and nums[i-1] == nums[i]: 
                continue # early check for duplicates. 

            l,r = i+1, len(nums) -1 
            while l <r: 
                sum = nums[i] + nums[l] + nums[r]
                if sum > 0: 
                    r-=1 
                elif sum < 0: 
                    l +=1 
                else: 
                    result.append([nums[i], nums[l], nums[r]])
                    l+=1 
                    while l<r and nums[l] == nums[l-1]: 
                        l+=1 
        return result


        