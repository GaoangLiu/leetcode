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
# @lc app=leetcode id=284 lang=python3
#
# [284] Peeking Iterator
#
# https://leetcode.com/problems/peeking-iterator/description/
#
# algorithms
# Medium (45.65%)
# Total Accepted:    101.1K
# Total Submissions: 221.2K
# Testcase Example:  '["PeekingIterator","next","peek","next","next","hasNext"]\n' +
#   '[[[1,2,3]],[],[],[],[],[]]'
#
# Given an Iterator class interface with methods: next() and hasNext(), design
# and implement a PeekingIterator that support the peek() operation -- it
# essentially peek() at the element that will be returned by the next call to
# next().
#
# Example:
#
#
# Assume that the iterator is initialized to the beginning of the list:
# [1,2,3].
#
# Call next() gets you 1, the first element in the list.
# Now you call peek() and it returns 2, the next element. Calling next() after
# that still return 2.
# You call next() the final time and it returns 3, the last element.
# Calling hasNext() after that should return false.
#
#
# Follow up: How would you extend your design to be generic and work with all
# types, not just integer?
#
#
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.it = iterator
        self.nx = self.it.next() if self.it.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.nx

    def next(self):
        """
        :rtype: int
        """
        res = self.nx
        self.nx = self.it.next() if self.it.hasNext() else None
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.nx is not None


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
