"""
LC 17. Letter Combinations of a Phone Number
Difficulty: Medium
Tags: Backtracking, Hash Table, String
Link: https://leetcode.cn/problems/letter-combinations-of-a-phone-number/
Category: 10-backtracking
"""


# ===== 暴力解法 =====
# 思路: 迭代法，逐位构建组合，每次将当前结果与下一组字母做笛卡尔积
# 复杂度: O(4^n) time, O(4^n) space (n为数字长度)
def solution_brute(digits):
    # WHY: 处理空字符串输入
    if not digits:
        return []

    # WHY: 数字到字母的映射表
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    # WHY: result初始化为包含空字符串的列表，用于迭代构建
    result = ['']

    # WHY: 遍历输入字符串的每个数字
    for digit in digits:
        # WHY: 获取当前数字对应的所有字母
        letters = phone_map[digit]
        # WHY: temp临时存储本轮构建的新组合
        temp = []
        # WHY: 将当前结果中的每个字符串与当前数字的每个字母组合
        for combo in result:
            for letter in letters:
                # WHY: 拼接形成新的组合字符串
                temp.append(combo + letter)
        # WHY: 更新结果为最新构建的组合列表
        result = temp

    # WHY: 返回所有字母组合
    return result


# ===== 最优解法 =====
# 思路: 回溯法，递归构建每种字母组合，使用索引追踪当前处理的数字位置
# 复杂度: O(4^n) time, O(n) space（递归栈深度）
def solution_optimal(digits):
    # WHY: 处理空字符串输入
    if not digits:
        return []

    # WHY: 数字到字母的映射表
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    # WHY: result存储所有字母组合
    result = []
    # WHY: path存储当前正在构建的组合字符串中的字符列表
    path = []

    # WHY: 定义回溯递归函数，index表示当前处理的数字位置
    def backtrack(index):
        # WHY: 如果已经处理完所有数字，将当前组合加入结果
        if index == len(digits):
            # WHY: 将路径中的字符列表拼接为字符串
            result.append(''.join(path))
            return

        # WHY: 获取当前数字对应的所有候选字母
        letters = phone_map[digits[index]]
        # WHY: 遍历每个候选字母
        for letter in letters:
            # WHY: 做选择：将当前字母加入路径
            path.append(letter)
            # WHY: 递归处理下一个数字
            backtrack(index + 1)
            # WHY: 撤销选择：移除当前字母（回溯核心）
            path.pop()

    # WHY: 从索引0开始回溯
    backtrack(0)
    # WHY: 返回所有字母组合
    return result


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Letter Combinations of a Phone Number...")

    # 测试用例1: "23" -> 9个组合
    result1 = solution_optimal("23")
    expected1 = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert sorted(result1) == sorted(expected1), "测试用例1最优解法失败"
    print("测试用例1通过: \"23\" -> 9个组合")

    # 测试用例2: "" -> []（空输入）
    assert solution_brute("") == [], "测试用例2暴力解法失败"
    assert solution_optimal("") == [], "测试用例2最优解法失败"
    print("测试用例2通过: \"\" -> []")

    # 测试用例3: "2" -> ["a","b","c"]
    result3 = solution_brute("2")
    expected3 = ["a", "b", "c"]
    assert sorted(result3) == sorted(expected3), "测试用例3暴力解法失败"
    print("测试用例3通过: \"2\" -> [\"a\",\"b\",\"c\"]")

    print("All tests passed!")
