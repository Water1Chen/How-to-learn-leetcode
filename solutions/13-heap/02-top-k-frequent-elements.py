"""
LC 347. Top K Frequent Elements (前 K 个高频元素)
Difficulty: Medium
Tags: Array, Hash Table, Heap (Priority Queue), Bucket Sort
Link: https://leetcode.cn/problems/top-k-frequent-elements/
Category: heap
"""

from typing import List
import heapq
from collections import Counter


# ===== 方法一: Heap (Priority Queue) =====
# 思路: Count frequencies with a hash map. Use a min-heap of size k to track the
#       k most frequent elements. For each (element, freq) pair, push onto heap;
#       if heap exceeds k, pop the smallest (least frequent) element.
# 复杂度: O(n log k) time, O(n + k) space for hashmap and heap
def solution_heap(nums: List[int], k: int) -> List[int]:
    """
    Find k most frequent elements using a min-heap of size k.
    """
    # WHY: Count frequency of each element using a hash map
    freq: dict = Counter(nums)

    # WHY: Min-heap stores tuples of (frequency, element) — we want to keep largest frequencies
    min_heap: list = []

    # WHY: Iterate through all unique elements and their frequencies
    for num, count in freq.items():
        # WHY: Push (frequency, element) onto the heap
        heapq.heappush(min_heap, (count, num))

        # WHY: If heap exceeds size k, remove the element with smallest frequency
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    # WHY: Extract the elements (discard frequency) from the heap
    return [num for _, num in min_heap]


# ===== 方法二: Bucket Sort =====
# 思路: Count frequencies. Since the maximum frequency is n (array length), create
#       buckets where bucket[i] contains all elements with frequency i.
#       Then traverse buckets from highest frequency downward, collecting elements.
# 复杂度: O(n) time, O(n) space
def solution_bucket(nums: List[int], k: int) -> List[int]:
    """
    Find k most frequent elements using bucket sort (counting sort by frequency).
    """
    # WHY: Count frequency of each element
    freq: dict = Counter(nums)

    # WHY: Create buckets where index = frequency, value = list of elements with that freq
    # WHY: Maximum frequency is len(nums), so we need n+1 buckets
    n: int = len(nums)
    buckets: List[List[int]] = [[] for _ in range(n + 1)]

    # WHY: Place each element into the bucket corresponding to its frequency
    for num, count in freq.items():
        buckets[count].append(num)

    # WHY: Collect top k frequent elements by traversing buckets from high to low frequency
    result: List[int] = []
    # WHY: Start from highest possible frequency (n) down to 1
    for freq_val in range(n, 0, -1):
        # WHY: Process all elements in the current frequency bucket
        for num in buckets[freq_val]:
            result.append(num)
            # WHY: Stop once we have collected k elements
            if len(result) == k:
                return result

    return result


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Top K Frequent Elements...")

    # Test case 1: Standard case
    nums1 = [1, 1, 1, 2, 2, 3]
    result1_heap = solution_heap(nums1, 2)
    result1_bucket = solution_bucket(nums1, 2)
    assert sorted(result1_heap) == [1, 2], f"Heap test 1 failed: {result1_heap}"
    assert sorted(result1_bucket) == [1, 2], f"Bucket test 1 failed: {result1_bucket}"
    print("Test 1 ([1,1,1,2,2,3], k=2 -> [1,2]) passed!")

    # Test case 2: Single element, k=1
    assert solution_heap([1], 1) == [1], "Heap test 2 failed"
    assert solution_bucket([1], 1) == [1], "Bucket test 2 failed"
    print("Test 2 ([1], k=1 -> [1]) passed!")

    # Test case 3: All elements have same frequency
    nums3 = [1, 2, 3, 4]
    result3_heap = solution_heap(nums3, 2)
    result3_bucket = solution_bucket(nums3, 2)
    # WHY: Any two elements are valid since all have frequency 1
    assert len(result3_heap) == 2, f"Heap test 3 failed: {result3_heap}"
    assert len(result3_bucket) == 2, f"Bucket test 3 failed: {result3_bucket}"
    print("Test 3 (all freq=1, k=2) passed!")

    # Test case 4: k equals number of unique elements
    nums4 = [1, 1, 2, 2, 3, 3]
    result4_heap = solution_heap(nums4, 3)
    result4_bucket = solution_bucket(nums4, 3)
    assert sorted(result4_heap) == [1, 2, 3], f"Heap test 4 failed: {result4_heap}"
    assert sorted(result4_bucket) == [1, 2, 3], f"Bucket test 4 failed: {result4_bucket}"
    print("Test 4 (k=3, all unique) passed!")

    # Test case 5: Negative numbers
    nums5 = [-1, -1, 0, 0, 0, 2]
    result5_heap = solution_heap(nums5, 2)
    result5_bucket = solution_bucket(nums5, 2)
    assert sorted(result5_heap) == [-1, 0], f"Heap test 5 failed: {result5_heap}"
    assert sorted(result5_bucket) == [-1, 0], f"Bucket test 5 failed: {result5_bucket}"
    print("Test 5 (negatives) passed!")

    print("All tests passed!")
