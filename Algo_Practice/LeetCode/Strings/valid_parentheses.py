'''
# 20 Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''


class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        if len(s) % 2 == 1:
            return False
        for x in s:
            if x in ['(', '[', '{']:
                my_stack.append(x)
            elif x in [')', ']', '}'] and len(my_stack) > 0:
                if x == ')':
                    if my_stack[-1] == '(':
                        my_stack.pop()
                    else:
                        return False
                elif x == ']':
                    if my_stack[-1] == '[':
                        my_stack.pop()
                    else:
                        return False
                elif x == '}':
                    if my_stack[-1] == '{':
                        my_stack.pop()
                    else:
                        return False
            else:
                return False
        if len(my_stack) > 0:
            return False
        return True


sol = Solution()
print(sol.isValid('()'))
print(sol.isValid('()[]{}'))
print(sol.isValid('(]'))
print(sol.isValid('([)]'))
print(sol.isValid('{[]}'))
