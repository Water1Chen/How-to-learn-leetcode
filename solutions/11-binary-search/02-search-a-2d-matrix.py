"""
LC 74. Search a 2D Matrix (搜索二维矩阵)
Difficulty: Medium
Tags: Array, Binary Search, Matrix
Link: https://leetcode.cn/problems/search-a-2d-matrix/
Category: binary-search
"""

from typing import List


# ===== 暴力解法 =====
# 思路: Iterate through all rows and columns, checking each element. Since the matrix
#       has sorted rows and the first element of each row > last element of previous row,
#       we could optimize slightly by skipping rows, but brute checks everything.
# 复杂度: O(m * n) time, O(1) space
def solution_brute(matrix: List[List[int]], target: int) -> bool:
    """
    Search for target in matrix by scanning every element.
    """
    if not matrix or not matrix[0]:
        # WHY: Empty matrix cannot contain target
        return False

    rows: int = len(matrix)
    cols: int = len(matrix[0])

    # WHY: Iterate through every cell in the matrix
    for r in range(rows):
        for c in range(cols):
            # WHY: Check if current cell matches target
            if matrix[r][c] == target:
                return True

    # WHY: Target not found after scanning entire matrix
    return False


# ===== 最优解法 =====
# 思路: Treat the sorted 2D matrix as a flattened 1D sorted array of length m*n.
#       Map 1D index to 2D coordinates: row = idx // cols, col = idx % cols.
#       Perform standard binary search on the virtual 1D array.
# 复杂度: O(log(m*n)) time, O(1) space
def solution_optimal(matrix: List[List[int]], target: int) -> bool:
    """
    Search for target in sorted matrix using binary search on virtual 1D array.
    """
    if not matrix or not matrix[0]:
        # WHY: Empty matrix cannot contain target
        return False

    rows: int = len(matrix)
    cols: int = len(matrix[0])

    # WHY: Define binary search bounds on the virtual 1D array [0, m*n)
    left: int = 0
    right: int = rows * cols

    # WHY: Narrow search until range is exhausted
    while left < right:
        # WHY: Calculate mid point in the virtual 1D array
        mid: int = left + (right - left) // 2

        # WHY: Map 1D index to 2D coordinates
        r: int = mid // cols
        c: int = mid % cols

        # WHY: Access the actual matrix value at the mapped position
        mid_val: int = matrix[r][c]

        # WHY: If target is less than mid, search left half
        if target < mid_val:
            right = mid
        # WHY: If target is greater than mid, search right half
        elif target > mid_val:
            left = mid + 1
        else:
            # WHY: Target found at this position
            return True

    # WHY: Target not found in the matrix
    return False


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Search a 2D Matrix...")

    # Test case 1: Target present in the matrix
    matrix1 = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    assert solution_optimal(matrix1, 3) == True, "Test 1 optimal failed"
    assert solution_brute(matrix1, 3) == True, "Test 1 brute failed"
    print("Test 1 (3 found) passed!")

    # Test case 2: Target not present
    assert solution_optimal(matrix1, 13) == False, "Test 2 optimal failed"
    assert solution_brute(matrix1, 13) == False, "Test 2 brute failed"
    print("Test 2 (13 not found) passed!")

    # Test case 3: Single element matrix, target matches
    assert solution_optimal([[1]], 1) == True, "Test 3 optimal failed"
    assert solution_brute([[1]], 1) == True, "Test 3 brute failed"
    print("Test 3 (single element match) passed!")

    # Test case 4: Single element matrix, no match
    assert solution_optimal([[1]], 0) == False, "Test 4 optimal failed"
    assert solution_brute([[1]], 0) == False, "Test 4 brute failed"
    print("Test 4 (single element no match) passed!")

    # Test case 5: Empty matrix
    assert solution_optimal([], 1) == False, "Test 5 optimal failed"
    assert solution_brute([], 1) == False, "Test 5 brute failed"
    print("Test 5 (empty matrix) passed!")

    print(f"Brute force verification: {solution_brute(matrix1, 10)}")
    print("All tests passed!")
