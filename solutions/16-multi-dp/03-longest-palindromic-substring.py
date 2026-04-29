"""
LC 5. Longest Palindromic Substring (最长回文子串)
Difficulty: Medium
Tags: String, Dynamic Programming
Link: https://leetcode.cn/problems/longest-palindromic-substring/
Category: 16-multi-dp
"""


# ===== 方法一：动态规划 =====
# 思路: dp[i][j]表示s[i:j+1]是否是回文串。dp[i][j] = (s[i]==s[j]) and dp[i+1][j-1]。
#        长度为1的子串都是回文，长度为2的看两个字符是否相等。
# 复杂度: O(n^2) time, O(n^2) space
def solution_dp(s: str) -> str:
    # WHY: 处理空字符串或单字符的边界情况
    if len(s) < 2:
        return s
    # WHY: 初始化dp表，dp[i][j]表示s[i:j+1]是否是回文
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    # WHY: 记录最长回文子串的起始和结束索引
    start = 0
    max_len = 1
    # WHY: 所有长度为1的子串都是回文
    for i in range(n):
        dp[i][i] = True
    # WHY: 按长度从2到n遍历所有子串
    for length in range(2, n + 1):
        # WHY: 遍历所有起始位置
        for i in range(n - length + 1):
            # WHY: 计算结束位置
            j = i + length - 1
            # WHY: 长度为2时，直接比较两个字符
            if length == 2:
                dp[i][j] = (s[i] == s[j])
            else:
                # WHY: 长度大于2时，首尾相等且内部子串为回文
                dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]
            # WHY: 如果是回文且长度更大，更新记录
            if dp[i][j] and length > max_len:
                start = i
                max_len = length
    # WHY: 返回最长回文子串
    return s[start:start + max_len]


# ===== 方法二：中心扩展（最优）=====
# 思路: 遍历每个字符，以该字符为中心向两边扩展，检查是否是回文。
#        回文中心可以是一个字符（奇数长度）或两个字符（偶数长度）。
# 复杂度: O(n^2) time, O(1) space
def solution_optimal(s: str) -> str:
    # WHY: 处理空字符串的边界情况
    if not s:
        return ""
    # WHY: 记录最长回文子串的起始和结束索引
    start = 0
    end = 0

    # WHY: 定义中心扩展函数，返回以left,right为中心的最大回文边界
    def expand_around_center(left: int, right: int) -> tuple:
        # WHY: 从中心向两边扩展，直到不能构成回文
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # WHY: 返回回文子串的左右边界（注意循环中多扩展了一步）
        return (left + 1, right - 1)

    # WHY: 遍历每个字符作为回文中心
    for i in range(len(s)):
        # WHY: 奇数长度回文，中心为一个字符
        l1, r1 = expand_around_center(i, i)
        # WHY: 偶数长度回文，中心为两个字符
        l2, r2 = expand_around_center(i, i + 1)
        # WHY: 更新最长回文子串的边界
        if r1 - l1 > end - start:
            start, end = l1, r1
        if r2 - l2 > end - start:
            start, end = l2, r2
    # WHY: 返回最长回文子串
    return s[start:end + 1]


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Longest Palindromic Substring...")

    # 测试用例1: "babad" → "bab" 或 "aba"
    test1 = "babad"
    result1_dp = solution_dp(test1)
    result1_opt = solution_optimal(test1)
    # WHY: "bab"和"aba"都是正确答案
    assert result1_dp in ["bab", "aba"], f"dp test1 failed: {result1_dp}"
    assert result1_opt in ["bab", "aba"], f"optimal test1 failed: {result1_opt}"

    # 测试用例2: "cbbd" → "bb"
    test2 = "cbbd"
    expected2 = "bb"
    assert solution_dp(test2) == expected2, f"dp test2 failed"
    assert solution_optimal(test2) == expected2, f"optimal test2 failed"

    # 测试用例3: "a" → "a"
    test3 = "a"
    expected3 = "a"
    assert solution_dp(test3) == expected3, f"dp test3 failed"
    assert solution_optimal(test3) == expected3, f"optimal test3 failed"

    print(f"DP method: {solution_dp(test1)}")
    print(f"Optimal (center expand): {solution_optimal(test1)}")
    print("All tests passed!")
