from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce
import string
true = True
false = False
#
# @lc app=leetcode id=946 lang=python3
#
# [946] Validate Stack Sequences
#
# https://leetcode.com/problems/validate-stack-sequences/description/
#
# algorithms
# Medium (58.54%)
# Total Accepted:    22.1K
# Total Submissions: 37.8K
# Testcase Example:  '[1,2,3,4,5]\n[4,5,3,2,1]'
#
# Given two sequences pushed and popped with distinct values, return true if
# and only if this could have been the result of a sequence of push and pop
# operations on an initially empty stack.
#
#
#
#
# Example 1:
#
#
# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# Output: true
# Explanation: We might do the following sequence:
# push(1), push(2), push(3), push(4), pop() -> 4,
# push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
#
#
#
# Example 2:
#
#
# Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# Output: false
# Explanation: 1 cannot be popped before 2.
#
#
#
#
# Note:
#
#
# 0 <= pushed.length == popped.length <= 1000
# 0 <= pushed[i], popped[i] < 1000
# pushed is a permutation of popped.
# pushed and popped have distinct values.
#
#
#
#


class Solution:
    def validateStackSequences(self, u, o):
        i, st = 0, deque()
        for n in u:
            st.append(n)
            while st and st[-1] == o[i]:
                st.pop()
                i += 1
        return not st 


sol = Solution()
u, o = [1, 2, 3, 4, 5], [4, 3, 5, 1, 2]
# u, o = [1, 2, 3, 4, 5], [4, 5, 3, 2, 1]
u, o = [0, 2, 1], [0, 1, 2]
print(sol.validateStackSequences(u, o))
