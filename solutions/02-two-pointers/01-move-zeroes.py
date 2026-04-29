"""
LC 283. 移动零 (Move Zeroes)
Difficulty: Easy
Tags: Array, Two Pointers
Link: https://leetcode.cn/problems/move-zeroes/
Category: 02-two-pointers
"""

from typing import List


# ===== 暴力解法 =====
# 思路: 创建新数组，遍历原数组将非零元素依次放入，剩余位置补零。
# 复杂度: O(n) time, O(n) space
def solution_brute(nums: List[int]) -> None:
    # WHY: 创建新数组来保存结果，避免原地操作复杂度
    result = [0] * len(nums)
    idx = 0
    # WHY: 将非零元素按顺序放入新数组
    for num in nums:
        if num != 0:
            result[idx] = num
            idx += 1
    # WHY: 将结果写回原数组（函数要求原地修改）
    for i in range(len(nums)):
        nums[i] = result[i]


# ===== 最优解法 =====
# 思路: 双指针，slow 指向当前可放置非零元素的位置，fast 遍历数组。
#       fast 遇到非零时与 slow 交换（或赋值），slow 前移。
#       这样所有非零元素被移到前面，零自然沉淀到末尾。
#       相比暴力法省去了额外 O(n) 空间。
# 复杂度: O(n) time, O(1) space
def solution_optimal(nums: List[int]) -> None:
    # WHY: slow 指针指向下一个非零元素应该放置的位置
    slow = 0

    # WHY: fast 指针遍历整个数组
    for fast in range(len(nums)):
        # WHY: 遇到非零元素时，移到 slow 位置
        if nums[fast] != 0:
            # WHY: slow != fast 时才交换，避免自己与自己交换的无效操作
            if slow != fast:
                # WHY: 交换使非零元素移到前面，零移到后面
                nums[slow], nums[fast] = nums[fast], nums[slow]
            # WHY: slow 前移，指向下一个待放置位置
            slow += 1
    # WHY: 循环结束后，所有非零元素已按顺序排列在前部
    # WHY: 剩余位置（从 slow 到末尾）自然都是零


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Move Zeroes...")

    # Test case 1 - 基础用例
    nums1 = [0, 1, 0, 3, 12]
    expected1 = [1, 3, 12, 0, 0]
    solution_optimal(nums1)
    print(f"Test 1: {nums1} == {expected1} -> {'PASS' if nums1 == expected1 else 'FAIL'}")

    # Test case 2 - 全零
    nums2 = [0, 0, 0]
    expected2 = [0, 0, 0]
    solution_optimal(nums2)
    print(f"Test 2: {nums2} == {expected2} -> {'PASS' if nums2 == expected2 else 'FAIL'}")

    # Test case 3 - 无零
    nums3 = [1, 2, 3]
    expected3 = [1, 2, 3]
    solution_optimal(nums3)
    print(f"Test 3: {nums3} == {expected3} -> {'PASS' if nums3 == expected3 else 'FAIL'}")

    # Test case 4 - 空数组
    nums4: List[int] = []
    expected4: List[int] = []
    solution_optimal(nums4)
    print(f"Test 4: {nums4} == {expected4} -> {'PASS' if nums4 == expected4 else 'FAIL'}")

    # 验证暴力解法
    print("\nBrute force verification:")
    nums_brute = [0, 1, 0, 3, 12]
    solution_brute(nums_brute)
    print(f"Brute Test 1: {nums_brute}")

    print("\nAll tests complete!")
