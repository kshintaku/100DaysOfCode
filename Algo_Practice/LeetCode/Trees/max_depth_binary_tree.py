'''
# 104 Maximum Depth of Binary Tree
Difficulty: Easy
https://leetcode.com/problems/maximum-depth-of-binary-tree/
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        if root:
            storage = [root]
        else:
            return 0
        storage = [root]
        while storage:
            new_stack = []
            for x in storage:
                if x.left:
                    new_stack.append(x.left)
                if x.right:
                    new_stack.append(x.right)
            depth += 1
            storage = new_stack
        return depth
