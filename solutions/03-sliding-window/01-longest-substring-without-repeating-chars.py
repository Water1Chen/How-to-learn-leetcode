"""
LC 3. 无重复字符的最长子串 (Longest Substring Without Repeating Characters)
Difficulty: Medium
Tags: Hash Table, String, Sliding Window
Link: https://leetcode.cn/problems/longest-substring-without-repeating-characters/
Category: 03-sliding-window
"""

from typing import Dict


# ===== 暴力解法 =====
# 思路: 枚举所有子串，对每个子串用集合检查是否有重复字符，记录最长长度。
# 复杂度: O(n³) time, O(k) space, k 为字符集大小
def solution_brute(s: str) -> int:
    n = len(s)
    max_len = 0

    # WHY: 枚举所有可能的子串起始位置
    for i in range(n):
        # WHY: 枚举所有可能的子串结束位置
        for j in range(i, n):
            # WHY: 用集合检查子串 s[i:j+1] 中是否有重复字符
            char_set = set()
            is_unique = True
            for k in range(i, j + 1):
                if s[k] in char_set:
                    is_unique = False
                    break
                char_set.add(s[k])
            # WHY: 如果无重复字符，更新最长长度
            if is_unique:
                max_len = max(max_len, j - i + 1)

    return max_len


# ===== 最优解法 =====
# 思路: 滑动窗口 + HashMap 记录每个字符最近出现的位置。
#       right 指针扩展窗口，当遇到重复字符时，left 直接跳到重复字符上次出现位置 +1。
#       这样窗口始终保持无重复字符，right - left 就是当前候选长度。
# 复杂度: O(n) time, O(k) space, k 为字符集大小
def solution_optimal(s: str) -> int:
    # WHY: 哈希表存储每个字符最近一次出现时右侧的下标（即重复时 left 要跳到的地方）
    # WHY: 存储 index+1 而非 index 是为了在重复时直接跳到重复字符之后
    char_to_next: Dict[str, int] = {}
    max_len = 0
    left = 0

    # WHY: right 指针遍历字符串，负责扩展窗口右边界
    for right, ch in enumerate(s):
        # WHY: 如果当前字符已在窗口内，将 left 移到上次出现位置的下一个位置
        # WHY: max 防止 left 回退（比如重复字符在 left 左边但已被跳过）
        if ch in char_to_next:
            left = max(left, char_to_next[ch])

        # WHY: 更新当前无重复子串的长度
        max_len = max(max_len, right - left + 1)

        # WHY: 记录当前字符下次出现时 left 应跳到的位置（当前下标 + 1）
        char_to_next[ch] = right + 1

    return max_len


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Longest Substring Without Repeating Characters...")

    # Test case 1 - 基础用例
    s1 = "abcabcbb"
    result1 = solution_optimal(s1)
    print(f"Test 1: {result1} == 3 -> {'PASS' if result1 == 3 else 'FAIL'}")
    # WHY: 最长子串是 "abc"，长度为 3

    # Test case 2 - 全相同字符
    s2 = "bbbbb"
    result2 = solution_optimal(s2)
    print(f"Test 2: {result2} == 1 -> {'PASS' if result2 == 1 else 'FAIL'}")

    # Test case 3 - 无重复
    s3 = "abcdef"
    result3 = solution_optimal(s3)
    print(f"Test 3: {result3} == 6 -> {'PASS' if result3 == 6 else 'FAIL'}")

    # Test case 4 - 空字符串
    s4 = ""
    result4 = solution_optimal(s4)
    print(f"Test 4: {result4} == 0 -> {'PASS' if result4 == 0 else 'FAIL'}")

    # Test case 5 - 重复字符在窗口外
    s5 = "abba"
    result5 = solution_optimal(s5)
    print(f"Test 5: {result5} == 2 -> {'PASS' if result5 == 2 else 'FAIL'}")
    # WHY: 最长子串是 "ab" 或 "ba"，长度为 2

    # 验证暴力解法
    print("\nBrute force verification:")
    print(f"Brute Test 1: {solution_brute(s1)}")
    print(f"Brute Test 2: {solution_brute(s2)}")

    print("\nAll tests complete!")
