#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int):
        if n == 0:
            return []
        ans = self.get_final_list(1, n)
        return ans

    def get_final_list(self, start, end):
        tree_list = []
        if start > end:
            return [None, ]
        
        for root in range(start, end+1):
            left = root - start
            right = end - root

            # print(left, right)

            left_tree = self.get_final_list(start, root-1)

            right_tree = self.get_final_list(root+1, end)


            for l_tree in left_tree:
                for r_tree in right_tree:
                    currTree = TreeNode(val=root, left=l_tree, right=r_tree)
                    tree_list.append(currTree)
        
        return tree_list


# @lc code=end

