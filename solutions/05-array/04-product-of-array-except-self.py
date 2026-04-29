"""
LC 238. Product of Array Except Self (除自身以外数组的乘积)
Difficulty: Medium
Tags: Array, Prefix Sum
Link: https://leetcode.cn/problems/product-of-array-except-self/
Category: 05-array
"""

from typing import List


# ===== 暴力解法 =====
# 思路: 对每个位置i，遍历所有元素计算除nums[i]外的乘积
# 复杂度: O(n^2) time, O(1) space (output数组不计)
def solution_brute(nums: List[int]) -> List[int]:
    # WHY: 暴力法直接按照问题描述，对每个位置重新计算乘积
    n = len(nums)
    result = [1] * n  # WHY: 初始化结果数组，每个位置先设为1（乘法单位元）
    for i in range(n):  # WHY: 遍历每个位置，计算该位置的结果
        for j in range(n):  # WHY: 遍历所有元素，累乘除nums[i]外的值
            if i != j:  # WHY: 跳过自身
                result[i] *= nums[j]  # WHY: 累乘其他所有元素
    return result


# ===== 最优解法 =====
# 思路: 前缀积 × 后缀积 — 对每个位置i，结果 = 左边所有数的积 × 右边所有数的积
#       先从左到右计算每个位置左边的乘积，再从右到左乘上右边的乘积
#       关键优化: 直接在输出数组上操作，避免额外空间
# 复杂度: O(n) time, O(1) space (output数组不计入额外空间)
def solution_optimal(nums: List[int]) -> List[int]:
    # WHY: 利用前缀积和后缀积分解问题，一次遍历计算左侧，一次遍历乘上右侧
    # WHY: 相比暴力法O(n^2)，将乘积计算分解为两个方向的累积过程
    n = len(nums)
    result = [1] * n  # WHY: 初始化结果数组，每个位置先设为1

    # WHY: 第一次遍历：计算每个位置左侧所有元素的乘积
    left_product = 1  # WHY: 当前索引i左侧所有元素的累积乘积
    for i in range(n):
        result[i] = left_product  # WHY: result[i]暂时存储左侧乘积
        left_product *= nums[i]  # WHY: 为下一个位置更新左侧乘积（包含当前nums[i]）

    # WHY: 第二次遍历：从右向左，将右侧乘积乘入结果
    right_product = 1  # WHY: 当前索引i右侧所有元素的累积乘积
    for i in range(n - 1, -1, -1):
        # WHY: 此时result[i] = 左侧乘积，乘上右侧乘积得到最终结果
        result[i] *= right_product
        right_product *= nums[i]  # WHY: 为下一个位置更新右侧乘积（包含当前nums[i]）

    return result


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Product of Array Except Self...")

    # 测试用例1: 标准情况，正数
    nums1 = [1, 2, 3, 4]
    expected1 = [24, 12, 8, 6]
    result1 = solution_optimal(nums1)
    print(f"Test 1: {result1} == {expected1} -> {'PASS' if result1 == expected1 else 'FAIL'}")

    # 测试用例2: 包含0
    nums2 = [-1, 1, 0, -3, 3]
    expected2 = [0, 0, 9, 0, 0]
    result2 = solution_optimal(nums2)
    print(f"Test 2: {result2} == {expected2} -> {'PASS' if result2 == expected2 else 'FAIL'}")

    # 测试用例3: 两个元素
    nums3 = [2, 3]
    expected3 = [3, 2]
    result3 = solution_optimal(nums3)
    print(f"Test 3: {result3} == {expected3} -> {'PASS' if result3 == expected3 else 'FAIL'}")

    # 测试用例4: 包含负数
    nums4 = [5, -2, 3]
    expected4 = [-6, 15, -10]
    result4 = solution_optimal(nums4)
    print(f"Test 4: {result4} == {expected4} -> {'PASS' if result4 == expected4 else 'FAIL'}")

    print("\nAll tests complete!")
