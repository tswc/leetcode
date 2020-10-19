#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """


        stack = []

        pre_node = None

        error_node1 = None
        error_node2 = None

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            
            curr_node = stack.pop(0)
            if pre_node is None:
                pre_node = curr_node
            else:
                
            root = curr_node.right

        
# @lc code=end

