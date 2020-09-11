'''
Day 2

Project: Two Sum test problem
Description:
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number. The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Notes:
Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.

Example:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
'''

def two_sum(array, sum):
  for idx, val in enumerate(array):
    print(idx, val)
    # This way got sidetracked and I realized there was a better way


# Holup
# I probably don't even need a for loop since I'm going from front and back
def two_sum_revised(array, sum):
  start = 0
  end = len(array)-1
  while (start < end):
    if array[start]+array[end] == sum:
      return [start+1, end+1]
    elif array[start]+array[end] < sum:
      start+=1
    else:
      end-=1


print(two_sum_revised([2,7,11,15], 9))
# two_sum([2,7,11,15], 9)