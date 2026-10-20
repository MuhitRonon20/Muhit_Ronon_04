class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = cur_max = cur_min = nums[0]
        
        for n in nums[1:]:
            if n < 0:
                cur_max, cur_min = cur_min, cur_max
                
            cur_max = n if n > cur_max * n else cur_max * n
            cur_min = n if n < cur_min * n else cur_min * n
            
            if cur_max > res:
                res = cur_max
                
        return res