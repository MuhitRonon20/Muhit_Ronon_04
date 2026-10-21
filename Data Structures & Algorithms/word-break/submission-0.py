class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        words = set(wordDict)
        min_len = min(len(w) for w in words)
        max_len = max(len(w) for w in words)
        
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  
        
        for i in range(1, n + 1):
            for l in range(min_len, min(i, max_len) + 1):
                if dp[i - l] and s[i - l:i] in words:
                    dp[i] = True
                    break  
                    
        return dp[n]