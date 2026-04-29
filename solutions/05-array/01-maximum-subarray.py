"""
LC 53. Maximum Subarray (最大子数组和)
Difficulty: Medium
Tags: Array, Divide and Conquer, Dynamic Programming
Link: https://leetcode.cn/problems/maximum-subarray/
Category: 05-array
"""

from typing import List


# ===== 暴力解法 =====
# 思路: 枚举所有可能的子数组，计算每个子数组的和，取最大值
# 复杂度: O(n^2) time, O(1) space
def solution_brute(nums: List[int]) -> int:
    # WHY: 暴力枚举所有子数组需要两层循环，外层固定起点，内层累加终点
    n = len(nums)
    max_sum = float('-inf')  # WHY: 初始化为负无穷，确保任何子数组和都能更新它
    for i in range(n):  # WHY: 枚举子数组的起始位置
        current_sum = 0  # WHY: 从起点开始累加，每轮重新初始化
        for j in range(i, n):  # WHY: 从i开始往后扩展子数组终点
            current_sum += nums[j]  # WHY: 累加当前元素到子数组和中
            max_sum = max(max_sum, current_sum)  # WHY: 更新全局最大值
    return max_sum


# ===== 最优解法 =====
# 思路: Kadane算法 — 遍历数组时，对每个位置i计算以i结尾的最大子数组和
#       递推公式: dp[i] = max(nums[i], dp[i-1] + nums[i])
#       含义: 要么从当前元素重新开始，要么接上前面的子数组
# 复杂度: O(n) time, O(1) space
def solution_optimal(nums: List[int]) -> int:
    # WHY: Kadane算法将问题分解为"以每个位置结尾的最大子数组和"
    # WHY: 相比暴力法，避免了重复计算子数组和，只需一次遍历
    current_max = nums[0]  # WHY: 以当前位置结尾的最大子数组和，初始为第一个元素
    global_max = nums[0]   # WHY: 全局最大子数组和，初始为第一个元素

    for i in range(1, len(nums)):  # WHY: 从第二个元素开始遍历
        # WHY: 核心转移方程：要么自成一派（从nums[i]重新开始），要么加入前面的子数组
        # WHY: 如果dp[i-1]是负数，加上它反而更小，不如从nums[i]重新开始
        current_max = max(nums[i], current_max + nums[i])
        # WHY: 更新全局最大值，因为全局最大可能出现在任意位置
        global_max = max(global_max, current_max)

    return global_max


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Maximum Subarray...")

    # 测试用例1: 标准情况，有正有负
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected1 = 6  # WHY: 子数组 [4,-1,2,1] 的和为 6
    result1 = solution_optimal(nums1)
    print(f"Test 1: {result1} == {expected1} -> {'PASS' if result1 == expected1 else 'FAIL'}")

    # 测试用例2: 全是负数
    nums2 = [-5, -2, -3, -1]
    expected2 = -1  # WHY: 最大的单个元素是 -1
    result2 = solution_optimal(nums2)
    print(f"Test 2: {result2} == {expected2} -> {'PASS' if result2 == expected2 else 'FAIL'}")

    # 测试用例3: 全是正数
    nums3 = [1, 2, 3, 4]
    expected3 = 10  # WHY: 整个数组的和
    result3 = solution_optimal(nums3)
    print(f"Test 3: {result3} == {expected3} -> {'PASS' if result3 == expected3 else 'FAIL'}")

    # 测试用例4: 单个元素
    nums4 = [7]
    expected4 = 7
    result4 = solution_optimal(nums4)
    print(f"Test 4: {result4} == {expected4} -> {'PASS' if result4 == expected4 else 'FAIL'}")

    print("\nAll tests complete!")
