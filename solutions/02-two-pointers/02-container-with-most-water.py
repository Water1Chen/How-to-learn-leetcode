"""
LC 11. 盛最多水的容器 (Container With Most Water)
Difficulty: Medium
Tags: Array, Two Pointers, Greedy
Link: https://leetcode.cn/problems/container-with-most-water/
Category: 02-two-pointers
"""

from typing import List


# ===== 暴力解法 =====
# 思路: 枚举所有两根线组成的组合，计算每个组合的盛水量，取最大值。
#       盛水量 = 两根线中较短的那根的高度 × 两根线之间的距离。
# 复杂度: O(n²) time, O(1) space
def solution_brute(height: List[int]) -> int:
    n = len(height)
    max_water = 0

    # WHY: 外层循环固定左边界
    for left in range(n):
        # WHY: 内层循环从 left + 1 开始，避免重复计算
        for right in range(left + 1, n):
            # WHY: 盛水量取决于较短的板（木桶效应）
            cur_water = min(height[left], height[right]) * (right - left)
            # WHY: 更新全局最大值
            max_water = max(max_water, cur_water)

    return max_water


# ===== 最优解法 =====
# 思路: 双指针从两端向中间移动。每次移动较矮的那一侧指针，
#       因为盛水量由较矮的板决定，移动较高的板只会让容量变小（距离缩短）。
#       这样只需 O(n) 次计算即可找到最大值。
# 复杂度: O(n) time, O(1) space
def solution_optimal(height: List[int]) -> int:
    # WHY: 左右指针初始在两端，此时宽度最大
    left = 0
    right = len(height) - 1
    max_water = 0

    # WHY: 当左右指针相遇时，所有可能的情况都已检查完毕
    while left < right:
        # WHY: 计算当前容器的盛水量 = 短板高度 × 宽度
        cur_water = min(height[left], height[right]) * (right - left)
        # WHY: 更新全局最大值
        max_water = max(max_water, cur_water)

        # WHY: 移动较矮的那一侧指针
        # WHY: 如果移动较高的一侧，新容器高度 ≤ 原容器高度，且宽度变小，容量一定变小
        # WHY: 只有移动较矮的一侧才有可能找到更高的板，从而提升容量
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Container With Most Water...")

    # Test case 1 - 基础用例
    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result1 = solution_optimal(height1)
    print(f"Test 1: {result1} == 49 -> {'PASS' if result1 == 49 else 'FAIL'}")
    # WHY: 最大容量在 height[1]=8 和 height[8]=7 之间，min(8,7)*(8-1)=49

    # Test case 2 - 递增
    height2 = [1, 2, 3, 4, 5]
    result2 = solution_optimal(height2)
    print(f"Test 2: {result2} == 6 -> {'PASS' if result2 == 6 else 'FAIL'}")
    # WHY: height[2]=3 和 height[4]=5, min(3,5)*(4-2)=6

    # Test case 3 - 只有两根线
    height3 = [1, 2]
    result3 = solution_optimal(height3)
    print(f"Test 3: {result3} == 1 -> {'PASS' if result3 == 1 else 'FAIL'}")

    # Test case 4 - 等高的容器
    height4 = [5, 5, 5, 5]
    result4 = solution_optimal(height4)
    print(f"Test 4: {result4} == 15 -> {'PASS' if result4 == 15 else 'FAIL'}")
    # WHY: height[0]=5 和 height[3]=5, 5*(3-0)=15

    # 验证暴力解法
    print("\nBrute force verification:")
    print(f"Brute Test 1: {solution_brute(height1)}")
    print(f"Brute Test 2: {solution_brute(height2)}")

    print("\nAll tests complete!")
