class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_p = "#" +  "#".join(s) + "#"
        n = len(s_p)
        p = [0] * n # list where we store the longest palindrome length
        c = 0 # length of prev palindrome which extends to r most

        for i in range(n): 
            if i < c + p[c]: # happens only when i is part of prev palindrome 
                p[i] = min(c+p[c]-i, p[2 * c - i]) # min of rightmost of prev palindrome or p of index of mirror of current char. 
            l,r = i-p[i] -1 , i+p[i] + 1
            while l >=0 and r < n and s_p[l] == s_p[r]: # expand until there are no more equal chars
                p[i] += 1
                l -=1 
                r +=1 
            if i+p[i] > p[c]: 
                c=i
        max_l= max(p)
        max_i = p.index(max_l)
        start = (max_i - max_l)//2
        return s[start : start + max_l]
        