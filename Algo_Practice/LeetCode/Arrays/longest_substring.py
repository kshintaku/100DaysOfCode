"""
longest substring

Project: Longest Substring Without Repeating Characters
Description:
Given a string s, find the length of the longest substring without
repeating characters.


Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a
subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


def longest_substring(input_str):
    pointer_one, pointer_two = 0, 0
    length = 0
    while pointer_two < len(input_str) - 1:
        pointer_two += 1
        if input_str[pointer_one] == input_str[pointer_two]:
            return length + 1
        else:
            length += 1
    return length


print(longest_substring("abcabcbb"), "exptected: {}".format(3))
print("{} expected: {}".format(longest_substring("bbbbb"), 1))
print("{} expected: {}".format(longest_substring("pwwkew"), 3))
print("{} expected: {}".format(longest_substring(""), 0))
