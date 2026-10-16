class Solution:

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)

        # Pass 1: Compute prefix products (product of elements to the left)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # Pass 2: Multiply by postfix products (product of elements to the right)
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res