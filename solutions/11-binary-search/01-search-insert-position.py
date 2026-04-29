"""
LC 35. Search Insert Position (搜索插入位置)
Difficulty: Easy
Tags: Array, Binary Search
Link: https://leetcode.cn/problems/search-insert-position/
Category: binary-search
"""

from typing import List


# ===== 暴力解法 =====
# 思路: Linear scan through the sorted array. Find the first element >= target,
#       which is the insert position. If target > all elements, insert at end.
# 复杂度: O(n) time, O(1) space
def solution_brute(nums: List[int], target: int) -> int:
    """
    Find the index where target should be inserted using linear scan.
    """
    # WHY: Iterate through the array to find first element >= target
    for i in range(len(nums)):
        # WHY: When we find an element >= target, this is the insert position
        if nums[i] >= target:
            return i
    # WHY: If all elements are smaller than target, insert at the end
    return len(nums)


# ===== 最优解法 =====
# 思路: Binary search for the left boundary (first position where nums[pos] >= target).
#       This directly gives the insert position. Standard binary search template
#       with inclusive left and exclusive right bounds [left, right).
# 复杂度: O(log n) time, O(1) space
def solution_optimal(nums: List[int], target: int) -> int:
    """
    Find the index where target should be inserted using binary search (left boundary).
    """
    # WHY: Initialize search range as [left, right) — left inclusive, right exclusive
    left: int = 0
    right: int = len(nums)

    # WHY: Narrow search until range is exhausted (left == right)
    while left < right:
        # WHY: Calculate mid point, avoiding integer overflow
        mid: int = left + (right - left) // 2

        # WHY: If middle element >= target, target belongs in the left half
        if nums[mid] >= target:
            # WHY: Narrow right bound to mid (exclusive) to search left half
            right = mid
        else:
            # WHY: Middle element < target, so target belongs to the right half
            # WHY: Move left bound past mid since mid is too small
            left = mid + 1

    # WHY: left == right == first position where nums[pos] >= target (insert position)
    return left


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Search Insert Position...")

    # Test case 1: Target exists in the array
    nums1 = [1, 3, 5, 6]
    assert solution_optimal(nums1, 5) == 2, f"Test 1 failed"
    assert solution_brute(nums1, 5) == 2, f"Test 1 brute failed"
    print("Test 1 (5 in [1,3,5,6] -> 2) passed!")

    # Test case 2: Target not in array, should be inserted in middle
    assert solution_optimal(nums1, 2) == 1, f"Test 2 failed"
    assert solution_brute(nums1, 2) == 1, f"Test 2 brute failed"
    print("Test 2 (2 in [1,3,5,6] -> 1) passed!")

    # Test case 3: Target larger than all elements
    assert solution_optimal(nums1, 7) == 4, f"Test 3 failed"
    assert solution_brute(nums1, 7) == 4, f"Test 3 brute failed"
    print("Test 3 (7 in [1,3,5,6] -> 4) passed!")

    # Test case 4: Target smaller than all elements
    assert solution_optimal(nums1, 0) == 0, f"Test 4 failed"
    assert solution_brute(nums1, 0) == 0, f"Test 4 brute failed"
    print("Test 4 (0 in [1,3,5,6] -> 0) passed!")

    # Test case 5: Empty array
    assert solution_optimal([], 5) == 0, f"Test 5 failed"
    assert solution_brute([], 5) == 0, f"Test 5 brute failed"
    print("Test 5 (empty array) passed!")

    print(f"Brute force verification: {solution_brute([1,3,5,6], 5)}")
    print("All tests passed!")
