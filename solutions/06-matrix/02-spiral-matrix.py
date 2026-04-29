"""
LC 54. Spiral Matrix (螺旋矩阵)
Difficulty: Medium
Tags: Array, Matrix, Simulation
Link: https://leetcode.cn/problems/spiral-matrix/
Category: 06-matrix
"""

from typing import List


# ===== 暴力解法 =====
# 思路: 使用visited集合记录已访问元素，按右下左上方向遍历
# 复杂度: O(m * n) time, O(m * n) space
def solution_brute(matrix: List[List[int]]) -> List[int]:
    # WHY: 使用visited集合避免重复访问，按螺旋顺序模拟行走
    if not matrix or not matrix[0]:
        return []

    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]  # WHY: 记录每个格子是否已访问
    result = []

    # WHY: 方向向量: 右、下、左、上（螺旋顺序）
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_idx = 0  # WHY: 当前方向索引
    r = c = 0  # WHY: 起始位置

    for _ in range(rows * cols):  # WHY: 遍历所有元素
        result.append(matrix[r][c])
        visited[r][c] = True

        # WHY: 计算下一步位置
        nr, nc = r + dirs[dir_idx][0], c + dirs[dir_idx][1]
        # WHY: 如果下一步越界或已访问，顺时针换方向
        if nr < 0 or nr >= rows or nc < 0 or nc >= cols or visited[nr][nc]:
            dir_idx = (dir_idx + 1) % 4  # WHY: 切换方向
            nr, nc = r + dirs[dir_idx][0], c + dirs[dir_idx][1]

        r, c = nr, nc  # WHY: 移动到下一个有效位置

    return result


# ===== 最优解法 =====
# 思路: 四边界收缩法 — 用top、bottom、left、right四个指针模拟螺旋边界
#       按右、下、左、上的顺序遍历，每遍历完一条边，对应边界向内收缩
# 复杂度: O(m * n) time, O(1) space (不含输出空间)
def solution_optimal(matrix: List[List[int]]) -> List[int]:
    # WHY: 边界收缩法直接利用坐标边界控制遍历，无需额外空间
    # WHY: 相比visited法，省去了O(m*n)的标记空间
    if not matrix or not matrix[0]:
        return []

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # WHY: 从左到右遍历上边界
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1  # WHY: 上边界收缩

        # WHY: 从上到下遍历右边界
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1  # WHY: 右边界收缩

        if top <= bottom:
            # WHY: 从右到左遍历下边界（如果还有行）
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1  # WHY: 下边界收缩

        if left <= right:
            # WHY: 从下到上遍历左边界（如果还有列）
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1  # WHY: 左边界收缩

    return result


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Spiral Matrix...")

    # 测试用例1: 3x3矩阵
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected1 = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    result1 = solution_optimal(matrix1)
    print(f"Test 1: {result1} == {expected1} -> {'PASS' if result1 == expected1 else 'FAIL'}")

    # 测试用例2: 3x4矩阵
    matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    expected2 = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    result2 = solution_optimal(matrix2)
    print(f"Test 2: {result2} == {expected2} -> {'PASS' if result2 == expected2 else 'FAIL'}")

    # 测试用例3: 单行
    matrix3 = [[1, 2, 3]]
    expected3 = [1, 2, 3]
    result3 = solution_optimal(matrix3)
    print(f"Test 3: {result3} == {expected3} -> {'PASS' if result3 == expected3 else 'FAIL'}")

    # 测试用例4: 单列
    matrix4 = [[1], [2], [3]]
    expected4 = [1, 2, 3]
    result4 = solution_optimal(matrix4)
    print(f"Test 4: {result4} == {expected4} -> {'PASS' if result4 == expected4 else 'FAIL'}")

    print("\nAll tests complete!")
