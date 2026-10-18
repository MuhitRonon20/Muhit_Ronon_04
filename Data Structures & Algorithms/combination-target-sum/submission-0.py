from typing import List


class Solution:

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(
            start_idx: int, current_target: int, path: List[int]
        ) -> None:
            if current_target == 0:
                res.append(path[:])
                return

            for i in range(start_idx, len(nums)):
                if nums[i] > current_target:
                    break

                path.append(nums[i])
                backtrack(i, current_target - nums[i], path)
                path.pop()

        backtrack(0, target, [])
        return res