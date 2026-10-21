class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0
        n = len(nums)
        
        for i in range(n):
            if i > max_reach:
                return False  
            
            reach = i + nums[i]
            if reach > max_reach:
                max_reach = reach
                
            if max_reach >= n - 1:
                return True  
                
        return True