"""
LC 62. Unique Paths (不同路径)
Difficulty: Medium
Tags: Math, Combinatorics, Dynamic Programming
Link: https://leetcode.cn/problems/unique-paths/
Category: 16-multi-dp
"""


# ===== 暴力解法 =====
# 思路: 递归，从(0,0)出发，每次只能向右或向下移动。到达(m-1,n-1)时返回1，
#        否则递归计算从右方和下方出发的路径数之和。
# 复杂度: O(2^(m+n)) time, O(m+n) space (递归栈)
def solution_brute(m: int, n: int) -> int:
    # WHY: 定义递归函数，从(i,j)出发到达右下角的路径数
    def dfs(i: int, j: int) -> int:
        # WHY: 如果到达右下角，找到一条路径
        if i == m - 1 and j == n - 1:
            return 1
        # WHY: 如果超出边界，返回0
        if i >= m or j >= n:
            return 0
        # WHY: 路径数等于向右走的路径数加上向下走的路径数
        return dfs(i + 1, j) + dfs(i, j + 1)
    # WHY: 从起点(0,0)开始计算
    return dfs(0, 0)


# ===== 最优解法 =====
# 思路: 动态规划，dp[i][j]表示到达位置(i,j)的路径数。
#        由于只能向右或向下移动，dp[i][j] = dp[i-1][j] + dp[i][j-1]。
#        可以用一维数组优化空间，dp[j] = dp[j] + dp[j-1]。
# 复杂度: O(m*n) time, O(n) space
def solution_optimal(m: int, n: int) -> int:
    # WHY: dp[j]表示到达当前行第j列的路径数，初始化为第一行（全为1）
    dp = [1] * n
    # WHY: 从第二行开始遍历（第0行已经初始化）
    for i in range(1, m):
        # WHY: 遍历每一列，第一列始终为1（只能从上面来）
        for j in range(1, n):
            # WHY: dp[j] = 上方路径数(dp[j]) + 左方路径数(dp[j-1])
            dp[j] = dp[j] + dp[j - 1]
    # WHY: 返回右下角的路径数
    return dp[n - 1]


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Unique Paths...")

    # 测试用例1: m=3, n=7 → 28
    assert solution_brute(3, 7) == 28, f"brute test1 failed"
    assert solution_optimal(3, 7) == 28, f"optimal test1 failed"

    # 测试用例2: m=3, n=2 → 3
    assert solution_brute(3, 2) == 3, f"brute test2 failed"
    assert solution_optimal(3, 2) == 3, f"optimal test2 failed"

    # 测试用例3: m=1, n=1 → 1
    assert solution_optimal(1, 1) == 1, f"optimal test3 failed"

    print(f"Brute force: {solution_brute(3, 7)}")
    print("All tests passed!")
