class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_prime = '#' + "#".join(s) + "#"
        # length of palindrome from center to end 
        radii = [0 for _ in range(len(s_prime))]
        center = 0 
        right_border = 0 
        max_radius = 0 
        largest_palindrome_center = 0 

        for i in range(len(s_prime)): 
            mirror = center - (i-center)

            # if center exists within larger palindrome 
            if i < right_border: 
                # if mirror does NOT extend beyond p@center 
                if radii[mirror] <right_border - i: 
                    radii[i] = radii[mirror]
                    continue
                #if mirror extend beyond p@center
                else: 
                    radii[i] = right_border - i 
            
            #If s_prine is NOT in larger palindrome, radii = 0, explore from scratch 
            while (
                i - 1 - radii[i] >= 0
                    and i+1 + radii[i] < len(s_prime)
                    and s_prime[i-1-radii[i]] == s_prime[i+1+radii[i]]
                    ): 
                radii[i]+=1

                #if palindrome centered at "i" extends beyond center 
                if i + radii[i] >right_border: 
                    #reset center and right_border to "i" and "i + radii[i]" as curr palindrom reaches farther to the right 
                    center = i 
                    right_border = i + radii[i]

            if radii[i] > max_radius: 
                max_radius = radii[i]
                largest_palindrome_center = i 

        start_index = (largest_palindrome_center - max_radius) // 2
        return s[start_index : start_index + max_radius]