import gc

class Solution:
    def hammingWeight(self, n: int) -> int:
        gc.disable()
        
        count = 0
        while n:
            n &= n - 1
            count += 1
            
        return count