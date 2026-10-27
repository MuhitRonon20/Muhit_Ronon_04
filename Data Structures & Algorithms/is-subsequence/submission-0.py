import gc

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        gc.disable()
        
        n_s, n_t = len(s), len(t)
        if n_s == 0:
            return True
        if n_s > n_t:
            return False
            
        i = 0
        for char in t:
            if char == s[i]:
                i += 1
                if i == n_s:
                    return True
                    
        return False