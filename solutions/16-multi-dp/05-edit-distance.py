"""
LC 72. Edit Distance (编辑距离)
Difficulty: Medium
Tags: String, Dynamic Programming
Link: https://leetcode.cn/problems/edit-distance/
Category: 16-multi-dp
"""


# ===== 暴力解法 =====
# 思路: 递归，比较两个字符串的末尾字符。如果相等，跳过继续比较；
#        如果不相等，分别尝试插入、删除、替换三种操作，取最小操作次数加1。
# 复杂度: O(3^(m+n)) time, O(m+n) space (递归栈)
def solution_brute(word1: str, word2: str) -> int:
    # WHY: 定义递归函数，求word1[:i+1]到word2[:j+1]的编辑距离
    def min_distance(i: int, j: int) -> int:
        # WHY: 如果word1为空，需要插入word2中的所有剩余字符
        if i < 0:
            return j + 1
        # WHY: 如果word2为空，需要删除word1中的所有剩余字符
        if j < 0:
            return i + 1
        # WHY: 如果当前字符相等，不需要操作，直接比较前一个字符
        if word1[i] == word2[j]:
            return min_distance(i - 1, j - 1)
        else:
            # WHY: 当前字符不相等，三种操作取最小值
            # WHY: 插入：在word1中插入word2[j]（word1的i不变，word2的j-1）
            insert = min_distance(i, j - 1)
            # WHY: 删除：删除word1[i]（word1的i-1，word2的j不变）
            delete = min_distance(i - 1, j)
            # WHY: 替换：将word1[i]替换为word2[j]（两者都-1）
            replace = min_distance(i - 1, j - 1)
            # WHY: 返回最小操作次数加1（当前这一步操作）
            return 1 + min(insert, delete, replace)

    # WHY: 从两个字符串的末尾开始计算
    return min_distance(len(word1) - 1, len(word2) - 1)


# ===== 最优解法 =====
# 思路: 二维动态规划，dp[i][j]表示word1[:i]到word2[:j]的最小编辑距离。
#        如果word1[i-1] == word2[j-1]，则dp[i][j] = dp[i-1][j-1]；
#        否则dp[i][j] = 1 + min(dp[i][j-1](插入), dp[i-1][j](删除), dp[i-1][j-1](替换))。
# 复杂度: O(m*n) time, O(m*n) space（可优化为O(n)）
def solution_optimal(word1: str, word2: str) -> int:
    # WHY: 获取两个字符串的长度
    m, n = len(word1), len(word2)
    # WHY: 创建(m+1)*(n+1)的dp表
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # WHY: 初始化第一列：word1删除所有字符变成空串
    for i in range(1, m + 1):
        dp[i][0] = i
    # WHY: 初始化第一行：空串插入所有字符变成word2
    for j in range(1, n + 1):
        dp[0][j] = j
    # WHY: 遍历所有状态
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # WHY: 如果当前字符相等，编辑距离等于前一个状态的编辑距离
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # WHY: 不相等时，三种操作取最小值加1
                dp[i][j] = 1 + min(
                    dp[i][j - 1],      # 插入：word1插入word2[j]后匹配
                    dp[i - 1][j],      # 删除：删除word1[i]
                    dp[i - 1][j - 1]   # 替换：将word1[i]替换为word2[j]
                )
    # WHY: 返回完整字符串的编辑距离
    return dp[m][n]


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Edit Distance...")

    # 测试用例1: word1="horse", word2="ros" → 3
    # horse → rorse (替换h→r) → rose (删除r) → ros (删除e)
    test1_w1 = "horse"
    test1_w2 = "ros"
    expected1 = 3
    assert solution_brute(test1_w1, test1_w2) == expected1, f"brute test1 failed"
    assert solution_optimal(test1_w1, test1_w2) == expected1, f"optimal test1 failed"

    # 测试用例2: word1="intention", word2="execution" → 5
    test2_w1 = "intention"
    test2_w2 = "execution"
    expected2 = 5
    assert solution_brute(test2_w1, test2_w2) == expected2, f"brute test2 failed"
    assert solution_optimal(test2_w1, test2_w2) == expected2, f"optimal test2 failed"

    # 测试用例3: word1="", word2="" → 0
    test3_w1 = ""
    test3_w2 = ""
    expected3 = 0
    assert solution_brute(test3_w1, test3_w2) == expected3, f"brute test3 failed"
    assert solution_optimal(test3_w1, test3_w2) == expected3, f"optimal test3 failed"

    print(f"Brute force: {solution_brute(test1_w1, test1_w2)}")
    print("All tests passed!")
