#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        head = root
        if not head: return head

        while root:
            p2 = root
            if root.left:
                p1 = root.left
                root.left = None
                while root.right:
                    root = root.right

                root.right = p1
            
            root = p2.right
        
        while head:
            print(head.val)
            head = head.right
        return head
# @lc code=end

