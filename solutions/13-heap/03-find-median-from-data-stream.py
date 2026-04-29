"""
LC 295. Find Median from Data Stream (数据流的中位数)
Difficulty: Hard
Tags: Two Pointers, Design, Heap (Priority Queue), Data Stream
Link: https://leetcode.cn/problems/find-median-from-data-stream/
Category: heap
"""

import heapq


# ===== 暴力解法 =====
# 思路: Maintain a sorted list. Each insertion uses binary search + insert (O(n)),
#       median retrieval is O(1) by accessing the middle element(s).
# 复杂度: addNum: O(n) time (due to list insertion shift), findMedian: O(1) time, O(n) space
class MedianFinderBrute:
    """
    Maintain median of a stream using a sorted list.
    """
    def __init__(self) -> None:
        # WHY: Store all numbers in a sorted list
        self._nums: list = []

    def addNum(self, num: int) -> None:
        # WHY: Find insertion point using binary search
        left: int = 0
        right: int = len(self._nums)
        while left < right:
            mid: int = left + (right - left) // 2
            if self._nums[mid] < num:
                left = mid + 1
            else:
                right = mid
        # WHY: Insert at correct position (O(n) due to shifting elements)
        self._nums.insert(left, num)

    def findMedian(self) -> float:
        # WHY: Access the middle element(s) directly
        n: int = len(self._nums)
        mid: int = n // 2
        if n % 2 == 0:
            # WHY: Even length: average of two middle elements
            return (self._nums[mid - 1] + self._nums[mid]) / 2.0
        # WHY: Odd length: middle element
        return float(self._nums[mid])


# ===== 最优解法 =====
# 思路: Two-heap approach: max-heap for the smaller half, min-heap for the larger half.
#       Python's heapq is a min-heap, so we store negative values to simulate max-heap.
#       Invariant: len(low) == len(high) or len(low) == len(high) + 1.
#       This ensures the median is always the top of low (or average of both tops).
# 复杂度: addNum: O(log n) time, findMedian: O(1) time, O(n) space
class MedianFinderOptimal:
    """
    Maintain median of a stream using two heaps (max-heap for lower half, min-heap for upper half).
    """
    def __init__(self) -> None:
        # WHY: Max-heap for the smaller half (store negative values for Python's min-heap)
        self._low: list = []   # Max-heap (negated values)
        # WHY: Min-heap for the larger half
        self._high: list = []  # Min-heap

    def addNum(self, num: int) -> None:
        # WHY: Step 1: Add to the max-heap (negated) for the lower half
        heapq.heappush(self._low, -num)

        # WHY: Step 2: Ensure every element in low <= every element in high
        # WHY: If the largest in low > smallest in high, move the largest from low to high
        if self._low and self._high and (-self._low[0]) > self._high[0]:
            # WHY: Pop the largest from low (negate back to positive)
            val: int = -heapq.heappop(self._low)
            # WHY: Push it into the high (min-heap)
            heapq.heappush(self._high, val)

        # WHY: Step 3: Balance sizes — low can have at most 1 more element than high
        if len(self._low) > len(self._high) + 1:
            # WHY: Move the largest element from low to high to restore balance
            val: int = -heapq.heappop(self._low)
            heapq.heappush(self._high, val)
        elif len(self._high) > len(self._low):
            # WHY: High has more elements — move the smallest from high to low
            val: int = heapq.heappop(self._high)
            heapq.heappush(self._low, -val)

    def findMedian(self) -> float:
        # WHY: If low has more elements, median is the top of low (the largest in lower half)
        if len(self._low) > len(self._high):
            return float(-self._low[0])

        # WHY: Equal sizes: median is average of tops of both heaps
        return (-self._low[0] + self._high[0]) / 2.0


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Find Median from Data Stream...")

    # Test case 1: Standard sequence
    mf_opt = MedianFinderOptimal()
    mf_brute = MedianFinderBrute()
    mf_opt.addNum(1)
    mf_brute.addNum(1)
    assert mf_opt.findMedian() == 1.0, f"Test 1 step 1 failed: {mf_opt.findMedian()}"
    mf_opt.addNum(2)
    mf_brute.addNum(2)
    assert mf_opt.findMedian() == 1.5, f"Test 1 step 2 failed: {mf_opt.findMedian()}"
    mf_opt.addNum(3)
    mf_brute.addNum(3)
    assert mf_opt.findMedian() == 2.0, f"Test 1 step 3 failed: {mf_opt.findMedian()}"
    # WHY: Verify optimal matches brute force at each step
    assert mf_opt.findMedian() == mf_brute.findMedian(), "Test 1 mismatch with brute"
    print("Test 1 (1,2,3 -> medians: 1, 1.5, 2) passed!")

    # Test case 2: Negative numbers
    mf2_opt = MedianFinderOptimal()
    mf2_brute = MedianFinderBrute()
    for num in [-1, -2, -3]:
        mf2_opt.addNum(num)
        mf2_brute.addNum(num)
    assert mf2_opt.findMedian() == -2.0, f"Test 2 failed: {mf2_opt.findMedian()}"
    assert abs(mf2_opt.findMedian() - mf2_brute.findMedian()) < 1e-9, "Test 2 mismatch"
    print("Test 2 (negatives) passed!")

    # Test case 3: Even count with large numbers
    mf3_opt = MedianFinderOptimal()
    mf3_brute = MedianFinderBrute()
    for num in [6, 10, 2, 8]:
        mf3_opt.addNum(num)
        mf3_brute.addNum(num)
    assert mf3_opt.findMedian() == 7.0, f"Test 3 failed: {mf3_opt.findMedian()}"
    assert abs(mf3_opt.findMedian() - mf3_brute.findMedian()) < 1e-9, "Test 3 mismatch"
    print("Test 3 ([6,10,2,8] -> median 7) passed!")

    # Test case 4: Single element
    mf4_opt = MedianFinderOptimal()
    mf4_opt.addNum(42)
    assert mf4_opt.findMedian() == 42.0, "Test 4 failed"
    print("Test 4 (single element) passed!")

    # Test case 5: Duplicates
    mf5_opt = MedianFinderOptimal()
    mf5_brute = MedianFinderBrute()
    for num in [1, 1, 1, 2, 2]:
        mf5_opt.addNum(num)
        mf5_brute.addNum(num)
    assert mf5_opt.findMedian() == 1.0, f"Test 5 failed: {mf5_opt.findMedian()}"
    assert abs(mf5_opt.findMedian() - mf5_brute.findMedian()) < 1e-9, "Test 5 mismatch"
    print("Test 5 (duplicates) passed!")

    print("All tests passed!")
