from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")

        def max_gain(node: Optional[TreeNode]) -> int:
            nonlocal max_sum
            if not node:
                return 0

            # Max sum on the left and right subtrees; ignore negative contributions
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # Path sum passing through the current node as the highest ancestor (split point)
            current_path_sum = node.val + left_gain + right_gain

            # Update global maximum path sum
            max_sum = max(max_sum, current_path_sum)

            # Return max gain the parent node can obtain by extending a single branch
            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return max_sum