"""
LC 153. Find Minimum in Rotated Sorted Array (寻找旋转排序数组中的最小值)
Difficulty: Medium
Tags: Array, Binary Search
Link: https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/
Category: binary-search
"""

from typing import List


# ===== 暴力解法 =====
# 思路: Linear scan to find the minimum element. The minimum is the "rotation point"
#       where the sorted order breaks. We can just scan for the smallest element.
# 复杂度: O(n) time, O(1) space
def solution_brute(nums: List[int]) -> int:
    """
    Find the minimum element in rotated sorted array using linear scan.
    """
    # WHY: Initialize minimum as the first element
    min_val: int = nums[0]

    # WHY: Scan through all elements to find the smallest
    for num in nums:
        # WHY: Update minimum if current element is smaller
        if num < min_val:
            min_val = num

    return min_val


# ===== 最优解法 =====
# 思路: Binary search comparing nums[mid] with nums[right]. If nums[mid] > nums[right],
#       the minimum is in the right half (because the rotation point is ahead).
#       If nums[mid] < nums[right], the minimum is in the left half (including mid).
#       When left == right, we have found the minimum.
# 复杂度: O(log n) time, O(1) space
def solution_optimal(nums: List[int]) -> int:
    """
    Find the minimum element in rotated sorted array using binary search.
    """
    left: int = 0
    right: int = len(nums) - 1

    # WHY: Binary search narrowing down to the pivot (minimum)
    while left < right:
        mid: int = left + (right - left) // 2

        # WHY: If mid element > right element, pivot is in the right half
        # WHY: This means the rotation point (minimum) is somewhere after mid
        if nums[mid] > nums[right]:
            # WHY: Minimum cannot be at or before mid, move left bound past mid
            left = mid + 1
        else:
            # WHY: nums[mid] <= nums[right], so right half is sorted
            # WHY: Minimum is in the left half (including mid)
            right = mid

    # WHY: When left == right, we have found the minimum's index
    return nums[left]


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Find Minimum in Rotated Sorted Array...")

    # Test case 1: Standard rotated array
    nums1 = [3, 4, 5, 1, 2]
    assert solution_optimal(nums1) == 1, f"Test 1 optimal failed: {solution_optimal(nums1)}"
    assert solution_brute(nums1) == 1, f"Test 1 brute failed"
    print("Test 1 ([3,4,5,1,2] -> 1) passed!")

    # Test case 2: No rotation (already sorted)
    nums2 = [1, 2, 3, 4, 5]
    assert solution_optimal(nums2) == 1, f"Test 2 optimal failed"
    assert solution_brute(nums2) == 1, f"Test 2 brute failed"
    print("Test 2 ([1,2,3,4,5] -> 1) passed!")

    # Test case 3: Fully rotated (min at the end)
    nums3 = [2, 3, 4, 5, 1]
    assert solution_optimal(nums3) == 1, f"Test 3 optimal failed"
    assert solution_brute(nums3) == 1, f"Test 3 brute failed"
    print("Test 3 ([2,3,4,5,1] -> 1) passed!")

    # Test case 4: Two elements rotated
    nums4 = [2, 1]
    assert solution_optimal(nums4) == 1, f"Test 4 optimal failed"
    assert solution_brute(nums4) == 1, f"Test 4 brute failed"
    print("Test 4 ([2,1] -> 1) passed!")

    # Test case 5: Single element
    assert solution_optimal([1]) == 1, f"Test 5 optimal failed"
    assert solution_brute([1]) == 1, f"Test 5 brute failed"
    print("Test 5 ([1] -> 1) passed!")

    print(f"Brute force verification: {solution_brute([4,5,6,7,0,1,2])}")
    print("All tests passed!")
