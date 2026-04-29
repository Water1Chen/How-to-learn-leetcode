"""
LC 198. House Robber (打家劫舍)
Difficulty: Medium
Tags: Array, Dynamic Programming
Link: https://leetcode.cn/problems/house-robber/
Category: 15-dp
"""

from typing import List


# ===== 暴力解法 =====
# 思路: 从每个位置开始，递归地考虑抢或不抢当前房子。如果抢当前房子，则跳过下一个；如果不抢，则从下一个开始。
# 复杂度: O(2^n) time, O(n) space (递归栈)
def solution_brute(nums: List[int]) -> int:
    # WHY: 定义递归函数，从第i个房子开始能抢到的最大金额
    def dfs(i: int) -> int:
        # WHY: 如果i超出数组范围，没有房子可抢，返回0
        if i >= len(nums):
            return 0
        # WHY: 选择1：抢当前房子，则跳过下一个房子(不能抢相邻的)
        rob_current = nums[i] + dfs(i + 2)
        # WHY: 选择2：不抢当前房子，从下一个房子开始
        skip_current = dfs(i + 1)
        # WHY: 返回两种选择中的最大值
        return max(rob_current, skip_current)
    # WHY: 从第0个房子开始抢劫
    return dfs(0)


# ===== 最优解法 =====
# 思路: 动态规划，dp[i]表示到第i个房子时能抢到的最大金额。状态转移：dp[i] = max(dp[i-1], dp[i-2] + nums[i])。
#        由于只依赖前两个状态，可以用滚动变量优化空间到O(1)。
# 复杂度: O(n) time, O(1) space
def solution_optimal(nums: List[int]) -> int:
    # WHY: 处理空数组的边界情况
    if not nums:
        return 0
    # WHY: 只有一个房子时直接返回
    if len(nums) == 1:
        return nums[0]
    # WHY: prev2 表示 dp[i-2]（到前两个房子时的最大值）
    prev2 = nums[0]
    # WHY: prev1 表示 dp[i-1]（到前一个房子时的最大值），取前两个房子的最大值
    prev1 = max(nums[0], nums[1])
    # WHY: 从第3个房子（索引2）开始遍历
    for i in range(2, len(nums)):
        # WHY: 状态转移：当前最大值 = max(不抢当前 = prev1, 抢当前 = prev2 + nums[i])
        curr = max(prev1, prev2 + nums[i])
        # WHY: 更新状态，将prev2和prev1向前滚动
        prev2, prev1 = prev1, curr
    # WHY: 最后一个prev1就是到最后一个房子的最大值
    return prev1


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing House Robber...")

    # 测试用例1: [1,2,3,1] → 4 (抢1+3)
    test1 = [1, 2, 3, 1]
    expected1 = 4
    assert solution_brute(test1) == expected1, f"brute test1 failed"
    assert solution_optimal(test1) == expected1, f"optimal test1 failed"

    # 测试用例2: [2,7,9,3,1] → 12 (抢2+9+1)
    test2 = [2, 7, 9, 3, 1]
    expected2 = 12
    assert solution_brute(test2) == expected2, f"brute test2 failed"
    assert solution_optimal(test2) == expected2, f"optimal test2 failed"

    # 测试用例3: 空数组 → 0
    test3: List[int] = []
    expected3 = 0
    assert solution_optimal(test3) == expected3, f"optimal test3 failed"

    # 测试用例4: 单个元素
    test4 = [5]
    expected4 = 5
    assert solution_brute(test4) == expected4, f"brute test4 failed"
    assert solution_optimal(test4) == expected4, f"optimal test4 failed"

    print(f"Brute force: {solution_brute(test1)}")
    print("All tests passed!")
