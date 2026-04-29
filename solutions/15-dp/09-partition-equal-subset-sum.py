"""
LC 416. Partition Equal Subset Sum (分割等和子集)
Difficulty: Medium
Tags: Array, Dynamic Programming
Link: https://leetcode.cn/problems/partition-equal-subset-sum/
Category: 15-dp
"""

from typing import List


# ===== 暴力解法 =====
# 思路: 枚举所有子集，计算每个子集的和，检查是否存在子集的和为总和的一半。
#        使用位运算或递归生成所有子集。
# 复杂度: O(2^n) time, O(n) space (递归栈)
def solution_brute(nums: List[int]) -> bool:
    # WHY: 计算数组总和
    total = sum(nums)
    # WHY: 如果总和为奇数，不可能平分，直接返回False
    if total % 2 != 0:
        return False
    # WHY: 目标和为总和的一半
    target = total // 2

    # WHY: 定义递归函数，从索引i开始选择数字，凑出和为remaining
    def dfs(i: int, remaining: int) -> bool:
        # WHY: 如果剩余目标为0，说明找到了一个子集
        if remaining == 0:
            return True
        # WHY: 如果超出数组范围或剩余目标小于0，剪枝
        if i >= len(nums) or remaining < 0:
            return False
        # WHY: 尝试选择当前数字或跳过当前数字（只要一个为True即可）
        return dfs(i + 1, remaining - nums[i]) or dfs(i + 1, remaining)

    # WHY: 从索引0开始，目标和为target
    return dfs(0, target)


# ===== 最优解法 =====
# 思路: 0-1背包问题，dp[j]表示是否存在子集的和为j。遍历每个数字num，
#        对于每个容量j从target到num，dp[j] = dp[j] or dp[j-num]。
#        因为每个数字只能用一次，所以内层循环需要倒序。
# 复杂度: O(n * target) time, O(target) space
def solution_optimal(nums: List[int]) -> bool:
    # WHY: 计算数组总和
    total = sum(nums)
    # WHY: 如果总和为奇数，不可能平分，直接返回False
    if total % 2 != 0:
        return False
    # WHY: 目标和为总和的一半
    target = total // 2
    # WHY: dp[j]表示是否存在子集的和为j，初始化为False
    dp = [False] * (target + 1)
    # WHY: 空子集的和为0，总是可以实现的
    dp[0] = True
    # WHY: 遍历每个数字
    for num in nums:
        # WHY: 倒序遍历容量，避免重复使用同一个数字（0-1背包特性）
        for j in range(target, num - 1, -1):
            # WHY: 状态转移：不选num或选num
            dp[j] = dp[j] or dp[j - num]
    # WHY: 返回是否能够凑出目标和target
    return dp[target]


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Partition Equal Subset Sum...")

    # 测试用例1: [1,5,11,5] → true (可分割为[1,5,5]和[11])
    test1 = [1, 5, 11, 5]
    expected1 = True
    assert solution_brute(test1) == expected1, f"brute test1 failed"
    assert solution_optimal(test1) == expected1, f"optimal test1 failed"

    # 测试用例2: [1,2,3,5] → false
    test2 = [1, 2, 3, 5]
    expected2 = False
    assert solution_brute(test2) == expected2, f"brute test2 failed"
    assert solution_optimal(test2) == expected2, f"optimal test2 failed"

    # 测试用例3: [2,2,1,1] → true
    test3 = [2, 2, 1, 1]
    expected3 = True
    assert solution_brute(test3) == expected3, f"brute test3 failed"
    assert solution_optimal(test3) == expected3, f"optimal test3 failed"

    print(f"Brute force: {solution_brute(test1)}")
    print("All tests passed!")
