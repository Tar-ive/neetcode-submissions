from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        a = Counter(nums).most_common(k)
        for n in a: 
            res.append(n[0])
        return res