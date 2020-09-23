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
# @lc app=leetcode id=1462 lang=python3
#
# [1462] Course Schedule IV
#
# https://leetcode.com/problems/course-schedule-iv/description/
#
# algorithms
# Medium (42.50%)
# Total Accepted:    11.2K
# Total Submissions: 26.3K
# Testcase Example:  '2\r\n[[1,0]]\r\n[[0,1],[1,0]]\r'
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
#
# Some courses may have direct prerequisites, for example, to take course 0 you
# have first to take course 1, which is expressed as a pair: [1,0]
#
# Given the total number of courses n, a list of direct prerequisite pairs and
# a list of queries pairs.
#
# You should answer for each queries[i] whether the course queries[i][0] is a
# prerequisite of the course queries[i][1] or not.
#
# Return a list of boolean, the answers to the given queries.
#
# Please note that if course a is a prerequisite of course b and course b is a
# prerequisite of course c, then, course a is a prerequisite of course c.
#
#
# Example 1:
#
#
# Input: n = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
# Output: [false,true]
# Explanation: course 0 is not a prerequisite of course 1 but the opposite is
# true.
#
#
# Example 2:
#
#
# Input: n = 2, prerequisites = [], queries = [[1,0],[0,1]]
# Output: [false,false]
# Explanation: There are no prerequisites and each course is independent.
#
#
# Example 3:
#
#
# Input: n = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
# Output: [true,true]
#
#
# Example 4:
#
#
# Input: n = 3, prerequisites = [[1,0],[2,0]], queries = [[0,1],[2,0]]
# Output: [false,true]
#
#
# Example 5:
#
#
# Input: n = 5, prerequisites = [[0,1],[1,2],[2,3],[3,4]], queries =
# [[0,4],[4,0],[1,3],[3,0]]
# Output: [true,false,true,false]
#
#
#
# Constraints:
#
#
# 2 <= n <= 100
# 0 <= prerequisite.length <= (n * (n - 1) / 2)
# 0 <= prerequisite[i][0], prerequisite[i][1] < n
# prerequisite[i][0] != prerequisite[i][1]
# The prerequisites graph has no cycles.
# The prerequisites graph has no repeated edges.
# 1 <= queries.length <= 10^4
# queries[i][0] != queries[i][1]
#
#
#
class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]],
                            queries: List[List[int]]) -> List[bool]:
        memo = [[-1] * n for _ in range(n)]
        pr = [[] for _ in range(n)]
        for p in prerequisites:
            a, b = p
            memo[a][b] = 1
            pr[b].append(a)

        def dfs(i, j):
            if memo[i][j] > -1:
                return memo[i][j]

            for c in pr[j]:
                if memo[i][c] == 1 or dfs(i, c):
                    memo[i][j] = 1
                    return True
            memo[i][j] = 0
            return False

        return [dfs(q[0], q[1]) for q in queries]


sol = Solution()

n, prerequisites, queries = 2, [[1, 0]], [[0, 1], [1, 0]]
n, prerequisites, queries = 2, [], [[1, 0], [0, 1]]
n, prerequisites, queries = 3, [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]]
n, prerequisites, queries = 3, [[1, 0], [2, 0]], [[0, 1], [2, 0]]
n, prerequisites, queries = 5, [[0, 1], [1, 2], [2, 3], [3,
                                                         4]], [[0, 4], [4, 0],
                                                               [1, 3], [3, 0]]
print(sol.checkIfPrerequisite(n, prerequisites, queries))
