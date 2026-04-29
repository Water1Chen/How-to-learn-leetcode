"""
LC 1143. Longest Common Subsequence (最长公共子序列)
Difficulty: Medium
Tags: String, Dynamic Programming
Link: https://leetcode.cn/problems/longest-common-subsequence/
Category: 16-multi-dp
"""


# ===== 暴力解法 =====
# 思路: 递归，比较两个字符串的末尾字符。如果相等，则LCS长度加1并同时缩短两个字符串；
#        如果不相等，则分别尝试缩短其中一个字符串，取最大值。
# 复杂度: O(2^(m+n)) time, O(m+n) space (递归栈)
def solution_brute(text1: str, text2: str) -> int:
    # WHY: 定义递归函数，求text1[:i+1]和text2[:j+1]的LCS长度
    def lcs(i: int, j: int) -> int:
        # WHY: 如果任一字符串为空，LCS长度为0
        if i < 0 or j < 0:
            return 0
        # WHY: 如果末尾字符相等，LCS长度加1
        if text1[i] == text2[j]:
            return 1 + lcs(i - 1, j - 1)
        else:
            # WHY: 末尾字符不相等，尝试跳过text1或text2的末尾字符，取较大值
            return max(lcs(i - 1, j), lcs(i, j - 1))
    # WHY: 从两个字符串的末尾开始计算
    return lcs(len(text1) - 1, len(text2) - 1)


# ===== 最优解法 =====
# 思路: 二维动态规划，dp[i][j]表示text1[:i]和text2[:j]的最长公共子序列长度。
#        如果text1[i-1] == text2[j-1]，则dp[i][j] = dp[i-1][j-1] + 1；
#        否则dp[i][j] = max(dp[i-1][j], dp[i][j-1])。
# 复杂度: O(m*n) time, O(m*n) space（可优化为O(min(m,n))）
def solution_optimal(text1: str, text2: str) -> int:
    # WHY: 获取两个字符串的长度
    m, n = len(text1), len(text2)
    # WHY: 创建(m+1)*(n+1)的dp表，多出一行一列作为空串的边界
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # WHY: 遍历text1的每个字符（从1开始，0表示空串）
    for i in range(1, m + 1):
        # WHY: 遍历text2的每个字符
        for j in range(1, n + 1):
            # WHY: 如果当前字符相等，LCS长度加1
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # WHY: 不相等时，取删除一个字符后的较大值
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    # WHY: 返回整个字符串的LCS长度
    return dp[m][n]


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Longest Common Subsequence...")

    # 测试用例1: text1="abcde", text2="ace" → 3 ("ace")
    test1_t1 = "abcde"
    test1_t2 = "ace"
    expected1 = 3
    assert solution_brute(test1_t1, test1_t2) == expected1, f"brute test1 failed"
    assert solution_optimal(test1_t1, test1_t2) == expected1, f"optimal test1 failed"

    # 测试用例2: text1="abc", text2="abc" → 3 ("abc")
    test2_t1 = "abc"
    test2_t2 = "abc"
    expected2 = 3
    assert solution_brute(test2_t1, test2_t2) == expected2, f"brute test2 failed"
    assert solution_optimal(test2_t1, test2_t2) == expected2, f"optimal test2 failed"

    # 测试用例3: text1="abc", text2="def" → 0 (无公共子序列)
    test3_t1 = "abc"
    test3_t2 = "def"
    expected3 = 0
    assert solution_brute(test3_t1, test3_t2) == expected3, f"brute test3 failed"
    assert solution_optimal(test3_t1, test3_t2) == expected3, f"optimal test3 failed"

    print(f"Brute force: {solution_brute(test1_t1, test1_t2)}")
    print("All tests passed!")
