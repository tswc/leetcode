#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.recureIsValidBST(root, float("-inf"), float("inf"))
        

    def recureIsValidBST(self, root_node, min_val, max_val):

        if root_node is None:
            return True
        if min_val < root_node.val < max_val:
            return self.recureIsValidBST(root_node.left, min_val, root_node.val) and self.recureIsValidBST(root_node.right, root_node.val, max_val)
        else:
            return False
# @lc code=end

