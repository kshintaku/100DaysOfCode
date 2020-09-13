'''
Day 5

Project: Sort Colors
Description:
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Follow up:

Could you solve this problem without using the library's sort function?
Could you come up with a one-pass algorithm using only O(1) constant space?

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Example 3:
Input: nums = [0]
Output: [0]
'''

# Edge cases: null, empty array, out of bounds


def sort_colors(array):
  red = white = 0
  blue = len(array)-1

  while(white <= blue):
    if array[white] == 0:
      array[red], array[white] = array[white], array[red]
      red += 1
      white += 1
    elif array[white] == 2:
      array[white], array[blue] = array[blue], array[white]
      blue -= 1
    else:
      white += 1
  return array
  # ans = []

  # horrible solution, takes too long and uses too much memory
  # for x in array:
  #   if x == 0:
  #     ans.append(x)
  # for x in array:
  #   if x == 1:
  #     ans.append(x)
  # for x in array:
  #   if x == 2:
  #     ans.append(x)

  # for idx, elem in enumerate(array):
  #   if elem == 0:
  #     if red != -1:
  #       array[red], array[idx] = array[idx], array[red]
  #     elif red == -1:
  #       red = idx
  #   if elem == 1:
  #     if white != -1:
  #       array[white], array[idx] = array[idx], array[white]
  #     else:
  #       white = idx
  #   if elem == 2:
  #     if blue != -1:
  #       array[blue], array[idx] = array[idx], array[blue]
  #     else:
  #       blue = idx

  n = len(array)

  # Bubble sort
  # for i in range(n-1):
  #   for j in range(0, n-i-1):
  #     if array[j] > array[j+1] :
  #           array[j], array[j+1] = array[j+1], array[j]


def partition(arr, low, high):
  i = (low-1)         # index of smaller element
  pivot = arr[high]     # pivot

  for j in range(low, high):

    # If current element is smaller than or
    # equal to pivot
    if arr[j] <= pivot:

      # increment index of smaller element
      i = i+1
      arr[i], arr[j] = arr[j], arr[i]

  arr[i+1], arr[high] = arr[high], arr[i+1]
  return (i+1)

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort


def quickSort(arr, low, high):
  if len(arr) == 1:
    return arr
  if low < high:

    # pi is partitioning index, arr[p] is now
    # at right place
    pi = partition(arr, low, high)

    # Separately sort elements before
    # partition and after partition
    quickSort(arr, low, pi-1)
    quickSort(arr, pi+1, high)
  return array

print(sort_colors([2,0,2,1,1,0]), '[0,0,1,1,2,2]')
print(sort_colors([2,0,1]), '[0,1,2]')
print(sort_colors([0]), '[0]')

# 2
# 2 0 -> 0 2
# 0 2 2
# 0 2 2 1
