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
MIN, MAX, MOD = -0x3f3f3f3f, 0x3f3f3f3f, 1000000007
#
# @lc app=leetcode id=1525 lang=python3
#
# [1525] Number of Good Ways to Split a String
#
# https://leetcode.com/problems/number-of-good-ways-to-split-a-string/description/
#
# algorithms
# Medium (68.08%)
# Total Accepted:    4.2K
# Total Submissions: 6.2K
# Testcase Example:  '"aacaba"'
#
# You are given a string s, a split is called good if you can split s into 2
# non-empty strings p and q where its concatenation is equal to s and the
# number of distinct letters in p and q are the same.
#
# Return the number of good splits you can make in s.
#
#
# Example 1:
#
#
# Input: s = "aacaba"
# Output: 2
# Explanation: There are 5 ways to split "aacaba" and 2 of them are good.
# ("a", "acaba") Left string and right string contains 1 and 3 different
# letters respectively.
# ("aa", "caba") Left string and right string contains 1 and 3 different
# letters respectively.
# ("aac", "aba") Left string and right string contains 2 and 2 different
# letters respectively (good split).
# ("aaca", "ba") Left string and right string contains 2 and 2 different
# letters respectively (good split).
# ("aacab", "a") Left string and right string contains 3 and 1 different
# letters respectively.
#
#
# Example 2:
#
#
# Input: s = "abcd"
# Output: 1
# Explanation: Split the string as follows ("ab", "cd").
#
#
# Example 3:
#
#
# Input: s = "aaaaa"
# Output: 4
# Explanation: All possible splits are good.
#
# Example 4:
#
#
# Input: s = "acbadbaada"
# Output: 2
#
#
#
# Constraints:
#
#
# s contains only lowercase English letters.
# 1 <= s.length <= 10^5
#
#


class Solution:
    def numSplits(self, s: str) -> int:
        left, right, ans = defaultdict(int), Counter(s), 0
        for c in s:
            left[c] += 1
            right[c] -= 1
            if not right[c]:
                del right[c]
            if len(left) == len(right):
                ans += 1
            elif len(left) > len(right):
                return ans
        return ans


sol = Solution()

s = "aacaba"
# s = "abcd"
# s = "aaaaa"
# s = "acbadbaada"
print(sol.numSplits(s))
