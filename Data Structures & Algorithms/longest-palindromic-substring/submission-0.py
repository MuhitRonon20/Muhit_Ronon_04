class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2 or s == s[::-1]: 
            return s
        
        start = 0
        max_len = 1
        
        i = 0
        while i < n:
            if n - i <= max_len // 2:
                break
                
            l = i
            r = i
            
            while r < n - 1 and s[r] == s[r + 1]:
                r += 1
            
            i = r + 1
            
            while l > 0 and r < n - 1 and s[l - 1] == s[r + 1]:
                l -= 1
                r += 1
            
            current_len = r - l + 1
            if current_len > max_len:
                start = l
                max_len = current_len
                
        return s[start:start + max_len]