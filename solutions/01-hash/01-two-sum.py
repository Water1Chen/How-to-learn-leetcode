"""
LC 1. 两数之和 (Two Sum)
Difficulty: Easy
Tags: Array, Hash Table
Link: https://leetcode.cn/problems/two-sum/
Category: 01-hash
"""

from typing import List, Dict


# ===== 暴力解法 =====
# 思路: 外层循环固定一个元素，内层循环找与 target 的差值，找到则返回下标。
# 复杂度: O(n²) time, O(1) space
def solution_brute(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    # WHY: 外层循环遍历每个元素作为第一个加数
    for i in range(n):
        # WHY: 内层从 i+1 开始，避免重复使用同一元素，避免 (i,j) 和 (j,i) 重复
        for j in range(i + 1, n):
            # WHY: 检查两数之和是否等于目标值
            if nums[i] + nums[j] == target:
                return [i, j]
    # WHY: 根据题意一定存在解，此处返回空列表仅为满足语法
    return []


# ===== 最优解法 =====
# 思路: 遍历数组时，用哈希表存储每个元素的值到索引的映射。
#       对于每个元素 nums[i]，检查 target - nums[i] 是否已在哈希表中。
#       若存在则直接返回，否则将当前元素加入哈希表。
#       相比暴力法用空间换时间，将查找从 O(n) 降为 O(1)。
# 复杂度: O(n) time, O(n) space
def solution_optimal(nums: List[int], target: int) -> List[int]:
    # WHY: 哈希表存储"值 -> 下标"的映射，用于 O(1) 查找 complement
    val_to_idx: Dict[int, int] = {}

    # WHY: 一次遍历，边查边存，保证不会重复使用同一元素
    for i, num in enumerate(nums):
        # WHY: 计算需要找的 complement 值 = target - 当前值
        complement = target - num
        # WHY: 如果 complement 已在哈希表中，说明找到了两个数
        if complement in val_to_idx:
            # WHY: complement 的下标一定在当前下标之前，所以先返回它
            return [val_to_idx[complement], i]
        # WHY: 将当前值存入哈希表，供后续元素查找
        val_to_idx[num] = i

    # WHY: 题目保证有唯一解，此处仅满足类型签名
    return []


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Two Sum...")

    # Test case 1 - 基础用例
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solution_optimal(nums1, target1)
    expected1 = [0, 1]
    # WHY: 验证结果长度和元素值，因为返回顺序可能不同
    print(f"Test 1: {result1} sum={nums1[result1[0]] + nums1[result1[1]]} == {target1} -> {'PASS' if sorted(result1) == sorted(expected1) else 'FAIL'}")

    # Test case 2 - 包含重复值
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = solution_optimal(nums2, target2)
    expected2 = [1, 2]
    print(f"Test 2: {result2} sum={nums2[result2[0]] + nums2[result2[1]]} == {target2} -> {'PASS' if sorted(result2) == sorted(expected2) else 'FAIL'}")

    # Test case 3 - 相同元素
    nums3 = [3, 3]
    target3 = 6
    result3 = solution_optimal(nums3, target3)
    expected3 = [0, 1]
    print(f"Test 3: {result3} sum={nums3[result3[0]] + nums3[result3[1]]} == {target3} -> {'PASS' if sorted(result3) == sorted(expected3) else 'FAIL'}")

    # 验证暴力解法
    print("\nBrute force verification:")
    print(f"Brute Test 1: {solution_brute(nums1, target1)}")
    print(f"Brute Test 2: {solution_brute(nums2, target2)}")
    print(f"Brute Test 3: {solution_brute(nums3, target3)}")

    print("\nAll tests complete!")
