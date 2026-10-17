from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left_bound, right_bound):
            if not node:
                return True

            if not (left_bound < node.val < right_bound):
                return False

            return valid(node.left, left_bound, node.val) and valid(
                node.right, node.val, right_bound
            )

        return valid(root, float("-inf"), float("inf"))