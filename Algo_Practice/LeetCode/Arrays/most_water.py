"""
# 11 Container with Most Water
Difficulty: Medium
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

 



The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

 

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""


class Solution:
    def maxArea(self, height):
        curr_max = 0
        left_side = 0
        right_side = len(height) - 1

        while left_side != right_side:
            if curr_max < min(height[left_side], height[right_side]) * (
                right_side - left_side
            ):
                curr_max = min(height[left_side], height[right_side]) * (
                    right_side - left_side
                )
            if height[left_side] < height[right_side]:
                left_side += 1
            else:
                right_side -= 1
        return curr_max


sol = Solution()
print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), ": expected 49")
