"""
LC 240. Search a 2D Matrix II (搜索二维矩阵 II)
Difficulty: Medium
Tags: Array, Binary Search, Divide and Conquer, Matrix
Link: https://leetcode.cn/problems/search-a-2d-matrix-ii/
Category: 06-matrix
"""

from typing import List


# ===== 暴力解法 =====
# 思路: 扫描整个矩阵，逐一比较每个元素
# 复杂度: O(m * n) time, O(1) space
def solution_brute(matrix: List[List[int]], target: int) -> bool:
    # WHY: 最简单的思路：遍历所有元素寻找目标值
    if not matrix or not matrix[0]:
        return False
    rows, cols = len(matrix), len(matrix[0])
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == target:
                return True
    return False


# ===== 最优解法 =====
# 思路: 从右上角开始搜索，利用矩阵的行列有序性质缩小搜索范围
#       如果当前值 > target，向左移动（列减1）；如果当前值 < target，向下移动（行加1）
#       关键洞察: 右上角元素是所在行的最大值、所在列的最小值，是完美的"分水岭"
# 复杂度: O(m + n) time, O(1) space
def solution_optimal(matrix: List[List[int]], target: int) -> bool:
    # WHY: 从右上角开始搜索，每次排除一行或一列，达到O(m+n)线性时间
    # WHY: 相比暴力法O(mn)，利用行列有序性质大幅剪枝
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    # WHY: 从右上角开始搜索，该位置同时具有"行最大、列最小"的特性
    row, col = 0, cols - 1

    while row < rows and col >= 0:
        current = matrix[row][col]
        if current == target:
            return True  # WHY: 找到目标值
        elif current > target:
            # WHY: 当前值大于目标，说明该列下方所有值都更大（列递增），排除整列
            col -= 1
        else:
            # WHY: 当前值小于目标，说明该行左侧所有值都更小（行递增），排除整行
            row += 1

    return False  # WHY: 越过边界仍未找到


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Search a 2D Matrix II...")

    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]

    # 测试用例1: 目标存在（中间值）
    target1 = 5
    expected1 = True
    result1 = solution_optimal(matrix, target1)
    print(f"Test 1: {result1} == {expected1} -> {'PASS' if result1 == expected1 else 'FAIL'}")

    # 测试用例2: 目标不存在
    target2 = 20
    expected2 = False
    result2 = solution_optimal(matrix, target2)
    print(f"Test 2: {result2} == {expected2} -> {'PASS' if result2 == expected2 else 'FAIL'}")

    # 测试用例3: 最小值
    target3 = 1
    expected3 = True
    result3 = solution_optimal(matrix, target3)
    print(f"Test 3: {result3} == {expected3} -> {'PASS' if result3 == expected3 else 'FAIL'}")

    # 测试用例4: 最大值
    target4 = 30
    expected4 = True
    result4 = solution_optimal(matrix, target4)
    print(f"Test 4: {result4} == {expected4} -> {'PASS' if result4 == expected4 else 'FAIL'}")

    print("\nAll tests complete!")
