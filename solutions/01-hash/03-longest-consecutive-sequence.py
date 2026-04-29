"""
LC 128. 最长连续序列 (Longest Consecutive Sequence)
Difficulty: Medium
Tags: Array, Hash Table, Union Find
Link: https://leetcode.cn/problems/longest-consecutive-sequence/
Category: 01-hash
"""

from typing import List, Set


# ===== 暴力解法 =====
# 思路: 先排序，再遍历查找最长连续序列。
#       排序后连续元素会相邻，只需检查相邻差值是否为 1。
# 复杂度: O(n log n) time, O(1) space (若允许原地排序)
def solution_brute(nums: List[int]) -> int:
    # WHY: 空数组没有连续序列，直接返回 0
    if not nums:
        return 0

    # WHY: 排序使连续元素相邻，便于线性扫描
    nums_sorted = sorted(nums)
    # WHY: max_len 记录全局最长长度，cur_len 记录当前连续序列长度
    max_len = 1
    cur_len = 1

    # WHY: 从第二个元素开始遍历，与前一个元素比较
    for i in range(1, len(nums_sorted)):
        # WHY: 相邻元素相等时跳过（重复值不影响连续序列）
        if nums_sorted[i] == nums_sorted[i - 1]:
            continue
        # WHY: 当前值比前一个大 1，说明连续，cur_len 递增
        if nums_sorted[i] == nums_sorted[i - 1] + 1:
            cur_len += 1
        else:
            # WHY: 不连续时更新全局最大值，重置当前长度为 1
            max_len = max(max_len, cur_len)
            cur_len = 1

    # WHY: 循环结束时再更新一次，避免最后一组未统计
    return max(max_len, cur_len)


# ===== 最优解法 =====
# 思路: 用 HashSet 存储所有数字, 只从"连续序列的起点"开始向后查找。
#       一个数是起点当且仅当 num-1 不在集合中。
#       这样每个数最多被访问 2 次（一次检查起点，一次在序列中延伸），总 O(n)。
# 复杂度: O(n) time, O(n) space
def solution_optimal(nums: List[int]) -> int:
    # WHY: 用 HashSet 去重并提供 O(1) 的查找能力
    num_set: Set[int] = set(nums)
    longest = 0

    # WHY: 遍历集合而非原数组，避免重复值带来的冗余判断
    for num in num_set:
        # WHY: 只有 num-1 不在集合中时才算序列起点
        # WHY: 这样保证每个连续序列只被处理一次（从其最小值开始）
        if num - 1 not in num_set:
            current_num = num
            length = 1

            # WHY: 从起点开始不断 +1 检查，统计连续长度
            while current_num + 1 in num_set:
                current_num += 1
                length += 1

            # WHY: 更新全局最长连续长度
            longest = max(longest, length)

    return longest


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Longest Consecutive Sequence...")

    # Test case 1 - 基础用例
    nums1 = [100, 4, 200, 1, 3, 2]
    result1 = solution_optimal(nums1)
    print(f"Test 1: {result1} == 4 -> {'PASS' if result1 == 4 else 'FAIL'}")
    # WHY: 最长连续序列是 [1,2,3,4]

    # Test case 2 - 包含重复值
    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    result2 = solution_optimal(nums2)
    print(f"Test 2: {result2} == 9 -> {'PASS' if result2 == 9 else 'FAIL'}")
    # WHY: 最长连续序列是 [0,1,2,3,4,5,6,7,8]

    # Test case 3 - 空数组
    nums3: List[int] = []
    result3 = solution_optimal(nums3)
    print(f"Test 3: {result3} == 0 -> {'PASS' if result3 == 0 else 'FAIL'}")

    # Test case 4 - 无连续
    nums4 = [1, 3, 5, 7]
    result4 = solution_optimal(nums4)
    print(f"Test 4: {result4} == 1 -> {'PASS' if result4 == 1 else 'FAIL'}")

    # 验证暴力解法
    print("\nBrute force verification:")
    print(f"Brute Test 1: {solution_brute(nums1)}")
    print(f"Brute Test 2: {solution_brute(nums2)}")

    print("\nAll tests complete!")
