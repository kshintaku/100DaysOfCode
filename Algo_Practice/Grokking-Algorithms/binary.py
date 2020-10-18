'''
Working on Chapter 1 problems from book
'''

'''
Exercises:
1.1 - Suppose you have a sorted list of 128 names, and you're searching through it using binary search. What's the maximum number of steps it should take?

log2(128)
128 -> 64 -> 32 -> 16 -> 8 -> 4 -> 2 -> 1
7 steps

1.2 - Suppose you double the size of the list. What's the maximum number of steps now?
256 -> 128 -> 64 -> 32 -> 16 -> 8 -> 4 -> 2 -> 1
8 steps, only 1 more step than before

1.3 - You have a name, and you want to find the person's phone number in the phone book.
O(log n) - Binary search

1.4 - You have a phone number, and you want to find the person's name in the phone book. (Hint: You'll have to search through the whole book!)
O(n) - simple search, all options

1.5 - You want to read the numbers of every person in the phone book.
O(n) - simple search, going through every item

1.6 - You want to read the numbers of just the As. (This is a tricky one! It involves conveps that are covered more in chapter 4. Read the answer - you may be surprised!)
O(n) - simple search, going through every A; constants don't matter
'''
