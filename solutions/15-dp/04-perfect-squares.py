"""
LC 279. Perfect Squares (完全平方数)
Difficulty: Medium
Tags: Math, Dynamic Programming, Breadth-First Search
Link: https://leetcode.cn/problems/perfect-squares/
Category: 15-dp
"""


# ===== 暴力解法 =====
# 思路: 递归地尝试减去每个完全平方数，然后求剩余数字的最小个数。对于每个n，减去所有满足j*j<=n的平方数。
# 复杂度: O(n^(n/2)) time, O(n) space (递归栈)
def solution_brute(n: int) -> int:
    # WHY: 如果n为0，不需要任何完全平方数
    if n == 0:
        return 0
    # WHY: 初始化最小个数为正无穷
    min_count = float('inf')
    # WHY: 尝试所有不大于n的完全平方数
    i = 1
    while i * i <= n:
        # WHY: 减去i*i后递归求解剩余部分，加1表示当前这个平方数
        count = 1 + solution_brute(n - i * i)
        # WHY: 更新最小值
        min_count = min(min_count, count)
        i += 1
    # WHY: 返回最小个数
    return int(min_count)


# ===== 最优解法 =====
# 思路: 动态规划，dp[i]表示组成i的最少完全平方数个数。
#        对于每个i，遍历所有j*j <= i，dp[i] = min(dp[i], dp[i-j*j] + 1)。
#        这类似于完全背包问题，每个平方数可以重复使用。
# 复杂度: O(n*sqrt(n)) time, O(n) space
def solution_optimal(n: int) -> int:
    # WHY: dp[i]表示数字i最少需要多少个完全平方数表示
    dp = [float('inf')] * (n + 1)
    # WHY: 0不需要任何平方数
    dp[0] = 0
    # WHY: 遍历1到n，计算每个数字的最少表示
    for i in range(1, n + 1):
        # WHY: 尝试所有不大于i的完全平方数
        j = 1
        while j * j <= i:
            # WHY: 状态转移：dp[i] = min(dp[i], dp[i-j*j] + 1)
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1
    # WHY: 返回n的最少完全平方数个数
    return dp[n]


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Perfect Squares...")

    # 测试用例1: n=12 → 3 (4+4+4)
    test1 = 12
    expected1 = 3
    assert solution_brute(test1) == expected1, f"brute test1 failed"
    assert solution_optimal(test1) == expected1, f"optimal test1 failed"

    # 测试用例2: n=13 → 2 (4+9)
    test2 = 13
    expected2 = 2
    assert solution_brute(test2) == expected2, f"brute test2 failed"
    assert solution_optimal(test2) == expected2, f"optimal test2 failed"

    # 测试用例3: n=0 → 0
    test3 = 0
    expected3 = 0
    assert solution_optimal(test3) == expected3, f"optimal test3 failed"

    print(f"Brute force: {solution_brute(test1)}")
    print("All tests passed!")
