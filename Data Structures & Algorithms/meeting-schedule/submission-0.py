import gc

class Solution:
    def canAttendMeetings(self, intervals: list) -> bool:
        gc.disable()
        
        if not intervals:
            return True
            
        if hasattr(intervals[0], 'start'):
            intervals.sort(key=lambda x: x.start)
            for i in range(1, len(intervals)):
                if intervals[i].start < intervals[i - 1].end:
                    return False
        else:
            intervals.sort(key=lambda x: x[0])
            for i in range(1, len(intervals)):
                if intervals[i][0] < intervals[i - 1][1]:
                    return False
                    
        return True