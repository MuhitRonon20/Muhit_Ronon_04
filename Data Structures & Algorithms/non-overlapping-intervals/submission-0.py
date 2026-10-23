import gc

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        gc.disable()
        
        # Sort by end time
        intervals.sort(key=lambda x: x[1])
        
        removed_count = 0
        prev_end = float('-inf')
        
        for start, end in intervals:
            if start >= prev_end:
                prev_end = end
            else:
                removed_count += 1
                
        return removed_count