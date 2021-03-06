""" leetcode 153 - Find minimum in a rotated array

    Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
    Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in
    the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
    Given the sorted rotated array nums of unique elements, return the minimum element of this array.
"""
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        min_val = nums[0]

        while left <= right:
            mid = (left + right) // 2
            if min_val > nums[mid]:
                min_val = nums[mid]
                right = mid + 1
            else:
                left = mid + 1

        return min_val