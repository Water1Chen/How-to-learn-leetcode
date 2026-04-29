"""
LC 39. Combination Sum
Difficulty: Medium
Tags: Backtracking, Array
Link: https://leetcode.cn/problems/combination-sum/
Category: 10-backtracking
"""


# ===== 暴力解法 =====
# 思路: 回溯法，枚举所有可能的组合（允许重复使用同一元素），检查组合和是否等于目标值
# 复杂度: O(n^(target/min)) time, O(target/min) space
def solution_brute(candidates, target):
    # WHY: result存储所有满足条件的组合
    result = []
    # WHY: n为候选数组长度
    n = len(candidates)
    # WHY: path存储当前正在构建的组合
    path = []

    # WHY: 定义递归枚举函数
    # WHY: start控制起始索引，避免重复组合（如[2,3]和[3,2]）
    def dfs(start, remaining):
        # WHY: 如果剩余值为0，说明当前组合的和正好等于目标值
        if remaining == 0:
            # WHY: 将当前路径的副本加入结果集
            result.append(path[:])
            return
        # WHY: 如果剩余值小于0，当前组合无效，剪枝返回
        if remaining < 0:
            return

        # WHY: 从start开始遍历，避免产生重复组合
        for i in range(start, n):
            # WHY: 做选择：将当前候选数加入组合
            path.append(candidates[i])
            # WHY: 递归调用，允许重复使用同一个数（所以start还是i）
            dfs(i, remaining - candidates[i])
            # WHY: 撤销选择：移除最后一个数（回溯核心）
            path.pop()

    # WHY: 从索引0、剩余值target开始搜索
    dfs(0, target)
    # WHY: 返回所有和为目标值的组合
    return result


# ===== 最优解法 =====
# 思路: 回溯法 + 剪枝优化，先排序以便提前终止，start索引避免重复组合
# 复杂度: O(n^(target/min)) time, O(target/min) space
def solution_optimal(candidates, target):
    # WHY: result存储所有满足条件的组合
    result = []
    # WHY: path存储当前正在构建的组合
    path = []

    # WHY: 先排序，方便后续剪枝（当前数字过大时后续更大数字都可以跳过）
    candidates.sort()

    # WHY: 定义回溯函数
    # WHY: start控制起始索引（避免重复组合，允许重复使用同一元素）
    # WHY: remaining表示距离目标值还差多少
    def backtrack(start, remaining):
        # WHY: 如果剩余值为0，说明当前组合的和正好等于目标值
        if remaining == 0:
            # WHY: 将当前路径的副本加入结果集
            result.append(path[:])
            return

        # WHY: 从start位置开始遍历候选数组
        for i in range(start, len(candidates)):
            # WHY: 剪枝优化：如果当前数字已经大于剩余值
            # WHY: 因为数组已排序，后续数字更大，全部不可能满足条件
            if candidates[i] > remaining:
                break

            # WHY: 做选择：将当前数字加入组合
            path.append(candidates[i])
            # WHY: 递归调用，传入i（而非i+1）允许重复使用同一数字
            backtrack(i, remaining - candidates[i])
            # WHY: 撤销选择：移除当前数字（回溯核心）
            path.pop()

    # WHY: 从索引0、剩余值target开始回溯
    backtrack(0, target)
    # WHY: 返回所有和为目标值的组合
    return result


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Combination Sum...")

    # 测试用例1: candidates=[2,3,6,7], target=7 -> [[2,2,3],[7]]
    result1 = solution_optimal([2, 3, 6, 7], 7)
    expected1 = [[2, 2, 3], [7]]
    assert sorted([sorted(c) for c in result1]) == sorted([sorted(c) for c in expected1]), \
        "测试用例1最优解法失败"
    print("测试用例1通过: [2,3,6,7], target=7 -> [[2,2,3],[7]]")

    # 测试用例2: candidates=[2,3,5], target=8
    result2 = solution_brute([2, 3, 5], 8)
    expected2 = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert sorted([sorted(c) for c in result2]) == sorted([sorted(c) for c in expected2]), \
        "测试用例2暴力解法失败"
    print("测试用例2通过: [2,3,5], target=8 -> [[2,2,2,2],[2,3,3],[3,5]]")

    print("All tests passed!")
