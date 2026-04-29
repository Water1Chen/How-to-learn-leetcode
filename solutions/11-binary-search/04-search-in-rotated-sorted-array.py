"""
LC 33. Search in Rotated Sorted Array (搜索旋转排序数组)
Difficulty: Medium
Tags: Array, Binary Search
Link: https://leetcode.cn/problems/search-in-rotated-sorted-array/
Category: binary-search
"""

from typing import List


# ===== 暴力解法 =====
# 思路: Linear scan through the array, checking each element. Since the array
#       is rotated but we just scan every element, we don't use the rotation info.
# 复杂度: O(n) time, O(1) space
def solution_brute(nums: List[int], target: int) -> int:
    """
    Search for target in rotated sorted array using linear scan.
    """
    # WHY: Iterate through every element in the array
    for i in range(len(nums)):
        # WHY: Return the index if current element matches target
        if nums[i] == target:
            return i
    # WHY: Target not found in the array
    return -1


# ===== 最优解法 =====
# 思路: Modified binary search. Find the mid point. One half must be sorted
#       (since the array is rotated at one pivot). Determine which half is sorted
#       and check if target lies in that half to narrow the search.
# 复杂度: O(log n) time, O(1) space
def solution_optimal(nums: List[int], target: int) -> int:
    """
    Search for target in rotated sorted array using modified binary search.
    """
    if not nums:
        # WHY: Empty array cannot contain target
        return -1

    left: int = 0
    right: int = len(nums) - 1

    # WHY: Standard binary search with inclusive bounds
    while left <= right:
        mid: int = left + (right - left) // 2

        # WHY: Target found at mid
        if nums[mid] == target:
            return mid

        # WHY: Determine which half is sorted by comparing nums[left] with nums[mid]
        if nums[left] <= nums[mid]:
            # WHY: Left half [left, mid] is sorted
            # WHY: Check if target lies in the sorted left half
            if nums[left] <= target < nums[mid]:
                # WHY: Target is in the sorted left half, narrow right bound
                right = mid - 1
            else:
                # WHY: Target is not in the sorted left half, search the right half
                left = mid + 1
        else:
            # WHY: Right half [mid, right] is sorted
            # WHY: Check if target lies in the sorted right half
            if nums[mid] < target <= nums[right]:
                # WHY: Target is in the sorted right half, narrow left bound
                left = mid + 1
            else:
                # WHY: Target is not in the sorted right half, search the left half
                right = mid - 1

    # WHY: Target not found after narrowing entire search range
    return -1


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Search in Rotated Sorted Array...")

    # Test case 1: Standard rotated array, target found
    nums1 = [4, 5, 6, 7, 0, 1, 2]
    assert solution_optimal(nums1, 0) == 4, f"Test 1 optimal failed: {solution_optimal(nums1, 0)}"
    assert solution_brute(nums1, 0) == 4, f"Test 1 brute failed"
    print("Test 1 (0 found at index 4) passed!")

    # Test case 2: Target not in array
    assert solution_optimal(nums1, 3) == -1, f"Test 2 optimal failed"
    assert solution_brute(nums1, 3) == -1, f"Test 2 brute failed"
    print("Test 2 (3 not found) passed!")

    # Test case 3: No rotation (fully sorted)
    nums3 = [1, 2, 3, 4, 5, 6, 7]
    assert solution_optimal(nums3, 5) == 4, f"Test 3 optimal failed"
    assert solution_brute(nums3, 5) == 4, f"Test 3 brute failed"
    print("Test 3 (no rotation, 5 found) passed!")

    # Test case 4: Single element array, target matches
    assert solution_optimal([1], 1) == 0, f"Test 4 optimal failed"
    assert solution_brute([1], 1) == 0, f"Test 4 brute failed"
    print("Test 4 (single element, match) passed!")

    # Test case 5: Two elements rotated
    nums5 = [2, 1]
    assert solution_optimal(nums5, 1) == 1, f"Test 5 optimal failed"
    assert solution_brute(nums5, 1) == 1, f"Test 5 brute failed"
    print("Test 5 (two elements rotated) passed!")

    # Test case 6: Empty array
    assert solution_optimal([], 5) == -1, f"Test 6 optimal failed"
    assert solution_brute([], 5) == -1, f"Test 6 brute failed"
    print("Test 6 (empty array) passed!")

    print(f"Brute force verification: {solution_brute([4,5,6,7,0,1,2], 7)}")
    print("All tests passed!")
