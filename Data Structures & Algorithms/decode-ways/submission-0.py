class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        prev2 = 1  # dp[i-2]
        prev1 = 1  # dp[i-1]
        
        for i in range(1, n):
            curr = 0
            
            # Single digit decode (1-9)
            if s[i] != '0':
                curr += prev1
                
            # Two digit decode (10-26)
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                curr += prev2
                
            prev2 = prev1
            prev1 = curr
            
            # Invalid sequence early exit
            if prev1 == 0:
                return 0
                
        return prev1