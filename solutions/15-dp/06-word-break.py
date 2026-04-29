"""
LC 139. Word Break (单词拆分)
Difficulty: Medium
Tags: Trie, Memoization, Hash Table, String, Dynamic Programming
Link: https://leetcode.cn/problems/word-break/
Category: 15-dp
"""

from typing import List


# ===== 暴力解法 =====
# 思路: 递归回溯，从字符串起始位置开始，尝试所有可能的单词匹配。
#        每次匹配一个单词后，递归检查剩余子串是否能被拆分为字典中的单词。
# 复杂度: O(2^n) time, O(n) space (递归栈)
def solution_brute(s: str, wordDict: List[str]) -> bool:
    # WHY: 将字典转为集合，便于O(1)查找
    word_set = set(wordDict)

    # WHY: 定义递归函数，检查从start位置开始的子串能否被拆分
    def backtrack(start: int) -> bool:
        # WHY: 如果到达字符串末尾，说明成功拆分所有部分
        if start == len(s):
            return True
        # WHY: 从start开始尝试所有可能的结束位置
        for end in range(start + 1, len(s) + 1):
            # WHY: 如果s[start:end]在字典中，递归检查剩余部分
            if s[start:end] in word_set:
                if backtrack(end):
                    return True
        # WHY: 所有尝试都失败，返回False
        return False

    # WHY: 从字符串开头开始检查
    return backtrack(0)


# ===== 最优解法 =====
# 思路: 动态规划，dp[i]表示s[0:i]是否可以被拆分为字典中的单词。
#        对于每个位置i，检查所有j < i，如果dp[j]为True且s[j:i]在字典中，则dp[i]为True。
# 复杂度: O(n^2) time, O(n) space
def solution_optimal(s: str, wordDict: List[str]) -> bool:
    # WHY: 将字典转为集合，便于O(1)查找
    word_set = set(wordDict)
    # WHY: dp[i]表示s的前i个字符s[0:i]是否可以被拆分
    dp = [False] * (len(s) + 1)
    # WHY: 空字符串可以被拆分
    dp[0] = True
    # WHY: 遍历所有结束位置i（从1到n）
    for i in range(1, len(s) + 1):
        # WHY: 遍历所有可能的分割点j（从0到i-1）
        for j in range(i):
            # WHY: 如果s[0:j]可拆分且s[j:i]在字典中
            if dp[j] and s[j:i] in word_set:
                # WHY: 标记s[0:i]可拆分，并跳出内层循环
                dp[i] = True
                break
    # WHY: 返回整个字符串是否可拆分
    return dp[len(s)]


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Word Break...")

    # 测试用例1: s="leetcode", dict=["leet","code"] → true
    test_s1 = "leetcode"
    test_dict1 = ["leet", "code"]
    expected1 = True
    assert solution_brute(test_s1, test_dict1) == expected1, f"brute test1 failed"
    assert solution_optimal(test_s1, test_dict1) == expected1, f"optimal test1 failed"

    # 测试用例2: s="applepenapple", dict=["apple","pen"] → true
    test_s2 = "applepenapple"
    test_dict2 = ["apple", "pen"]
    expected2 = True
    assert solution_brute(test_s2, test_dict2) == expected2, f"brute test2 failed"
    assert solution_optimal(test_s2, test_dict2) == expected2, f"optimal test2 failed"

    # 测试用例3: s="catsandog", dict=["cats","dog","sand","and","cat"] → false
    test_s3 = "catsandog"
    test_dict3 = ["cats", "dog", "sand", "and", "cat"]
    expected3 = False
    assert solution_brute(test_s3, test_dict3) == expected3, f"brute test3 failed"
    assert solution_optimal(test_s3, test_dict3) == expected3, f"optimal test3 failed"

    print(f"Brute force: {solution_brute(test_s1, test_dict1)}")
    print("All tests passed!")
