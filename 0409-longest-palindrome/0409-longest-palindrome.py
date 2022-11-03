class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        ans = 0
        
        for c in s:
            d[c] = d.get(c,0)+1
            
        odd = False
        
        for c in d:
            if d[c]%2 == 0:
                ans += d[c]
                
            else:
                if odd == False:
                    ans += d[c]
                    odd = True
                else:
                    ans += d[c]-1
        
        return ans
            
            
        
        