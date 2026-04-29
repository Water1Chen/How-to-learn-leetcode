"""
LC 34. Find First and Last Position of Element in Sorted Array (在排序数组中查找元素的第一个和最后一个位置)
Difficulty: Medium
Tags: Array, Binary Search
Link: https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/
Category: binary-search
"""

from typing import List


# ===== 暴力解法 =====
# 思路: Linear scan from left to right. Record first occurrence and last occurrence
#       by updating when we see the target. If never seen, return [-1, -1].
# 复杂度: O(n) time, O(1) space
def solution_brute(nums: List[int], target: int) -> List[int]:
    """
    Find first and last position of target using linear scan.
    """
    first: int = -1
    last: int = -1

    # WHY: Iterate through the array once
    for i in range(len(nums)):
        # WHY: Current element matches target
        if nums[i] == target:
            # WHY: If this is the first match, record it as the first position
            if first == -1:
                first = i
            # WHY: Always update last position to the most recent match
            last = i

    # WHY: Return [first, last]; both stay -1 if target never found
    return [first, last]


# ===== 最优解法 =====
# 思路: Two binary searches: first finds the leftmost occurrence (first position >= target),
#       second finds the rightmost occurrence (last position <= target).
#       Each binary search runs in O(log n) time.
# 复杂度: O(log n) time, O(1) space
def solution_optimal(nums: List[int], target: int) -> List[int]:
    """
    Find first and last position of target using two binary searches.
    """

    # WHY: Helper to find the leftmost index where nums[idx] >= target
    def find_left_bound() -> int:
        left: int = 0
        right: int = len(nums)
        # WHY: Standard left-boundary binary search [left, right)
        while left < right:
            mid: int = left + (right - left) // 2
            # WHY: If mid >= target, narrow right (target is in left half)
            if nums[mid] >= target:
                right = mid
            else:
                # WHY: Mid < target, so move past mid
                left = mid + 1
        return left

    # WHY: Helper to find the leftmost index where nums[idx] > target
    # WHY: Then rightmost occurrence of target = find_right_bound() - 1
    def find_right_bound() -> int:
        left: int = 0
        right: int = len(nums)
        # WHY: Standard left-boundary binary search for > target
        while left < right:
            mid: int = left + (right - left) // 2
            # WHY: If mid > target, narrow right
            if nums[mid] > target:
                right = mid
            else:
                # WHY: Mid <= target, so move past mid
                left = mid + 1
        return left

    # WHY: Find first position where nums[idx] >= target
    first: int = find_left_bound()
    # WHY: Find first position where nums[idx] > target
    last: int = find_right_bound() - 1

    # WHY: Validate: first must be within bounds and must equal target
    if first < len(nums) and nums[first] == target:
        return [first, last]

    # WHY: Target not found in the array
    return [-1, -1]


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Find First and Last Position...")

    # Test case 1: Standard case with multiple occurrences
    nums1 = [5, 7, 7, 8, 8, 10]
    assert solution_optimal(nums1, 8) == [3, 4], f"Test 1 optimal failed: {solution_optimal(nums1, 8)}"
    assert solution_brute(nums1, 8) == [3, 4], f"Test 1 brute failed"
    print("Test 1 (8 in [5,7,7,8,8,10] -> [3,4]) passed!")

    # Test case 2: Single occurrence
    assert solution_optimal(nums1, 6) == [-1, -1], f"Test 2 optimal failed"
    assert solution_brute(nums1, 6) == [-1, -1], f"Test 2 brute failed"
    print("Test 2 (6 not found -> [-1,-1]) passed!")

    # Test case 3: Target at the very beginning
    assert solution_optimal(nums1, 5) == [0, 0], f"Test 3 optimal failed"
    assert solution_brute(nums1, 5) == [0, 0], f"Test 3 brute failed"
    print("Test 3 (5 at start -> [0,0]) passed!")

    # Test case 4: All elements are the target
    nums4 = [2, 2, 2, 2, 2]
    assert solution_optimal(nums4, 2) == [0, 4], f"Test 4 optimal failed"
    assert solution_brute(nums4, 2) == [0, 4], f"Test 4 brute failed"
    print("Test 4 (all 2s -> [0,4]) passed!")

    # Test case 5: Empty array
    assert solution_optimal([], 0) == [-1, -1], f"Test 5 optimal failed"
    assert solution_brute([], 0) == [-1, -1], f"Test 5 brute failed"
    print("Test 5 (empty array) passed!")

    print(f"Brute force verification: {solution_brute([5,7,7,8,8,10], 10)}")
    print("All tests passed!")
