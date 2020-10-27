from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right 
from functools import reduce, lru_cache 
from typing import List 
import itertools 
import math 
import heapq 
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=1446 lang=python3
#
# [1446] Consecutive Characters
#
# https://leetcode.com/problems/consecutive-characters/description/
#
# algorithms
# Easy (63.43%)
# Total Accepted:    6.4K
# Total Submissions: 10.1K
# Testcase Example:  '"leetcode"'
#
# Given a string s, the power of the string is the maximum length of a
# non-empty substring that contains only one unique character.
# 
# Return the power of the string.
# 
# 
# Example 1:
# 
# 
# Input: s = "leetcode"
# Output: 2
# Explanation: The substring "ee" is of length 2 with the character 'e' only.
# 
# 
# Example 2:
# 
# 
# Input: s = "abbcccddddeeeeedcba"
# Output: 5
# Explanation: The substring "eeeee" is of length 5 with the character 'e'
# only.
# 
# 
# Example 3:
# 
# 
# Input: s = "triplepillooooow"
# Output: 5
# 
# 
# Example 4:
# 
# 
# Input: s = "hooraaaaaaaaaaay"
# Output: 11
# 
# 
# Example 5:
# 
# 
# Input: s = "tourist"
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 500
# s contains only lowercase English letters.
# 
#
class Solution:
    def maxPower(self, s: str) -> int:
        return max(len(list(v)) for _, v in itertools.groupby(s))
        
# s = "aaabbbcaabbc"
# print([len(list(g)) for _, g in (itertools.groupby(s))])

# sol = Solution()
# print(sol.maxPower(s))

