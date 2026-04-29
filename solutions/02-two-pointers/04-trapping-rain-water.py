"""
LC 42. 接雨水 (Trapping Rain Water)
Difficulty: Hard
Tags: Array, Two Pointers, Dynamic Programming, Monotonic Stack
Link: https://leetcode.cn/problems/trapping-rain-water/
Category: 02-two-pointers
"""

from typing import List


# ===== 暴力解法 =====
# 思路: 对每个位置，分别向左和向右扫描找到左边最大值和右边最大值，
#       该位置能接的雨水 = min(left_max, right_max) - height[i]。
# 复杂度: O(n²) time, O(1) space
def solution_brute(height: List[int]) -> int:
    n = len(height)
    total = 0

    # WHY: 第一个和最后一个位置不能接雨水（没有左侧或右侧边界）
    for i in range(1, n - 1):
        # WHY: 向左扫描找到左边最高柱子
        left_max = 0
        for j in range(i, -1, -1):
            left_max = max(left_max, height[j])

        # WHY: 向右扫描找到右边最高柱子
        right_max = 0
        for j in range(i, n):
            right_max = max(right_max, height[j])

        # WHY: 当前位置能接的雨水 = 两侧较矮的那根 - 当前高度
        total += min(left_max, right_max) - height[i]

    return total


# ===== 最优解法 =====
# 思路: 双指针从两端向中间逼近，维护 left_max 和 right_max。
#       对于左指针位置，如果左边最大值 ≤ 右边最大值，则左指针处的水量由左边决定，
#       否则右指针处的水量由右边决定。这样避免了为每个位置重新扫描左右最大值。
# 复杂度: O(n) time, O(1) space
def solution_optimal(height: List[int]) -> int:
    n = len(height)
    # WHY: 长度小于 3 时无法接雨水
    if n < 3:
        return 0

    # WHY: 左右指针从两端开始向中间移动
    left = 0
    right = n - 1
    # WHY: 维护左右两侧扫描过的最大高度
    left_max = 0
    right_max = 0
    total = 0

    # WHY: 当左右指针相遇时所有位置已处理完毕
    while left < right:
        # WHY: 更新左侧最大值（包含当前柱子）
        left_max = max(left_max, height[left])
        # WHY: 更新右侧最大值（包含当前柱子）
        right_max = max(right_max, height[right])

        # WHY: 比较当前左右两侧的最大高度，决定处理哪一侧
        # WHY: 水量由较矮的那一侧决定（木桶效应）
        if left_max < right_max:
            # WHY: 左指针处的水量 = 左侧最大值 - 当前高度
            # WHY: 因为右侧已有更高的柱子，水不会从右侧流走
            total += left_max - height[left]
            left += 1
        else:
            # WHY: 右指针处的水量 = 右侧最大值 - 当前高度
            total += right_max - height[right]
            right -= 1

    return total


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Trapping Rain Water...")

    # Test case 1 - 基础用例
    height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result1 = solution_optimal(height1)
    print(f"Test 1: {result1} == 6 -> {'PASS' if result1 == 6 else 'FAIL'}")

    # Test case 2 - 两个柱子
    height2 = [4, 2, 0, 3, 2, 5]
    result2 = solution_optimal(height2)
    print(f"Test 2: {result2} == 9 -> {'PASS' if result2 == 9 else 'FAIL'}")

    # Test case 3 - 不足三个元素
    height3 = [1, 2]
    result3 = solution_optimal(height3)
    print(f"Test 3: {result3} == 0 -> {'PASS' if result3 == 0 else 'FAIL'}")

    # Test case 4 - 递增（接不到雨水）
    height4 = [1, 2, 3, 4, 5]
    result4 = solution_optimal(height4)
    print(f"Test 4: {result4} == 0 -> {'PASS' if result4 == 0 else 'FAIL'}")

    # 验证暴力解法
    print("\nBrute force verification:")
    print(f"Brute Test 1: {solution_brute(height1)}")
    print(f"Brute Test 2: {solution_brute(height2)}")

    print("\nAll tests complete!")
