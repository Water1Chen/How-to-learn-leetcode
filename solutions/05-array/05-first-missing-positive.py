"""
LC 41. First Missing Positive (缺失的第一个正数)
Difficulty: Hard
Tags: Array, Hash Table
Link: https://leetcode.cn/problems/first-missing-positive/
Category: 05-array
"""

from typing import List


# ===== 暴力解法 =====
# 思路: 排序后找第一个缺失的正数
# 复杂度: O(n log n) time, O(1) space (允许原地排序)
def solution_brute(nums: List[int]) -> int:
    # WHY: 排序后可以线性扫描找第一个不连续的正数
    nums.sort()  # WHY: 原地排序，O(n log n)
    smallest = 1  # WHY: 最小的正整数从1开始
    for num in nums:
        if num == smallest:
            # WHY: 找到了当前期望的正数，下一个期望值+1
            smallest += 1
        # WHY: 如果num < smallest说明是重复数或非正数，跳过
    return smallest


# ===== 最优解法 =====
# 思路: 原地哈希（桶排序思想）— 将每个正整数x放到索引x-1处
#       第一次遍历: 将每个在[1, n]范围内的数放到正确位置
#       第二次遍历: 找到第一个位置不匹配的数，即为缺失的最小正数
#       关键点: 利用数组本身作为哈希表，不占用额外空间
# 复杂度: O(n) time, O(1) space
def solution_optimal(nums: List[int]) -> int:
    # WHY: 利用数组索引作为哈希键，将值x放到索引x-1处
    # WHY: 只关心[1, n]范围内的正整数，其他数不影响结果
    n = len(nums)

    # WHY: 第一次遍历：将每个数放到它应该在的位置上
    for i in range(n):
        # WHY: 循环交换直到当前位置的值正确或无法交换
        # WHY: 条件：值在[1, n]范围内，且没在正确位置上，且目标位置的值也不正确
        while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
            # WHY: 将nums[i]交换到它应该在的索引位置nums[i]-1
            correct_idx = nums[i] - 1
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]

    # WHY: 第二次遍历：找到第一个位置不匹配的元素
    for i in range(n):
        if nums[i] != i + 1:
            # WHY: 期望nums[i] = i+1，否则i+1就是缺失的最小正数
            return i + 1

    # WHY: 如果数组包含1到n所有数，缺失的是n+1
    return n + 1


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing First Missing Positive...")

    # 测试用例1: 标准情况（来自题目）
    nums1 = [3, 4, -1, 1]
    expected1 = 2
    result1 = solution_optimal(nums1)
    print(f"Test 1: {result1} == {expected1} -> {'PASS' if result1 == expected1 else 'FAIL'}")

    # 测试用例2: 从1开始连续
    nums2 = [1, 2, 0]
    expected2 = 3
    result2 = solution_optimal(nums2)
    print(f"Test 2: {result2} == {expected2} -> {'PASS' if result2 == expected2 else 'FAIL'}")

    # 测试用例3: 全部不连续
    nums3 = [7, 8, 9, 11, 12]
    expected3 = 1
    result3 = solution_optimal(nums3)
    print(f"Test 3: {result3} == {expected3} -> {'PASS' if result3 == expected3 else 'FAIL'}")

    # 测试用例4: 包含重复
    nums4 = [1, 1, 2, 2]
    expected4 = 3
    result4 = solution_optimal(nums4)
    print(f"Test 4: {result4} == {expected4} -> {'PASS' if result4 == expected4 else 'FAIL'}")

    print("\nAll tests complete!")
