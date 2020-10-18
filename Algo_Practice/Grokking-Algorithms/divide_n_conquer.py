'''
Chapter 4 - Quicksort

Exercies:
4.1 - Write out the code for the earlier sum function
'''


def recursive_sum(arr):
    x = 0
    if len(arr) > 0:
        x = arr.pop()
        return x + recursive_sum(arr)
    else:
        return x


print('This is recursive sum: ', recursive_sum([1, 2, 3]))

'''
4.2 - Write a recursive function to count the number of items in a list
'''


def recursive_count(arr):
    if len(arr) > 0:
        arr.pop()
        return 1 + recursive_count(arr)
    else:
        return 0


print('This is recursive length: ', recursive_count([1, 2, 3, 4, 5, 6]))

'''
4.3 - Find the maximunm number in a list
'''


def recursive_max(arr):
    if len(arr) > 0:
        return max(arr.pop(), recursive_max(arr))
    else:
        return 0


print('This is recursive max: ', recursive_max([1, 2, 3, 4, 5, 7, 0, -1]))

'''
4.4 - Remember binary search from chapter 1? It's a divide-and-conquer algorithm, too. Can you come up with the base case and recursive case for binary search?

Base case would be item == search
recursive case would be, item is greater than current, return right, otherwise return left side
'''
