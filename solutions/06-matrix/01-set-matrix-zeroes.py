"""
LC 73. Set Matrix Zeroes (矩阵置零)
Difficulty: Medium
Tags: Array, Hash Table, Matrix
Link: https://leetcode.cn/problems/set-matrix-zeroes/
Category: 06-matrix
"""

from typing import List


# ===== 暴力解法 =====
# 思路: 使用两个集合分别记录需要置零的行和列，然后遍历置零
# 复杂度: O(m * n) time, O(m + n) space
def solution_brute(matrix: List[List[int]]) -> None:
    # WHY: 用额外集合记录0的位置，空间换时间的简单思路
    if not matrix or not matrix[0]:
        return
    rows, cols = len(matrix), len(matrix[0])
    zero_rows = set()  # WHY: 记录需要置零的行
    zero_cols = set()  # WHY: 记录需要置零的列

    # WHY: 第一遍扫描：找出所有0所在的行和列
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                zero_rows.add(r)
                zero_cols.add(c)

    # WHY: 第二遍扫描：将标记的行和列置零
    for r in range(rows):
        for c in range(cols):
            if r in zero_rows or c in zero_cols:
                matrix[r][c] = 0


# ===== 最优解法 =====
# 思路: 使用矩阵的第一行和第一列作为标记位，代替额外的集合
#       需要额外两个标记变量记录第一行和第一列本身是否需要置零
# 复杂度: O(m * n) time, O(1) space
def solution_optimal(matrix: List[List[int]]) -> None:
    # WHY: 利用矩阵本身的行列作为标记，实现O(1)额外空间
    # WHY: 相比暴力法，省去了O(m+n)的额外集合空间
    if not matrix or not matrix[0]:
        return
    rows, cols = len(matrix), len(matrix[0])

    # WHY: 预先检查第一行和第一列是否包含0，因为后续会用它们做标记
    first_row_zero = any(matrix[0][c] == 0 for c in range(cols))
    first_col_zero = any(matrix[r][0] == 0 for r in range(rows))

    # WHY: 用第一行和第一列标记需要置零的行和列
    # WHY: 如果matrix[r][c]==0，则在第一行第c列和第一列第r行做标记
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][c] == 0:
                matrix[0][c] = 0  # WHY: 标记第c列需要置零
                matrix[r][0] = 0  # WHY: 标记第r行需要置零

    # WHY: 根据标记，将对应行置零（跳过第一行）
    for r in range(1, rows):
        if matrix[r][0] == 0:  # WHY: 该行被标记，需要全置零
            for c in range(1, cols):
                matrix[r][c] = 0

    # WHY: 根据标记，将对应列置零（跳过第一列）
    for c in range(1, cols):
        if matrix[0][c] == 0:  # WHY: 该列被标记，需要全置零
            for r in range(1, rows):
                matrix[r][c] = 0

    # WHY: 根据预先检查，处理第一行
    if first_row_zero:
        for c in range(cols):
            matrix[0][c] = 0

    # WHY: 根据预先检查，处理第一列
    if first_col_zero:
        for r in range(rows):
            matrix[r][0] = 0


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Set Matrix Zeroes...")

    # 测试用例1: 标准情况
    matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    expected1 = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    solution_optimal(matrix1)
    print(f"Test 1: {matrix1} == {expected1} -> {'PASS' if matrix1 == expected1 else 'FAIL'}")

    # 测试用例2: 多个0
    matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    expected2 = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
    solution_optimal(matrix2)
    print(f"Test 2: {matrix2} == {expected2} -> {'PASS' if matrix2 == expected2 else 'FAIL'}")

    # 测试用例3: 无0
    matrix3 = [[1, 2], [3, 4]]
    expected3 = [[1, 2], [3, 4]]
    solution_optimal(matrix3)
    print(f"Test 3: {matrix3} == {expected3} -> {'PASS' if matrix3 == expected3 else 'FAIL'}")

    # 测试用例4: 单行
    matrix4 = [[0, 1]]
    expected4 = [[0, 0]]
    solution_optimal(matrix4)
    print(f"Test 4: {matrix4} == {expected4} -> {'PASS' if matrix4 == expected4 else 'FAIL'}")

    print("\nAll tests complete!")
