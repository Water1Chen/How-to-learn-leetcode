"""
LC 300. Longest Increasing Subsequence (最长递增子序列)
Difficulty: Medium
Tags: Binary Search, Array, Dynamic Programming
Link: https://leetcode.cn/problems/longest-increasing-subsequence/
Category: 15-dp
"""

from typing import List
import bisect


# ===== 解法一：动态规划 =====
# 思路: dp[i]表示以nums[i]结尾的最长递增子序列的长度。对于每个i，遍历所有j < i，
#        如果nums[j] < nums[i]，则dp[i] = max(dp[i], dp[j] + 1)。
# 复杂度: O(n^2) time, O(n) space
def solution_dp(nums: List[int]) -> int:
    # WHY: 处理空数组的情况
    if not nums:
        return 0
    # WHY: dp[i]表示以nums[i]结尾的最长递增子序列长度，初始化为1（自身）
    dp = [1] * len(nums)
    # WHY: 记录全局最大长度
    max_len = 1
    # WHY: 遍历每个位置作为子序列结尾
    for i in range(len(nums)):
        # WHY: 检查所有在i之前的位置
        for j in range(i):
            # WHY: 如果nums[j] < nums[i]，nums[i]可以接在nums[j]后面形成更长的子序列
            if nums[j] < nums[i]:
                # WHY: 状态转移：更新以nums[i]结尾的最长长度
                dp[i] = max(dp[i], dp[j] + 1)
        # WHY: 更新全局最大长度
        max_len = max(max_len, dp[i])
    # WHY: 返回最长递增子序列的长度
    return max_len


# ===== 解法二：贪心 + 二分查找（最优）=====
# 思路: 维护一个tails数组，tails[i]表示长度为i+1的递增子序列的最小末尾元素。
#        使用patience sorting（耐心排序）的思想，对每个元素二分查找其在tails中的位置。
#        这样可以保证tails保持递增，且长度即为LIS的长度。
# 复杂度: O(n log n) time, O(n) space
def solution_optimal(nums: List[int]) -> int:
    # WHY: 处理空数组的情况
    if not nums:
        return 0
    # WHY: tails[i]存储长度为i+1的递增子序列的最小末尾元素
    tails: List[int] = []
    # WHY: 遍历每个数字
    for num in nums:
        # WHY: 二分查找num在tails中应插入的位置（第一个 >= num的位置）
        pos = bisect.bisect_left(tails, num)
        # WHY: 如果pos等于tails长度，说明num比所有tails末尾元素都大，可以延长子序列
        if pos == len(tails):
            tails.append(num)
        else:
            # WHY: 否则用num替换tails[pos]，更新该长度下的最小末尾元素
            tails[pos] = num
    # WHY: tails的长度就是最长递增子序列的长度
    return len(tails)


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Longest Increasing Subsequence...")

    # 测试用例1: [10,9,2,5,3,7,101,18] → 4 ([2,3,7,101])
    test1 = [10, 9, 2, 5, 3, 7, 101, 18]
    expected1 = 4
    assert solution_dp(test1) == expected1, f"dp test1 failed"
    assert solution_optimal(test1) == expected1, f"optimal test1 failed"

    # 测试用例2: [0,1,0,3,2,3] → 4
    test2 = [0, 1, 0, 3, 2, 3]
    expected2 = 4
    assert solution_dp(test2) == expected2, f"dp test2 failed"
    assert solution_optimal(test2) == expected2, f"optimal test2 failed"

    # 测试用例3: [7,7,7,7,7,7] → 1 (严格递增，相等不算)
    test3 = [7, 7, 7, 7, 7, 7]
    expected3 = 1
    assert solution_dp(test3) == expected3, f"dp test3 failed"
    assert solution_optimal(test3) == expected3, f"optimal test3 failed"

    print(f"DP method: {solution_dp(test1)}")
    print(f"Optimal (binary search): {solution_optimal(test1)}")
    print("All tests passed!")
