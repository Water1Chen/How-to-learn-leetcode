"""
LC 438. 找到字符串中所有字母异位词 (Find All Anagrams in a String)
Difficulty: Medium
Tags: Hash Table, String, Sliding Window
Link: https://leetcode.cn/problems/find-all-anagrams-in-a-string/
Category: 03-sliding-window
"""

from typing import List


# ===== 暴力解法 =====
# 思路: 对每个长度为 len(p) 的子串排序，与排序后的 p 比较。
# 复杂度: O(n · m log m) time, O(m) space, m = len(p)
def solution_brute(s: str, p: str) -> List[int]:
    n, m = len(s), len(p)
    result: List[int] = []

    # WHY: 如果 s 比 p 短，不可能有异位词
    if n < m:
        return []

    # WHY: 排序后的 p 作为比较基准
    sorted_p = sorted(p)

    # WHY: 枚举所有长度为 m 的子串
    for i in range(n - m + 1):
        # WHY: 对子串排序后与 sorted_p 比较
        if sorted(s[i:i + m]) == sorted_p:
            result.append(i)

    return result


# ===== 最优解法 =====
# 思路: 固定大小的滑动窗口。用两个计数数组分别记录 p 和当前窗口的字符频率。
#       每次窗口移动时，只需更新移入/移出的字符，比较两个计数数组是否相等。
#       相比排序 O(m log m)，计数比较只需 O(26) = O(1)。
# 复杂度: O(n) time, O(1) space (计数数组固定 26)
def solution_optimal(s: str, p: str) -> List[int]:
    n, m = len(s), len(p)
    result: List[int] = []

    # WHY: 如果 s 比 p 短，不可能有异位词
    if n < m:
        return []

    # WHY: 长度为 26 的计数数组，分别统计 p 和当前窗口的字符频率
    p_count = [0] * 26
    window_count = [0] * 26

    # WHY: 辅助函数将字符映射到 0-25 的索引
    def idx(ch: str) -> int:
        return ord(ch) - ord('a')

    # WHY: 统计 p 中每个字符的频率
    for ch in p:
        p_count[idx(ch)] += 1

    # WHY: 初始化第一个窗口的字符频率
    for i in range(m):
        window_count[idx(s[i])] += 1

    # WHY: 检查第一个窗口是否匹配
    if window_count == p_count:
        result.append(0)

    # WHY: 滑动窗口，每次移动一步
    for i in range(m, n):
        # WHY: 移入新字符 (s[i])，增加计数
        window_count[idx(s[i])] += 1
        # WHY: 移出旧字符 (s[i - m])，减少计数
        window_count[idx(s[i - m])] -= 1

        # WHY: 比较计数数组是否相等，若相等则找到异位词
        if window_count == p_count:
            # WHY: 当前窗口起始位置为 i - m + 1
            result.append(i - m + 1)

    return result


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Find All Anagrams in a String...")

    # Test case 1 - 基础用例
    s1 = "cbaebabacd"
    p1 = "abc"
    result1 = solution_optimal(s1, p1)
    print(f"Test 1: {result1} == [0, 6] -> {'PASS' if result1 == [0, 6] else 'FAIL'}")
    # WHY: 子串 "cba" (0) 和 "bac" (6) 是 "abc" 的异位词

    # Test case 2 - 连续异位词
    s2 = "abab"
    p2 = "ab"
    result2 = solution_optimal(s2, p2)
    print(f"Test 2: {result2} == [0, 1, 2] -> {'PASS' if result2 == [0, 1, 2] else 'FAIL'}")
    # WHY: "ab"(0), "ba"(1), "ab"(2) 都是 "ab" 的异位词

    # Test case 3 - 无匹配
    s3 = "hello"
    p3 = "abc"
    result3 = solution_optimal(s3, p3)
    print(f"Test 3: {result3} == [] -> {'PASS' if result3 == [] else 'FAIL'}")

    # Test case 4 - s 比 p 短
    s4 = "ab"
    p4 = "abc"
    result4 = solution_optimal(s4, p4)
    print(f"Test 4: {result4} == [] -> {'PASS' if result4 == [] else 'FAIL'}")

    # 验证暴力解法
    print("\nBrute force verification:")
    print(f"Brute Test 1: {solution_brute(s1, p1)}")
    print(f"Brute Test 2: {solution_brute(s2, p2)}")

    print("\nAll tests complete!")
