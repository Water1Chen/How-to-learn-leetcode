"""
LC 322. Coin Change (零钱兑换)
Difficulty: Medium
Tags: Breadth-First Search, Dynamic Programming, Array
Link: https://leetcode.cn/problems/coin-change/
Category: 15-dp
"""

from typing import List


# ===== 暴力解法 =====
# 思路: 递归尝试每种硬币，每次选择一个硬币并减小目标金额，直到金额为0。
#        对于每个amount，遍历所有硬币，递归求解amount-coin的最小硬币数。
# 复杂度: O(amount^n) time, O(amount) space (递归栈)
def solution_brute(coins: List[int], amount: int) -> int:
    # WHY: 如果金额为0，不需要任何硬币
    if amount == 0:
        return 0
    # WHY: 如果金额小于0，无法凑出，返回-1
    if amount < 0:
        return -1
    # WHY: 初始化最小硬币数为正无穷
    min_coins = float('inf')
    # WHY: 遍历所有硬币面值
    for coin in coins:
        # WHY: 递归求解剩余金额的最小硬币数
        sub = solution_brute(coins, amount - coin)
        # WHY: 如果剩余金额有解，更新最小硬币数（加1表示当前这枚硬币）
        if sub != -1:
            min_coins = min(min_coins, sub + 1)
    # WHY: 如果最小硬币数仍是正无穷，说明无解，返回-1；否则返回最小硬币数
    return -1 if min_coins == float('inf') else int(min_coins)


# ===== 最优解法 =====
# 思路: 动态规划，dp[i]表示凑出金额i所需的最少硬币数。
#        对于每个金额i，遍历所有硬币coin，dp[i] = min(dp[i], dp[i-coin] + 1)。
#        这是一个完全背包问题，每个硬币可以无限使用。
# 复杂度: O(amount * len(coins)) time, O(amount) space
def solution_optimal(coins: List[int], amount: int) -> int:
    # WHY: dp[i]表示凑出金额i所需的最少硬币数，初始化为一个很大的值
    dp = [amount + 1] * (amount + 1)
    # WHY: 凑出金额0需要0个硬币
    dp[0] = 0
    # WHY: 遍历所有金额从1到amount
    for i in range(1, amount + 1):
        # WHY: 尝试每种硬币
        for coin in coins:
            # WHY: 如果当前硬币面值不超过当前金额
            if coin <= i:
                # WHY: 状态转移：dp[i] = min(dp[i], dp[i-coin] + 1)
                dp[i] = min(dp[i], dp[i - coin] + 1)
    # WHY: 如果dp[amount]仍为初始值，说明无法凑出，返回-1；否则返回最少硬币数
    return -1 if dp[amount] == amount + 1 else dp[amount]


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Coin Change...")

    # 测试用例1: coins=[1,2,5], amount=11 → 3 (5+5+1)
    test_coins1 = [1, 2, 5]
    test_amount1 = 11
    expected1 = 3
    assert solution_brute(test_coins1, test_amount1) == expected1, f"brute test1 failed"
    assert solution_optimal(test_coins1, test_amount1) == expected1, f"optimal test1 failed"

    # 测试用例2: coins=[2], amount=3 → -1 (无法凑出)
    test_coins2 = [2]
    test_amount2 = 3
    expected2 = -1
    assert solution_brute(test_coins2, test_amount2) == expected2, f"brute test2 failed"
    assert solution_optimal(test_coins2, test_amount2) == expected2, f"optimal test2 failed"

    # 测试用例3: coins=[1], amount=0 → 0
    test_coins3 = [1]
    test_amount3 = 0
    expected3 = 0
    assert solution_optimal(test_coins3, test_amount3) == expected3, f"optimal test3 failed"

    print(f"Brute force: {solution_brute(test_coins1, test_amount1)}")
    print("All tests passed!")
