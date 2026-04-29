"""
LC 49. 字母异位词分组 (Group Anagrams)
Difficulty: Medium
Tags: Array, Hash Table, String, Sorting
Link: https://leetcode.cn/problems/group-anagrams/
Category: 01-hash
"""

from typing import List, Dict, Tuple
from collections import defaultdict


# ===== 暴力解法 =====
# 思路: 对每个字符串排序，用排序后的结果作为 key 分组。
#       排序可唯一标识一组字母异位词。
# 复杂度: O(n · m log m) time, O(n · m) space，m 为字符串平均长度
def solution_brute(strs: List[str]) -> List[List[str]]:
    # WHY: defaultdict 避免手动检查 key 是否存在，自动初始化为空列表
    groups: Dict[str, List[str]] = defaultdict(list)

    # WHY: 遍历每个字符串，用排序后的形式作为异位词的统一标识
    for s in strs:
        # WHY: 排序将字母重排为固定顺序，所有异位词排序后得到相同结果
        key = ''.join(sorted(s))
        groups[key].append(s)

    # WHY: 返回所有分组，每个分组是一个列表
    return list(groups.values())


# ===== 最优解法 =====
# 思路: 用长度为 26 的计数数组代替排序，将计数元组作为 key。
#       相比排序 O(m log m)，计数只需 O(m)，总复杂度降为 O(n·m)。
# 复杂度: O(n · m) time, O(n · m) space，m 为字符串平均长度
def solution_optimal(strs: List[str]) -> List[List[str]]:
    # WHY: defaultdict 自动处理 key 不存在的情况，简化分组逻辑
    groups: Dict[Tuple[int, ...], List[str]] = defaultdict(list)

    # WHY: 遍历每个字符串，用字符计数元组作为 key
    for s in strs:
        # WHY: 长度为 26 的计数数组，对应 26 个小写字母
        counts = [0] * 26

        # WHY: 统计每个字符出现的次数
        for ch in s:
            # WHY: ord(ch) - ord('a') 将字母 a-z 映射到 0-25 的索引
            counts[ord(ch) - ord('a')] += 1

        # WHY: 元组可哈希且不可变，适合作为字典 key；列表不可哈希
        key = tuple(counts)
        groups[key].append(s)

    # WHY: 返回所有字母异位词分组
    return list(groups.values())


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Group Anagrams...")

    # Test case 1 - 基础用例
    strs1 = ["eat","tea","tan","ate","nat","bat"]
    result1 = solution_optimal(strs1)
    # WHY: 将每组内部排序后整体排序，避免顺序影响比较
    sorted_result1 = sorted([sorted(group) for group in result1])
    expected1 = sorted([["bat"],["nat","tan"],["ate","eat","tea"]])
    sorted_expected1 = sorted([sorted(group) for group in expected1])
    print(f"Test 1: {sorted_result1} == {sorted_expected1} -> {'PASS' if sorted_result1 == sorted_expected1 else 'FAIL'}")

    # Test case 2 - 空字符串
    strs2 = [""]
    result2 = solution_optimal(strs2)
    print(f"Test 2: {result2} == {[['']]} -> {'PASS' if result2 == [['']] else 'FAIL'}")

    # Test case 3 - 单个字符
    strs3 = ["a"]
    result3 = solution_optimal(strs3)
    print(f"Test 3: {result3} == {[['a']]} -> {'PASS' if result3 == [['a']] else 'FAIL'}")

    # 验证暴力解法
    print("\nBrute force verification:")
    sorted_brute1 = sorted([sorted(group) for group in solution_brute(strs1)])
    print(f"Brute Test 1: {sorted_brute1}")

    print("\nAll tests complete!")
