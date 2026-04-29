"""
LC 239. 滑动窗口最大值 (Sliding Window Maximum)
Difficulty: Hard
Tags: Array, Queue, Sliding Window, Monotonic Queue, Heap (Priority Queue)
Link: https://leetcode.cn/problems/sliding-window-maximum/
Category: 04-substring
"""

from typing import List
from collections import deque


# ===== 暴力解法 =====
# 思路: 对每个窗口位置，遍历窗口内所有元素找到最大值。
# 复杂度: O(nk) time, O(1) space (不计输出数组)
def solution_brute(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    result: List[int] = []

    # WHY: 枚举所有窗口的起始位置
    for i in range(n - k + 1):
        # WHY: 遍历窗口内所有元素找最大值
        max_val = nums[i]
        for j in range(i + 1, i + k):
            max_val = max(max_val, nums[j])
        result.append(max_val)

    return result


# ===== 最优解法 =====
# 思路: 单调递减双端队列。队列中存储的是数组下标（而非值），
#       保证队列中对应的值从队首到队尾是严格递减的。
#       每次窗口移动时：1) 移出不在窗口内的队首元素 2) 从队尾移除所有 ≤ 新元素的值
#       3) 将新元素下标入队 4) 队首即为当前窗口最大值。
# 复杂度: O(n) time（每个元素最多入队一次、出队一次）, O(k) space
def solution_optimal(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    result: List[int] = []

    # WHY: 单调递减队列，存储数组下标，保证对应值从队首到队尾严格递减
    # WHY: 使用 collections.deque 实现 O(1) 的队首/队尾操作
    dq: deque = deque()

    # WHY: 遍历每个元素，构建第一个窗口并处理后续窗口
    for i in range(n):
        # WHY: 移除不在当前窗口内的队首元素（下标 < i - k + 1 的已过时）
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # WHY: 从队尾开始，移除所有 ≤ 当前元素的下标
        # WHY: 这些值不可能是后续任何窗口的最大值（因为当前元素更大且更靠右）
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()

        # WHY: 将当前元素下标加入队尾
        dq.append(i)

        # WHY: 当遍历的索引 i 达到 k-1（第一个窗口结束时），开始记录结果
        if i >= k - 1:
            # WHY: 队首元素对应的值就是当前窗口的最大值
            result.append(nums[dq[0]])

    return result


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Sliding Window Maximum...")

    # Test case 1 - 基础用例
    nums1 = [1, 3, -1, -3, 5, 3, 6, 7]
    k1 = 3
    result1 = solution_optimal(nums1, k1)
    print(f"Test 1: {result1} == [3,3,5,5,6,7] -> {'PASS' if result1 == [3,3,5,5,6,7] else 'FAIL'}")

    # Test case 2 - 单个元素
    nums2 = [1]
    k2 = 1
    result2 = solution_optimal(nums2, k2)
    print(f"Test 2: {result2} == [1] -> {'PASS' if result2 == [1] else 'FAIL'}")

    # Test case 3 - 降序数组
    nums3 = [5, 4, 3, 2, 1]
    k3 = 3
    result3 = solution_optimal(nums3, k3)
    print(f"Test 3: {result3} == [5,4,3] -> {'PASS' if result3 == [5,4,3] else 'FAIL'}")

    # Test case 4 - 升序数组
    nums4 = [1, 2, 3, 4, 5]
    k4 = 3
    result4 = solution_optimal(nums4, k4)
    print(f"Test 4: {result4} == [3,4,5] -> {'PASS' if result4 == [3,4,5] else 'FAIL'}")

    # 验证暴力解法
    print("\nBrute force verification:")
    print(f"Brute Test 1: {solution_brute(nums1, k1)}")
    print(f"Brute Test 2: {solution_brute(nums2, k2)}")

    print("\nAll tests complete!")
