"""
# 15 3sum
Difficulty: Medium
Given an array nums of n integers, are there elements a, b, c in nums
such that a + b + c = 0? Find all unique triplets in the array
which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []


Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105

Notes:
Very similar to 2sum problem. Instead of setting sum to zero,
set the sum/target to 3rd variable
To avoid duplicate combinations, must keep iterating until non duplicate
is found for first two pointers
One coveat is that the array has to be in sorted order to remove
duplicates this way
"""


class Solution:
    def threeSum(self, nums):
        nums.sort()
        N, result = len(nums), []
        for i in range(N):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = nums[i] * -1
            s, e = i + 1, N - 1
            while s < e:
                if nums[s] + nums[e] == target:
                    result.append([nums[i], nums[s], nums[e]])
                    s = s + 1
                    while s < e and nums[s] == nums[s - 1]:
                        s = s + 1
                elif nums[s] + nums[e] < target:
                    s = s + 1
                else:
                    e = e - 1
        return result
