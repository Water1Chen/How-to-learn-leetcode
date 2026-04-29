"""
LC 4. Median of Two Sorted Arrays (寻找两个正序数组的中位数)
Difficulty: Hard
Tags: Array, Binary Search, Divide and Conquer
Link: https://leetcode.cn/problems/median-of-two-sorted-arrays/
Category: binary-search
"""

from typing import List


# ===== 暴力解法 =====
# 思路: Merge both sorted arrays into one (like merge step of merge sort),
#       then find the median of the merged array. Even if we stop at the middle,
#       this requires O(m+n) time.
# 复杂度: O(m + n) time, O(m + n) space for the merged array
def solution_brute(nums1: List[int], nums2: List[int]) -> float:
    """
    Find the median by merging both sorted arrays.
    """
    merged: List[int] = []
    i: int = 0
    j: int = 0

    # WHY: Merge both sorted arrays into one sorted array
    while i < len(nums1) and j < len(nums2):
        # WHY: Take the smaller element from the two arrays
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    # WHY: Append remaining elements from nums1 (if any)
    while i < len(nums1):
        merged.append(nums1[i])
        i += 1

    # WHY: Append remaining elements from nums2 (if any)
    while j < len(nums2):
        merged.append(nums2[j])
        j += 1

    # WHY: Calculate median from the merged array
    total: int = len(merged)
    mid: int = total // 2

    # WHY: If total length is even, median is average of two middle elements
    if total % 2 == 0:
        return (merged[mid - 1] + merged[mid]) / 2.0
    # WHY: If total length is odd, median is the middle element
    return float(merged[mid])


# ===== 最优解法 =====
# 思路: Binary search on the smaller array to find the correct partition point.
#       We partition both arrays such that all elements in left partitions are
#       <= all elements in right partitions. Then median is derived from the
#       boundary elements. The key insight: we just need to find the right cut
#       in the smaller array; the cut in the larger array is determined.
# 复杂度: O(log(min(m, n))) time, O(1) space
def solution_optimal(nums1: List[int], nums2: List[int]) -> float:
    """
    Find the median using binary search on the smaller array for partition.
    """
    # WHY: Ensure nums1 is the smaller array to minimize binary search range
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m: int = len(nums1)
    n: int = len(nums2)
    total: int = m + n
    half: int = (total + 1) // 2  # WHY: Number of elements in the left partition

    # WHY: Binary search on the smaller array for correct partition point
    left: int = 0
    right: int = m

    while left <= right:
        # WHY: Partition point in nums1 (number of elements taken from nums1 for left partition)
        partition1: int = left + (right - left) // 2
        # WHY: Partition point in nums2 (remaining elements needed for left partition)
        partition2: int = half - partition1

        # WHY: Get boundary values around the partition points
        # WHY: left1 is the max element in left partition of nums1 (-inf if none)
        left1: int = nums1[partition1 - 1] if partition1 > 0 else -10**9
        # WHY: right1 is the min element in right partition of nums1 (+inf if none)
        right1: int = nums1[partition1] if partition1 < m else 10**9
        # WHY: left2 is the max element in left partition of nums2 (-inf if none)
        left2: int = nums2[partition2 - 1] if partition2 > 0 else -10**9
        # WHY: right2 is the min element in right partition of nums2 (+inf if none)
        right2: int = nums2[partition2] if partition2 < n else 10**9

        # WHY: Check if we have found the correct partition
        # WHY: Correct partition means all left <= all right
        if left1 <= right2 and left2 <= right1:
            # WHY: Correct partition found
            if total % 2 == 0:
                # WHY: Even length: median is average of max left and min right
                return (max(left1, left2) + min(right1, right2)) / 2.0
            else:
                # WHY: Odd length: median is the max of the left partition elements
                return float(max(left1, left2))
        elif left1 > right2:
            # WHY: left1 is too big, need to move partition1 left (take fewer from nums1)
            right = partition1 - 1
        else:
            # WHY: left2 > right1, need to move partition1 right (take more from nums1)
            left = partition1 + 1

    # WHY: Should never reach here with valid input
    return 0.0


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Median of Two Sorted Arrays...")

    # Test case 1: Odd total length
    nums1_1 = [1, 3]
    nums2_1 = [2]
    result_1_opt = solution_optimal(nums1_1, nums2_1)
    result_1_brute = solution_brute(nums1_1, nums2_1)
    assert abs(result_1_opt - 2.0) < 1e-9, f"Test 1 optimal failed: {result_1_opt}"
    assert abs(result_1_brute - 2.0) < 1e-9, f"Test 1 brute failed"
    print("Test 1 ([1,3], [2] -> 2.0) passed!")

    # Test case 2: Even total length
    nums2_1 = [1, 2]
    nums2_2 = [3, 4]
    result_2_opt = solution_optimal(nums2_1, nums2_2)
    result_2_brute = solution_brute(nums2_1, nums2_2)
    assert abs(result_2_opt - 2.5) < 1e-9, f"Test 2 optimal failed: {result_2_opt}"
    assert abs(result_2_brute - 2.5) < 1e-9, f"Test 2 brute failed"
    print("Test 2 ([1,2], [3,4] -> 2.5) passed!")

    # Test case 3: One array empty
    nums3_1 = []
    nums3_2 = [1]
    result_3_opt = solution_optimal(nums3_1, nums3_2)
    result_3_brute = solution_brute(nums3_1, nums3_2)
    assert abs(result_3_opt - 1.0) < 1e-9, f"Test 3 optimal failed: {result_3_opt}"
    assert abs(result_3_brute - 1.0) < 1e-9, f"Test 3 brute failed"
    print("Test 3 ([], [1] -> 1.0) passed!")

    # Test case 4: Duplicate values
    nums4_1 = [1, 2]
    nums4_2 = [1, 2]
    result_4_opt = solution_optimal(nums4_1, nums4_2)
    result_4_brute = solution_brute(nums4_1, nums4_2)
    assert abs(result_4_opt - 1.5) < 1e-9, f"Test 4 optimal failed: {result_4_opt}"
    assert abs(result_4_brute - 1.5) < 1e-9, f"Test 4 brute failed"
    print("Test 4 ([1,2], [1,2] -> 1.5) passed!")

    # Test case 5: Single elements each
    result_5_opt = solution_optimal([0], [0])
    result_5_brute = solution_brute([0], [0])
    assert abs(result_5_opt - 0.0) < 1e-9, f"Test 5 optimal failed"
    assert abs(result_5_brute - 0.0) < 1e-9, f"Test 5 brute failed"
    print("Test 5 ([0], [0] -> 0.0) passed!")

    print(f"Brute force verification: {solution_brute([1,3], [2])}")
    print("All tests passed!")
