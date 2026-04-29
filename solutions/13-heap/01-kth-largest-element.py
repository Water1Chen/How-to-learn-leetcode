"""
LC 215. Kth Largest Element in an Array (数组中的第K个最大元素)
Difficulty: Medium
Tags: Array, Divide and Conquer, Heap (Priority Queue), Quickselect
Link: https://leetcode.cn/problems/kth-largest-element-in-an-array/
Category: heap
"""

from typing import List
import heapq
import random


# ===== 解法一: Min-Heap =====
# 思路: Use a min-heap of size k. Iterate through all elements, maintaining the heap
#       such that it always contains the k largest elements seen so far. The smallest
#       element in this heap (heap[0]) is the kth largest overall.
# 复杂度: O(n log k) time, O(k) space
def solution_heap(nums: List[int], k: int) -> int:
    """
    Find kth largest element using a min-heap of size k.
    """
    # WHY: Initialize a min-heap to track the k largest elements
    min_heap: list = []

    # WHY: Process each element in the array
    for num in nums:
        # WHY: Push current element onto the heap
        heapq.heappush(min_heap, num)

        # WHY: If heap exceeds size k, remove the smallest element
        # WHY: This keeps only the k largest elements in the heap
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    # WHY: The top of the min-heap is the kth largest (smallest of the k largest)
    return min_heap[0]


# ===== 解法二: Quickselect =====
# 思路: Use the Quickselect algorithm (similar to quicksort). Pick a pivot, partition
#       the array such that larger elements come before the pivot. If pivot is at index
#       k-1 (0-indexed), return it. Otherwise, recurse on the appropriate partition.
#       Average case O(n), but we implement median-of-medians or randomized pivot.
# 复杂度: O(n) average time, O(n^2) worst case, O(1) space (in-place partition)
def solution_quickselect(nums: List[int], k: int) -> int:
    """
    Find kth largest element using Quickselect algorithm.
    """
    # WHY: Work with a copy to avoid modifying the original (though we use in-place)
    arr: List[int] = nums
    n: int = len(arr)
    # WHY: kth largest corresponds to index (n - k) in 0-indexed sorted order
    target_idx: int = n - k

    # WHY: Helper to partition array around pivot, returns pivot's final position
    def partition(left: int, right: int, pivot_idx: int) -> int:
        # WHY: Move pivot to the end for easier partitioning
        pivot_val: int = arr[pivot_idx]
        arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]

        # WHY: store_idx tracks where elements smaller than pivot go
        store_idx: int = left

        # WHY: Iterate through the segment, moving elements <= pivot to the left
        for i in range(left, right):
            if arr[i] <= pivot_val:
                arr[i], arr[store_idx] = arr[store_idx], arr[i]
                store_idx += 1

        # WHY: Place pivot in its final sorted position
        arr[store_idx], arr[right] = arr[right], arr[store_idx]
        return store_idx

    # WHY: Quickselect recursion: find element at target_idx
    def quickselect(left: int, right: int) -> int:
        # WHY: Base case — single element left
        if left == right:
            return arr[left]

        # WHY: Randomly choose pivot to achieve O(n) average time
        pivot_idx: int = random.randint(left, right)
        # WHY: Partition and get the pivot's final index
        pivot_final: int = partition(left, right, pivot_idx)

        if target_idx == pivot_final:
            # WHY: Found the kth largest element
            return arr[target_idx]
        elif target_idx < pivot_final:
            # WHY: Target is in the left partition
            return quickselect(left, pivot_final - 1)
        else:
            # WHY: Target is in the right partition
            return quickselect(pivot_final + 1, right)

    return quickselect(0, n - 1)


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Kth Largest Element...")

    # Test case 1: Standard case
    nums1 = [3, 2, 1, 5, 6, 4]
    assert solution_heap(nums1, 2) == 5, f"Heap test 1 failed: {solution_heap(nums1, 2)}"
    assert solution_quickselect(nums1[:], 2) == 5, f"Quickselect test 1 failed"
    print("Test 1 ([3,2,1,5,6,4], k=2 -> 5) passed!")

    # Test case 2: Duplicate values
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    assert solution_heap(nums2, 4) == 4, f"Heap test 2 failed: {solution_heap(nums2, 4)}"
    assert solution_quickselect(nums2[:], 4) == 4, f"Quickselect test 2 failed"
    print("Test 2 (duplicates, k=4 -> 4) passed!")

    # Test case 3: k = 1 (largest element)
    nums3 = [1, 2, 3, 4, 5]
    assert solution_heap(nums3, 1) == 5, "Heap test 3 failed"
    assert solution_quickselect(nums3[:], 1) == 5, "Quickselect test 3 failed"
    print("Test 3 (k=1 -> 5) passed!")

    # Test case 4: k = n (smallest element)
    nums4 = [5, 4, 3, 2, 1]
    assert solution_heap(nums4, 5) == 1, "Heap test 4 failed"
    assert solution_quickselect(nums4[:], 5) == 1, "Quickselect test 4 failed"
    print("Test 4 (k=n -> 1) passed!")

    # Test case 5: Single element
    assert solution_heap([1], 1) == 1, "Heap test 5 failed"
    assert solution_quickselect([1], 1) == 1, "Quickselect test 5 failed"
    print("Test 5 (single element) passed!")

    print("All tests passed!")
