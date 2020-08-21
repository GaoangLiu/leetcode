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
# @lc app=leetcode id=915 lang=python3
#
# [915] Partition Array into Disjoint Intervals
#
# https://leetcode.com/problems/partition-array-into-disjoint-intervals/description/
#
# algorithms
# Medium (44.91%)
# Total Accepted:    18.5K
# Total Submissions: 41.2K
# Testcase Example:  '[5,0,3,8,6]'
#
# Given an array A, partition it into two (contiguous) subarrays left and right
# so that:
#
#
# Every element in left is less than or equal to every element in right.
# left and right are non-empty.
# left has the smallest possible size.
#
#
# Return the length of left after such a partitioning.  It is guaranteed that
# such a partitioning exists.
#
#
#
# Example 1:
#
#
# Input: [5,0,3,8,6]
# Output: 3
# Explanation: left = [5,0,3], right = [8,6]
#
#
#
# Example 2:
#
#
# Input: [1,1,1,0,6,12]
# Output: 4
# Explanation: left = [1,1,1,0], right = [6,12]
#
#
#
#
#
# Note:
#
#
# 2 <= A.length <= 30000
# 0 <= A[i] <= 10^6
# It is guaranteed there is at least one way to partition A as described.
#
#
#
#
#
#
#


class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        pre_max = all_max = A[0]
        pos = 1
        for i, v in enumerate(A):
            if v < pre_max:
                pre_max = all_max
                pos = i + 1
            elif v > all_max:
                all_max = v 
        return pos 
        
sol = Solution()
A = [5, 0, 3, 8, 6]
A = [1, 1, 1, 0, 6, 12]
print(sol.partitionDisjoint(A))
