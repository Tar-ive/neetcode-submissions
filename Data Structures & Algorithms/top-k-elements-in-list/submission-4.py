
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for n in range(len(nums)+ 1)] # creates empty lists called buckets for bucket sort. 

        for n in nums: # populating a frequency map in python. 
            count[n] = 1 + count.get(n,0)
        
        for n, c in count.items():  # bucketing from bucket sort 
            freq[c].append(n)
            
        res = [] # initialize result array 

        for i in range(len(freq) -1, 0, -1): # looping from the end 
            for n in freq[i]: 
                res.append(n)
                if len(res) == k: 
                    return res


