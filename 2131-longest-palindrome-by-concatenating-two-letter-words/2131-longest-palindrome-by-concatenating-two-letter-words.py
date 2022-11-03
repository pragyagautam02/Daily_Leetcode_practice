class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        def isPalindrome(word):
            return (''.join(list(reversed(word)))) == word
        
        
        d = {}
        ans = 0
        flag = False
        
        for word in words:
            d[word] = d.get(word,0)+1
        
        for word in d:
            revWord = (''.join(list(reversed(word))))
            if isPalindrome(word):
                if d[word]%2 == 0:
                    ans += len(word)*d[word]
                else:
                    if flag == True:
                        ans += (len(word)*(d[word] - 1))
                    else:
                        ans += len(word)*d[word]
                        flag = True
                        
            
            elif revWord in d:
                ans += len(word)*min(d[word], d[revWord])
        
        return ans
                    
                    