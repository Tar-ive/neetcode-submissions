class Solution:
    def firstUniqChar(self, s: str) -> int:
        # if not keep 
        # push elements to a queue, if not seen till end of string, a character, pop the character.
        # traverse the whole string.
        # could use a set 

        # need to preserve index of characters. 
        # keep adding from right, if we see a repeating character, pop from left, once we have finished traversing through the array result will be popleft()
        count = collections.Counter(s)
        queue = collections.deque()
        # only add uni
        for index, char in enumerate(s):
            if count[char] == 1: 
                queue.append(index)
        
        # cleanup front of the queue to find first valid unique element 
        # while queue and count[s[queue[0]]]> 1: 
        #     queue.popleft()
        
        return queue[0] if queue else -1
            

        