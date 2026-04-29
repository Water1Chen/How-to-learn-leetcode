"""
LC 64. Minimum Path Sum (最小路径和)
Difficulty: Medium
Tags: Array, Dynamic Programming, Matrix
Link: https://leetcode.cn/problems/minimum-path-sum/
Category: 16-multi-dp
"""

from typing import List


# ===== 暴力解法 =====
# 思路: 递归，从(0,0)开始，每次向右或向下移动，到达右下角时返回当前路径和，
#        否则返回当前格子的值加上向右和向下路径中的最小值。
# 复杂度: O(2^(m+n)) time, O(m+n) space (递归栈)
def solution_brute(grid: List[List[int]]) -> int:
    # WHY: 获取网格的行数和列数
    m = len(grid)
    n = len(grid[0])

    # WHY: 定义递归函数，从(i,j)出发到达右下角的最小路径和
    def dfs(i: int, j: int) -> int:
        # WHY: 如果到达右下角，返回当前格子的值
        if i == m - 1 and j == n - 1:
            return grid[i][j]
        # WHY: 如果超出边界，返回一个很大的值表示此路不通
        if i >= m or j >= n:
            return float('inf')
        # WHY: 当前格子的值加上向右走和向下走的最小值
        return grid[i][j] + min(dfs(i + 1, j), dfs(i, j + 1))

    # WHY: 从起点(0,0)开始计算
    return dfs(0, 0)


# ===== 最优解法 =====
# 思路: 动态规划，dp[i][j]表示到达(i,j)的最小路径和。
#        dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])。
#        可以直接在原数组上修改（in-place），节省空间。
# 复杂度: O(m*n) time, O(1) space (in-place修改)
def solution_optimal(grid: List[List[int]]) -> int:
    # WHY: 获取网格的行数和列数
    m = len(grid)
    n = len(grid[0])
    # WHY: 初始化第一行：只能从左边来，所以路径和累加
    for j in range(1, n):
        grid[0][j] += grid[0][j - 1]
    # WHY: 初始化第一列：只能从上面来，所以路径和累加
    for i in range(1, m):
        grid[i][0] += grid[i - 1][0]
    # WHY: 从(1,1)开始填表
    for i in range(1, m):
        for j in range(1, n):
            # WHY: 状态转移：当前值 + min(上方, 左方)
            grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
    # WHY: 返回右下角的最小路径和
    return grid[m - 1][n - 1]


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Minimum Path Sum...")

    # 测试用例1: [[1,3,1],[1,5,1],[4,2,1]] → 7 (1→3→1→1→1)
    test1 = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    expected1 = 7
    assert solution_brute(test1) == expected1, f"brute test1 failed"
    assert solution_optimal(test1) == expected1, f"optimal test1 failed"

    # 测试用例2: [[1,2,3],[4,5,6]] → 12 (1→2→3→6)
    test2 = [[1, 2, 3], [4, 5, 6]]
    expected2 = 12
    assert solution_brute(test2) == expected2, f"brute test2 failed"
    assert solution_optimal(test2) == expected2, f"optimal test2 failed"

    # 测试用例3: [[1]] → 1
    test3 = [[1]]
    expected3 = 1
    assert solution_optimal(test3) == expected3, f"optimal test3 failed"

    print(f"Brute force: {solution_brute(test1)}")
    print("All tests passed!")
