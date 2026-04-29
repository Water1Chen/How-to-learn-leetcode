"""
LC 560. 和为 K 的子数组 (Subarray Sum Equals K)
Difficulty: Medium
Tags: Array, Hash Table, Prefix Sum
Link: https://leetcode.cn/problems/subarray-sum-equals-k/
Category: 04-substring
"""

from typing import List, Dict


# ===== 暴力解法 =====
# 思路: 枚举所有子数组，计算每个子数组的和，统计等于 k 的个数。
# 复杂度: O(n²) time, O(1) space
def solution_brute(nums: List[int], k: int) -> int:
    n = len(nums)
    count = 0

    # WHY: 枚举所有子数组的起始位置
    for start in range(n):
        cur_sum = 0
        # WHY: 枚举从 start 开始的所有子数组，逐步扩展并累加
        # WHY: 这样避免了为每个子数组重新求和（相比三重循环的优化）
        for end in range(start, n):
            cur_sum += nums[end]
            # WHY: 如果当前子数组的和等于 k，计数加一
            if cur_sum == k:
                count += 1

    return count


# ===== 最优解法 =====
# 思路: 利用前缀和 + 哈希表。prefix_sum[i] = nums[0] + ... + nums[i-1]。
#       子数组 nums[j..i] 的和 = prefix_sum[i+1] - prefix_sum[j]。
#       遍历时用哈希表记录每个前缀和出现的次数，对每个位置 i，
#       只需查询 prefix_sum - k 在哈希表中的出现次数。
# 复杂度: O(n) time, O(n) space
def solution_optimal(nums: List[int], k: int) -> int:
    # WHY: 哈希表存储"前缀和 -> 出现次数"，用于 O(1) 查询
    # WHY: 初始化 {0: 1} 表示前缀和为 0 出现过 1 次
    # WHY: 这处理了从数组开头到当前元素的子数组之和等于 k 的情况
    prefix_sum_count: Dict[int, int] = {0: 1}
    prefix_sum = 0
    count = 0

    # WHY: 一次遍历，累加前缀和并统计符合条件的子数组个数
    for num in nums:
        # WHY: 更新当前前缀和
        prefix_sum += num

        # WHY: 如果 prefix_sum - k 存在于哈希表中，说明存在以当前元素结尾、
        # WHY: 且和为 k 的子数组（数量等于 prefix_sum - k 的出现次数）
        count += prefix_sum_count.get(prefix_sum - k, 0)

        # WHY: 将当前前缀和加入哈希表，供后续元素查询
        prefix_sum_count[prefix_sum] = prefix_sum_count.get(prefix_sum, 0) + 1

    return count


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Subarray Sum Equals K...")

    # Test case 1 - 基础用例
    nums1 = [1, 1, 1]
    k1 = 2
    result1 = solution_optimal(nums1, k1)
    print(f"Test 1: {result1} == 2 -> {'PASS' if result1 == 2 else 'FAIL'}")
    # WHY: 子数组 [1,1] (0..1) 和 [1,1] (1..2) 的和为 2

    # Test case 2 - 包含负数
    nums2 = [1, 2, 3]
    k2 = 3
    result2 = solution_optimal(nums2, k2)
    print(f"Test 2: {result2} == 2 -> {'PASS' if result2 == 2 else 'FAIL'}")
    # WHY: 子数组 [1,2] (0..1) 和 [3] (2) 的和为 3

    # Test case 3 - 无匹配
    nums3 = [1, 2, 3]
    k3 = 7
    result3 = solution_optimal(nums3, k3)
    print(f"Test 3: {result3} == 0 -> {'PASS' if result3 == 0 else 'FAIL'}")

    # Test case 4 - 负数和零
    nums4 = [-1, -1, 1]
    k4 = 0
    result4 = solution_optimal(nums4, k4)
    print(f"Test 4: {result4} == 1 -> {'PASS' if result4 == 1 else 'FAIL'}")
    # WHY: 子数组 [-1, 1] (1..2) 的和为 0

    # 验证暴力解法
    print("\nBrute force verification:")
    print(f"Brute Test 1: {solution_brute(nums1, k1)}")
    print(f"Brute Test 2: {solution_brute(nums2, k2)}")

    print("\nAll tests complete!")
