"""
LC 118. Pascal's Triangle (杨辉三角)
Difficulty: Easy
Tags: Array, Dynamic Programming
Link: https://leetcode.cn/problems/pascals-triangle/
Category: dp
"""

from typing import List


# ===== 暴力解法 =====
# 思路: Compute each element using the combination formula C(row, col) = row! / (col! * (row-col)!).
#       This uses factorial calculations for every element, which is computationally expensive.
# 复杂度: O(n^3) time (n rows, each element computed with O(n) factorial),
#         O(1) extra space (excluding output)
def solution_brute(numRows: int) -> List[List[int]]:
    """
    Generate Pascal's triangle using factorial combination formula.
    """
    # WHY: Helper to compute factorial of a number
    def factorial(k: int) -> int:
        result: int = 1
        # WHY: Multiply from 2 to k to compute k!
        for i in range(2, k + 1):
            result *= i
        return result

    # WHY: Helper to compute binomial coefficient C(row, col)
    def combination(row: int, col: int) -> int:
        # WHY: C(row, col) = row! / (col! * (row-col)!)
        return factorial(row) // (factorial(col) * factorial(row - col))

    triangle: List[List[int]] = []
    # WHY: Build each row of Pascal's triangle
    for row in range(numRows):
        current_row: List[int] = []
        # WHY: Each row has (row+1) elements, indexed 0 to row
        for col in range(row + 1):
            # WHY: Compute value using combination formula
            current_row.append(combination(row, col))
        triangle.append(current_row)

    return triangle


# ===== 最优解法 =====
# 思路: DP iterative row by row. Start with the first row [1]. For each subsequent row,
#       create an array of length row+1, fill first and last with 1, and for each
#       middle element j, set row[j] = prev_row[j-1] + prev_row[j].
# 复杂度: O(n^2) time (sum of 1 to n elements), O(1) extra space (excluding output)
def solution_optimal(numRows: int) -> List[List[int]]:
    """
    Generate Pascal's triangle using DP iterative construction.
    """
    triangle: List[List[int]] = []

    # WHY: Build each row from row 0 to row numRows-1
    for row in range(numRows):
        # WHY: Create a new row with (row+1) elements, all initialized to 1
        current_row: List[int] = [1] * (row + 1)

        # WHY: Middle elements are computed from the previous row
        for j in range(1, row):
            # WHY: Each interior element = sum of two elements above it
            # WHY: Row above is triangle[row-1], at indices j-1 and j
            current_row[j] = triangle[row - 1][j - 1] + triangle[row - 1][j]

        # WHY: Append the fully constructed row to the triangle
        triangle.append(current_row)

    return triangle


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Pascal's Triangle...")

    # Test case 1: numRows=5
    expected_1: List[List[int]] = [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1]
    ]
    assert solution_optimal(5) == expected_1, f"Test 1 optimal failed: {solution_optimal(5)}"
    assert solution_brute(5) == expected_1, f"Test 1 brute failed"
    print("Test 1 (numRows=5) passed!")

    # Test case 2: numRows=1
    assert solution_optimal(1) == [[1]], "Test 2 optimal failed"
    assert solution_brute(1) == [[1]], "Test 2 brute failed"
    print("Test 2 (numRows=1) passed!")

    # Test case 3: numRows=2
    expected_3 = [[1], [1, 1]]
    assert solution_optimal(2) == expected_3, "Test 3 optimal failed"
    assert solution_brute(2) == expected_3, "Test 3 brute failed"
    print("Test 3 (numRows=2) passed!")

    # Test case 4: numRows=0 (empty triangle)
    assert solution_optimal(0) == [], "Test 4 optimal failed"
    assert solution_brute(0) == [], "Test 4 brute failed"
    print("Test 4 (numRows=0) passed!")

    # Test case 5: Verify numRows=6
    result_5_opt = solution_optimal(6)
    result_5_brute = solution_brute(6)
    assert len(result_5_opt) == 6, "Test 5 should have 6 rows"
    assert result_5_opt == result_5_brute, "Test 5 mismatch between optimal and brute"
    # WHY: Row 5 should be [1, 5, 10, 10, 5, 1]
    assert result_5_opt[5] == [1, 5, 10, 10, 5, 1], f"Test 5 row 5 wrong: {result_5_opt[5]}"
    print("Test 5 (numRows=6) passed!")

    print(f"Brute force verification (numRows=5): {solution_brute(5)}")
    print("All tests passed!")
