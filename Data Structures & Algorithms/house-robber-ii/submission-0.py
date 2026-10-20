class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def robLinear(houses: list[int]) -> int:
            prev2, prev1 = 0, 0
            for money in houses:
                curr = max(prev1, prev2 + money)
                prev2 = prev1
                prev1 = curr
            return prev1

        return max(robLinear(nums[:-1]), robLinear(nums[1:]))