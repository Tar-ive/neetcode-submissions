class Solution:
    def countSubstrings(self, s: str) -> int:

        # is palindrome helper function
        #for each substring check that. 

        # this would be the brute force approach leading to O(n^3)

        # a more optimized solution is using dp table, or using 2 pointers 

        # res = 0 
        # for i in range(len(s)): 
        #     l,r=i,i
        #     while l >=0 and r < len(s) and s[l] == s[r]: 
        #         res +=1 
        #         l-=1 
        #         r+=1

        # for i in range(len(s)): 
        #     l,r = i, i+1
        #     while l >=0 and r < len(s) and s[l] == s[r]: 
        #         res+=1 
        #         l-=1 
        #         r+=1 

        # as all of this goes into helper function 

    #     res = 0 
    #     for i in range(len(s)): 
    #         res += self.countPali(s, i, i) # odd cases 
    #         res += self.countPali(s, i, i+1) # even cases 
    #     return res 

    # def countPali(self, s, l, r): 
    #     res = 0 
    #     while l >=0 and r < len(s) and s[l] == s[r]: 
    #         res+=1 
    #         l-=1 
    #         r+=1

    #     return res       


    # an even optimized solution is presented by using manachars algorithm where we can solve the problem in O(n) time. 
        def manacher(s): 
            t= "#" + "#".join(s) + "#"
            n = len(t)
            p = [0] * n 
            l,r = 0, 0 
            for i in range(n): 
                p[i] = min(r - i, p[l + (r - i)]) if i < r else 0 
                while (i + p[i] + 1 < n and i - p[i] -1 >= 0 
                        and t[i + p[i] + 1] == t[i - p[i] -1]): 
                    p[i] += 1
                if i + p[i] > r: 
                    l,r = i - p[i], i + p[i]
            return p 

        p = manacher(s)
        res = 0 
        for i in p: 
            res += (i+1) // 2 # as we are doing t for even ones. 
        return res 
