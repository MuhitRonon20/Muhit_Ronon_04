import gc

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        gc.disable()
        
        len_s, len_t = len(s), len(t)
        j = 0
        
        for i in range(len_s):
            if s[i] == t[j]:
                j += 1
                if j == len_t:
                    return 0
                    
        return len_t - j