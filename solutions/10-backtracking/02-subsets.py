"""
LC 78. Subsets
Difficulty: Medium
Tags: Backtracking, Array, Bit Manipulation
Link: https://leetcode.cn/problems/subsets/
Category: 10-backtracking
"""


# ===== 暴力解法 =====
# 思路: 使用位掩码枚举所有子集，每个元素可选（1）或不选（0）
# 复杂度: O(n * 2^n) time, O(n * 2^n) space
def solution_brute(nums):
    # WHY: result存储所有子集
    result = []
    # WHY: n为数组长度，共有2^n个子集
    n = len(nums)

    # WHY: 遍历所有位掩码 0 到 2^n - 1
    for mask in range(1 << n):
        # WHY: subset存储当前掩码对应的子集
        subset = []
        # WHY: 检查每个二进制位
        for i in range(n):
            # WHY: 如果第i位为1，表示选择nums[i]
            if mask & (1 << i):
                subset.append(nums[i])
        # WHY: 将当前子集加入结果集
        result.append(subset)

    # WHY: 返回所有子集
    return result


# ===== 最优解法 =====
# 思路: 回溯法，每个元素有选与不选两种选择，递归构建所有子集
# 复杂度: O(n * 2^n) time, O(n) space（不包含输出空间）
def solution_optimal(nums):
    # WHY: result存储所有子集
    result = []
    # WHY: path存储当前正在构建的子集
    path = []

    # WHY: 定义回溯递归函数，start_index控制可选择元素的起始位置
    def backtrack(start_index):
        # WHY: 将当前路径的副本加入结果集（每个节点都是一个有效子集）
        result.append(path[:])

        # WHY: 从start_index开始遍历剩余元素
        # WHY: 使用start_index避免重复生成相同子集（如[2,1]和[1,2]）
        for i in range(start_index, len(nums)):
            # WHY: 做选择：将当前元素加入子集
            path.append(nums[i])
            # WHY: 递归处理下一个元素，start_index为i+1（每个元素只能用一次）
            backtrack(i + 1)
            # WHY: 撤销选择：移除当前元素（回溯核心）
            path.pop()

    # WHY: 从索引0开始回溯
    backtrack(0)
    # WHY: 返回所有子集
    return result


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Subsets...")

    # 测试用例1: [1,2,3] -> 8个子集
    result1 = solution_optimal([1, 2, 3])
    expected1 = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    # WHY: 先对每个子集排序，再对所有子集排序，避免顺序差异导致断言失败
    assert sorted([sorted(s) for s in result1]) == sorted([sorted(s) for s in expected1]), \
        "测试用例1最优解法失败"
    print("测试用例1通过: [1,2,3] -> 8个子集")

    # 测试用例2: [0] -> 2个子集
    result2 = solution_brute([0])
    expected2 = [[], [0]]
    assert sorted(result2) == sorted(expected2), "测试用例2暴力解法失败"
    print("测试用例2通过: [0] -> 2个子集")

    print("All tests passed!")
