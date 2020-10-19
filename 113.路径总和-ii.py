#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum1: int) -> List[List[int]]:
        if not root: return []
        path = []
        res = []
        def get_sum(root, sum1, path):
            path.append(root.val)
            if not root.left and not root.right:
                # print(path, sum1)

                if sum(path) == sum1:
                    res.append(list(path))
            if root.left:
                get_sum(root.left, sum1, path)
                path.pop()
            if root.right:
                get_sum(root.right, sum1, path)
                path.pop()
        get_sum(root, sum1, path)
        return res
# @lc code=end

