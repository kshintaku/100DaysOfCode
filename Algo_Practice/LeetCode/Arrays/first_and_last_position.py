'''
# 34 Find First and Last Position of Element in Sorted Array
Difficulty: Medium
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
'''


class Solution:
    # working from front to back and stopping when the pointers pass each other or reach the target
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        if len(nums) <1:
            return ans
        first = 0
        last = len(nums)-1

        while nums[first] != target or nums[last] != target:
            if nums[first] < target:
                first += 1
            if nums[last] > target:
                last -= 1
            if last < first:
                return [-1, -1]
        return [first, last]
