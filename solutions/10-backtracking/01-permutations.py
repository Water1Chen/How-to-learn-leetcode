"""
LC 46. Permutations
Difficulty: Medium
Tags: Backtracking, Array
Link: https://leetcode.cn/problems/permutations/
Category: 10-backtracking
"""


# ===== 暴力解法 =====
# 思路: 使用itertools.permutations生成所有排列
# 复杂度: O(n! * n) time, O(n! * n) space
def solution_brute(nums):
    # WHY: 导入itertools库的permutations函数
    from itertools import permutations
    # WHY: 生成所有排列并转换为列表形式返回
    return [list(p) for p in permutations(nums)]


# ===== 最优解法 =====
# 思路: 回溯法，使用used数组标记已使用的元素，逐步构建排列
# 复杂度: O(n! * n) time, O(n) space（不包含输出空间）
def solution_optimal(nums):
    # WHY: result存储所有生成的排列
    result = []
    # WHY: path存储当前正在构建的排列路径
    path = []
    # WHY: used数组标记每个元素是否已被使用（True表示已使用）
    used = [False] * len(nums)

    # WHY: 定义回溯递归函数
    def backtrack():
        # WHY: 如果当前路径长度等于数组长度，说明一个排列已构建完成
        if len(path) == len(nums):
            # WHY: 将当前路径的副本加入结果集（避免后续修改影响）
            result.append(path[:])
            return

        # WHY: 遍历所有元素，尝试将未使用的元素加入排列
        for i in range(len(nums)):
            # WHY: 如果当前元素已被使用，跳过
            if used[i]:
                continue

            # WHY: 做选择：标记当前元素为已使用
            used[i] = True
            # WHY: 将当前元素加入路径
            path.append(nums[i])

            # WHY: 递归处理下一个位置的选择
            backtrack()

            # WHY: 撤销选择：从路径中移除当前元素
            path.pop()
            # WHY: 恢复当前元素为未使用状态（回溯核心）
            used[i] = False

    # WHY: 从空路径开始回溯
    backtrack()
    # WHY: 返回所有排列
    return result


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Permutations...")

    # 测试用例1: [1,2,3] -> 6个排列
    result1 = solution_optimal([1, 2, 3])
    expected1 = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert sorted(result1) == sorted(expected1), "测试用例1最优解法失败"
    print("测试用例1通过: [1,2,3] -> 6个排列")

    # 测试用例2: [0,1] -> 2个排列
    result2 = solution_brute([0, 1])
    expected2 = [[0, 1], [1, 0]]
    assert sorted(result2) == sorted(expected2), "测试用例2暴力解法失败"
    print("测试用例2通过: [0,1] -> 2个排列")

    print("All tests passed!")
