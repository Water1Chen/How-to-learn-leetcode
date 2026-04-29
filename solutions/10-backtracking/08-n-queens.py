"""
LC 51. N-Queens (N 皇后)
Difficulty: Hard
Tags: Array, Backtracking
Link: https://leetcode.cn/problems/n-queens/
Category: backtracking
"""

from typing import List


# ===== 暴力解法 =====
# 思路: Place queens column by column. For each new queen, check all previously placed
#       queens for conflicts (same row, same diagonal). This is O(n!) since we place
#       one queen per column and try all rows, but each conflict check takes O(n).
# 复杂度: O(n! * n) time, O(n) space for board representation
def solution_brute(n: int) -> List[List[str]]:
    """
    Solve N-Queens by placing queens column by column with O(n) conflict checks.
    """
    results: List[List[str]] = []

    # WHY: queens[r] = c means a queen is placed at row r, column c
    # WHY: -1 indicates no queen placed in that row yet
    queens: List[int] = [-1] * n

    # WHY: Helper to check if a queen at (row, col) conflicts with already placed queens
    def is_safe(row: int, col: int) -> bool:
        # WHY: Check conflicts with all previously placed queens (rows 0 to row-1)
        for prev_row in range(row):
            prev_col: int = queens[prev_row]
            # WHY: Same column conflict
            if prev_col == col:
                return False
            # WHY: Diagonal conflict: |row_diff| == |col_diff| means same diagonal
            if abs(prev_row - row) == abs(prev_col - col):
                return False
        return True

    # WHY: Helper to convert queen positions to the required string board format
    def build_board() -> List[str]:
        board: List[str] = []
        # WHY: Construct each row as a string with 'Q' at the queen column and '.' elsewhere
        for r in range(n):
            row_str: List[str] = ['.'] * n
            row_str[queens[r]] = 'Q'
            board.append(''.join(row_str))
        return board

    # WHY: Backtrack by placing queen in each row sequentially
    def backtrack(row: int) -> None:
        # WHY: All n queens placed successfully — build and save the board
        if row == n:
            results.append(build_board())
            return

        # WHY: Try placing queen in every column of the current row
        for col in range(n):
            # WHY: Check if position (row, col) is safe from attack
            if is_safe(row, col):
                # WHY: Place queen at this position
                queens[row] = col
                # WHY: Recurse to place next queen in the next row
                backtrack(row + 1)
                # WHY: Backtrack — remove queen (set back to -1, though not strictly needed)
                queens[row] = -1

    backtrack(0)
    return results


# ===== 最优解法 =====
# 思路: Backtracking with O(1) conflict check using sets for columns and diagonals.
#       Main diagonal index = r - c (constant along NW-SE diagonal), anti-diagonal
#       index = r + c (constant along NE-SW diagonal). This avoids O(n) scan per placement.
# 复杂度: O(n!) time, O(n) space for sets
def solution_optimal(n: int) -> List[List[str]]:
    """
    Solve N-Queens using backtracking with O(1) conflict detection via sets.
    """
    results: List[List[str]] = []

    # WHY: Sets for O(1) conflict checking
    cols: set = set()       # WHY: Track which columns are occupied
    diag1: set = set()      # WHY: Track main diagonals (r - c) — NW-SE direction
    diag2: set = set()      # WHY: Track anti-diagonals (r + c) — NE-SW direction

    # WHY: Store queen column position per row for board construction
    queens: List[int] = [-1] * n

    # WHY: Helper to construct the board string representation from queen positions
    def build_board() -> List[str]:
        board: List[str] = []
        # WHY: Each row has exactly one 'Q' at the stored column index
        for r in range(n):
            row_str: List[str] = ['.'] * n
            row_str[queens[r]] = 'Q'
            board.append(''.join(row_str))
        return board

    # WHY: Backtrack by placing queens row by row
    def backtrack(row: int) -> None:
        # WHY: Base case — all rows have a queen placed
        if row == n:
            results.append(build_board())
            return

        # WHY: Try placing queen in every column of the current row
        for col in range(n):
            # WHY: O(1) conflict check using sets
            d1: int = row - col   # WHY: Main diagonal index (unique per NW-SE diagonal)
            d2: int = row + col   # WHY: Anti-diagonal index (unique per NE-SW diagonal)

            # WHY: Skip if column or either diagonal is already occupied
            if col in cols or d1 in diag1 or d2 in diag2:
                continue

            # WHY: Place queen — mark column and diagonals as occupied
            queens[row] = col
            cols.add(col)
            diag1.add(d1)
            diag2.add(d2)

            # WHY: Recurse to the next row
            backtrack(row + 1)

            # WHY: Backtrack — remove queen and unmark column/diagonals
            queens[row] = -1
            cols.discard(col)
            diag1.discard(d1)
            diag2.discard(d2)

    backtrack(0)
    return results


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing N-Queens...")

    # Test case 1: n=1 (single queen)
    result_1_opt = solution_optimal(1)
    result_1_brute = solution_brute(1)
    assert len(result_1_opt) == 1, f"Optimal n=1 should have 1 solution, got {len(result_1_opt)}"
    assert len(result_1_brute) == 1, f"Brute n=1 should have 1 solution, got {len(result_1_brute)}"
    assert result_1_opt[0] == ["Q"], f"n=1 solution wrong: {result_1_opt}"
    print("Test 1 (n=1) passed!")

    # Test case 2: n=4 (2 solutions)
    result_2_opt = solution_optimal(4)
    result_2_brute = solution_brute(4)
    assert len(result_2_opt) == 2, f"Optimal n=4 should have 2 solutions, got {len(result_2_opt)}"
    assert len(result_2_brute) == 2, f"Brute n=4 should have 2 solutions, got {len(result_2_brute)}"
    # WHY: Verify the solutions are valid boards with correct format
    for board in result_2_opt:
        assert len(board) == 4, "Board should have 4 rows"
        assert all(len(row) == 4 for row in board), "Each row should have 4 chars"
        assert all(c in '.Q' for row in board for c in row), "Only '.' and 'Q' allowed"
        # WHY: Each row must have exactly one queen
        assert all(row.count('Q') == 1 for row in board)
    print("Test 2 (n=4) passed!")

    # Test case 3: n=2 (no solution)
    result_3_opt = solution_optimal(2)
    result_3_brute = solution_brute(2)
    assert len(result_3_opt) == 0, f"Optimal n=2 should have 0 solutions, got {len(result_3_opt)}"
    assert len(result_3_brute) == 0, f"Brute n=2 should have 0 solutions, got {len(result_3_brute)}"
    print("Test 3 (n=2) passed!")

    print(f"Brute force verification (n=4): {len(solution_brute(4))} solutions found")
    print("All tests passed!")
