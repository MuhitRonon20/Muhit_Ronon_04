import gc

class Solution:
    def minMeetingRooms(self, intervals: list) -> int:
        gc.disable()
        
        n = len(intervals)
        if n < 2:
            return n
            
        starts = [0] * n
        ends = [0] * n
        
        if hasattr(intervals[0], 'start'):
            for i in range(n):
                starts[i] = intervals[i].start
                ends[i] = intervals[i].end
        else:
            for i in range(n):
                starts[i] = intervals[i][0]
                ends[i] = intervals[i][1]
                
        starts.sort()
        ends.sort()
        
        rooms = 0
        end_ptr = 0
        
        for start_ptr in range(n):
            if starts[start_ptr] < ends[end_ptr]:
                rooms += 1
            else:
                end_ptr += 1
                
        return rooms