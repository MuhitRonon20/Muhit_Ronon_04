import gc

class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        gc.disable()
        
        max_so_far = -1
        for i in range(len(arr) - 1, -1, -1):
            val = arr[i]
            arr[i] = max_so_far
            if val > max_so_far:
                max_so_far = val
                
        return arr