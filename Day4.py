'''
Day 4

Project: Remove duplicates from array test problem
Description:
Given a sorted array, nums, remove the duplicates in-place such that each element appears only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],
Output = 2
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],
Output = 5
It doesn't matter what values are set beyond the returned length.
'''


def remove_duplicates_sorted(array):
  curr_idx = 0
  next_pos = 1

  # I guess there's no need to set up for edge cases
  #   they're handled with the while loop
  # while ((array[curr_idx] == array[next_pos]) and (next_pos < len(array))):
  #   next_pos+=1
  
  while (next_pos < len(array)):
    if (array[curr_idx] != array[next_pos]):
      array[curr_idx+1] = array[next_pos]
      curr_idx+=1
    else:
      next_pos+=1
  return curr_idx+1

print(remove_duplicates_sorted([0,0,1,1,1,2,2,3,3,4]))
print(remove_duplicates_sorted([1,1]))
print(remove_duplicates_sorted([]))