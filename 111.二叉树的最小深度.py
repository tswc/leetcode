#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0

        stack = [root]
        res = 0
        while stack:
            res = res + 1
            curr_len = len(stack)
            for i in range(curr_len):
                curr_node = stack.pop(0)
                if curr_node.left: stack.append(curr_node.left)
                if curr_node.right: stack.append(curr_node.right)

                if not curr_node.left and not curr_node.right:
                    return res 
        
# @lc code=end

