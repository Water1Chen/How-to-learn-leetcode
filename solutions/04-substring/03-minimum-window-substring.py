"""
LC 76. 最小覆盖子串 (Minimum Window Substring)
Difficulty: Hard
Tags: Hash Table, String, Sliding Window
Link: https://leetcode.cn/problems/minimum-window-substring/
Category: 04-substring
"""

from typing import Dict


# ===== 暴力解法 =====
# 思路: 枚举所有子串，检查是否包含 t 中所有字符，记录最短的符合条件的子串。
# 复杂度: O(n² · m) time, O(m) space, m = len(t)
def solution_brute(s: str, t: str) -> str:
    n, m = len(s), len(t)

    # WHY: t 比 s 长时不可能有覆盖子串
    if n < m:
        return ""

    min_len = n + 1
    min_start = 0

    # WHY: 辅助函数：检查指定子串 s[start:end+1] 是否包含 t 的所有字符
    def covers(start: int, end: int) -> bool:
        # WHY: 统计 t 中每个字符的需求量
        need: Dict[str, int] = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        # WHY: 遍历子串，减少需求计数
        for i in range(start, end + 1):
            if s[i] in need:
                need[s[i]] -= 1
                # WHY: 如果某个字符的需求量减到 0，从字典中删除
                if need[s[i]] == 0:
                    del need[s[i]]

        # WHY: 如果所有字符都已满足，need 应为空
        return len(need) == 0

    # WHY: 枚举所有可能的子串
    for i in range(n):
        for j in range(i, n):
            # WHY: 如果子串长度已超过当前最短，剪枝
            if j - i + 1 >= min_len:
                break
            # WHY: 检查当前子串是否覆盖 t
            if covers(i, j):
                min_len = j - i + 1
                min_start = i

    return s[min_start:min_start + min_len] if min_len <= n else ""


# ===== 最优解法 =====
# 思路: 可变大小的滑动窗口。用 need 字典统计 t 中字符的需求量（正数表示缺少）。
#       right 指针扩展窗口直到覆盖 t，然后 left 指针收缩窗口以找到最短覆盖子串。
#       valid 变量跟踪当前已满足的字符种类数，避免每次都遍历 need 字典。
# 复杂度: O(n) time, O(m) space, m = len(t)
def solution_optimal(s: str, t: str) -> str:
    n, m = len(s), len(t)

    # WHY: t 比 s 长时不可能有覆盖子串
    if n < m:
        return ""

    # WHY: need 记录 t 中每个字符还缺少多少（正数缺少，负数过剩）
    need: Dict[str, int] = {}
    for ch in t:
        need[ch] = need.get(ch, 0) + 1

    # WHY: 滑动窗口的左右指针
    left = 0
    # WHY: valid 统计已满足"数量需求"的字符种类数
    # WHY: 当一个字符在窗口中的数量 >= 需求量时，该字符被视为"已满足"
    valid = 0

    # WHY: 最小覆盖子串的起始位置和长度
    start = 0
    min_len = n + 1

    # WHY: 扩展窗口右边界
    for right, ch in enumerate(s):
        # WHY: 如果当前字符是 t 中需要的字符
        if ch in need:
            # WHY: 减少该字符的需求量（负数表示窗口中有过剩的该字符）
            need[ch] -= 1
            # WHY: 当某个字符的需求量降为 0，说明该字符已完全满足
            if need[ch] == 0:
                valid += 1

        # WHY: 当所有 t 中的字符都已满足时，尝试收缩左边界
        while valid == len(need):
            # WHY: 更新最小覆盖子串
            if right - left + 1 < min_len:
                min_len = right - left + 1
                start = left

            # WHY: 左指针右移，移出窗口左端字符
            left_ch = s[left]
            left += 1

            # WHY: 如果移出的字符是 t 中需要的
            if left_ch in need:
                # WHY: 当该字符之前恰好满足时（need=0），移出后变为不满足
                if need[left_ch] == 0:
                    valid -= 1
                # WHY: 恢复该字符的需求量（表示重新缺少一个）
                need[left_ch] += 1

    return s[start:start + min_len] if min_len <= n else ""


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Minimum Window Substring...")

    # Test case 1 - 基础用例
    s1 = "ADOBECODEBANC"
    t1 = "ABC"
    result1 = solution_optimal(s1, t1)
    print(f"Test 1: '{result1}' == 'BANC' -> {'PASS' if result1 == 'BANC' else 'FAIL'}")

    # Test case 2 - 单个字符
    s2 = "a"
    t2 = "a"
    result2 = solution_optimal(s2, t2)
    print(f"Test 2: '{result2}' == 'a' -> {'PASS' if result2 == 'a' else 'FAIL'}")

    # Test case 3 - 无匹配
    s3 = "a"
    t3 = "aa"
    result3 = solution_optimal(s3, t3)
    print(f"Test 3: '{result3}' == '' -> {'PASS' if result3 == '' else 'FAIL'}")

    # Test case 4 - 精确匹配
    s4 = "abc"
    t4 = "abc"
    result4 = solution_optimal(s4, t4)
    print(f"Test 4: '{result4}' == 'abc' -> {'PASS' if result4 == 'abc' else 'FAIL'}")

    # Test case 5 - t 中有重复字符
    s5 = "aa"
    t5 = "aa"
    result5 = solution_optimal(s5, t5)
    print(f"Test 5: '{result5}' == 'aa' -> {'PASS' if result5 == 'aa' else 'FAIL'}")

    # 验证暴力解法
    print("\nBrute force verification:")
    print(f"Brute Test 1: '{solution_brute(s1, t1)}'")
    print(f"Brute Test 2: '{solution_brute(s2, t2)}'")

    print("\nAll tests complete!")
