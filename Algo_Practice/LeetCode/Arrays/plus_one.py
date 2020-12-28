'''
# 66 Plus One
Difficulty: Easy
https://leetcode.com/problems/plus-one/


Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Example 3:

Input: digits = [0]
Output: [1]
 

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
'''


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        digits[-1] += 1
        sol = []
        for item in digits[::-1]:
            if item + carry > 9:
                sol.append((item + carry) % 10)
                carry = 1
            else:
                sol.append(item + carry)
                carry = 0
        if carry == 1:
            sol.append(carry)
        return sol[::-1]
