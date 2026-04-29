"""
LC 189. Rotate Array (轮转数组)
Difficulty: Medium
Tags: Array, Math, Two Pointers
Link: https://leetcode.cn/problems/rotate-array/
Category: 05-array
"""

from typing import List


# ===== 暴力解法 =====
# 思路: 创建一个新数组，将每个元素放到它轮转后的位置 (i + k) % n
# 复杂度: O(n) time, O(n) space
def solution_brute(nums: List[int], k: int) -> None:
    # WHY: 使用额外数组存储轮转结果，空间换时间的简单思路
    n = len(nums)
    if n == 0:
        return
    k = k % n  # WHY: 轮转n次等于没轮转，取模简化
    result = [0] * n  # WHY: 创建等长新数组存放轮转结果
    for i in range(n):
        # WHY: 元素nums[i]在轮转k位后应位于索引(i + k) % n
        result[(i + k) % n] = nums[i]
    # WHY: 将结果拷贝回原数组（题目要求原地修改）
    for i in range(n):
        nums[i] = result[i]


# ===== 最优解法 =====
# 思路: 三次反转法 — 先反转整个数组，再反转前k个，再反转后n-k个
#       数学原理: 反转操作可以精确地将元素移动到轮转后的位置
#       例子: [1,2,3,4,5,6,7], k=3
#       全反: [7,6,5,4,3,2,1] → 反前3: [5,6,7,4,3,2,1] → 反后4: [5,6,7,1,2,3,4]
# 复杂度: O(n) time, O(1) space (原地修改)
def solution_optimal(nums: List[int], k: int) -> None:
    # WHY: 三次反转法实现O(1)额外空间，是本题的最优原地解法
    n = len(nums)
    if n == 0:
        return
    k = k % n  # WHY: 轮转n次回到原位，取模减少无意义操作

    # WHY: 定义辅助函数反转数组中指定范围的元素
    def reverse(start: int, end: int) -> None:
        # WHY: 双指针从两端向中间交换，实现原地反转
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]  # WHY: 交换首尾元素
            start += 1  # WHY: 左指针右移
            end -= 1    # WHY: 右指针左移

    # WHY: 第一步：反转整个数组 — 将后半部分元素移到前半部分
    reverse(0, n - 1)
    # WHY: 第二步：反转前k个元素 — 将原本在末尾的k个元素恢复顺序
    reverse(0, k - 1)
    # WHY: 第三步：反转剩余n-k个元素 — 将原本在前面的元素恢复顺序
    reverse(k, n - 1)


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Rotate Array...")

    # 测试用例1: 标准情况
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    k1 = 3
    expected1 = [5, 6, 7, 1, 2, 3, 4]
    solution_optimal(nums1, k1)
    print(f"Test 1: {nums1} == {expected1} -> {'PASS' if nums1 == expected1 else 'FAIL'}")

    # 测试用例2: k大于数组长度
    nums2 = [-1, -100, 3, 99]
    k2 = 5  # WHY: 5 % 4 = 1，等价于轮转1位
    expected2 = [99, -1, -100, 3]
    solution_optimal(nums2, k2)
    print(f"Test 2: {nums2} == {expected2} -> {'PASS' if nums2 == expected2 else 'FAIL'}")

    # 测试用例3: k=0，不轮转
    nums3 = [1, 2, 3]
    k3 = 0
    expected3 = [1, 2, 3]
    solution_optimal(nums3, k3)
    print(f"Test 3: {nums3} == {expected3} -> {'PASS' if nums3 == expected3 else 'FAIL'}")

    # 测试用例4: 单个元素
    nums4 = [42]
    k4 = 100
    expected4 = [42]
    solution_optimal(nums4, k4)
    print(f"Test 4: {nums4} == {expected4} -> {'PASS' if nums4 == expected4 else 'FAIL'}")

    print("\nAll tests complete!")
