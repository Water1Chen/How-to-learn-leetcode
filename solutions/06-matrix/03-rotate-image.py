"""
LC 48. Rotate Image (旋转图像)
Difficulty: Medium
Tags: Array, Matrix
Link: https://leetcode.cn/problems/rotate-image/
Category: 06-matrix
"""

from typing import List


# ===== 暴力解法 =====
# 思路: 使用新矩阵，根据旋转公式 new[row][col] = old[n-1-col][row] 填充
# 复杂度: O(n^2) time, O(n^2) space
def solution_brute(matrix: List[List[int]]) -> None:
    # WHY: 创建一个新矩阵存储旋转结果，直观但空间效率低
    n = len(matrix)
    result = [[0] * n for _ in range(n)]  # WHY: 创建n×n的新矩阵

    for r in range(n):
        for c in range(n):
            # WHY: 顺时针旋转90°的坐标映射: (r, c) → (c, n-1-r)
            # WHY: 也可以表达为 new[r][c] = old[n-1-c][r]
            result[c][n - 1 - r] = matrix[r][c]

    # WHY: 将结果拷贝回原矩阵（题目要求原地修改）
    for r in range(n):
        for c in range(n):
            matrix[r][c] = result[r][c]


# ===== 最优解法 =====
# 思路: 先转置矩阵（行变列），再对每一行做水平翻转
#       分两步实现原地旋转，每个步骤都容易理解和实现
#       数学原理: 转置 + 水平翻转 = 顺时针旋转90°
# 复杂度: O(n^2) time, O(1) space
def solution_optimal(matrix: List[List[int]]) -> None:
    # WHY: 分两步实现原地旋转，O(1)额外空间
    # WHY: 相比暴力法，通过数学变换避免使用额外矩阵
    n = len(matrix)

    # WHY: 第一步：矩阵转置 — 将matrix[i][j]与matrix[j][i]交换
    # WHY: 转置使行变为列，为下一步翻转做准备
    for i in range(n):
        for j in range(i + 1, n):  # WHY: j从i+1开始，避免重复交换和对角线交换
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # WHY: 第二步：每一行水平翻转
    # WHY: 转置后水平翻转 = 顺时针旋转90°
    for i in range(n):
        # WHY: 双指针从两端向中间交换
        left, right = 0, n - 1
        while left < right:
            matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
            left += 1
            right -= 1


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Rotate Image...")

    # 测试用例1: 3x3矩阵
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected1 = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    solution_optimal(matrix1)
    print(f"Test 1: {matrix1} == {expected1} -> {'PASS' if matrix1 == expected1 else 'FAIL'}")

    # 测试用例2: 4x4矩阵
    matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    expected2 = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
    solution_optimal(matrix2)
    print(f"Test 2: {matrix2} == {expected2} -> {'PASS' if matrix2 == expected2 else 'FAIL'}")

    # 测试用例3: 2x2矩阵
    matrix3 = [[1, 2], [3, 4]]
    expected3 = [[3, 1], [4, 2]]
    solution_optimal(matrix3)
    print(f"Test 3: {matrix3} == {expected3} -> {'PASS' if matrix3 == expected3 else 'FAIL'}")

    # 测试用例4: 1x1矩阵
    matrix4 = [[1]]
    expected4 = [[1]]
    solution_optimal(matrix4)
    print(f"Test 4: {matrix4} == {expected4} -> {'PASS' if matrix4 == expected4 else 'FAIL'}")

    print("\nAll tests complete!")
