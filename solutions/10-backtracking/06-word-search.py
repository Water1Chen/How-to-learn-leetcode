"""
LC 79. Word Search (单词搜索)
Difficulty: Medium
Tags: Array, Backtracking, Matrix
Link: https://leetcode.cn/problems/word-search/
Category: backtracking
"""

from typing import List, Tuple


# ===== 暴力解法 =====
# 思路: DFS from each cell on the board, exploring all 4 directions recursively.
#       Use a visited set to avoid revisiting cells in the current path.
# 复杂度: O(m * n * 4^L) time where L=len(word), O(L) space for recursion + visited set
def solution_brute(board: List[List[str]], word: str) -> bool:
    """
    Search for word in board using DFS with a visited set.
    """
    if not board or not board[0]:
        # WHY: Empty board cannot contain any word
        return False

    rows, cols = len(board), len(board[0])

    # WHY: Track visited cells in the current path to prevent re-use of same cell
    visited: set = set()

    # WHY: Helper performs DFS from position (r, c) looking for word starting at index idx
    def dfs(r: int, c: int, idx: int) -> bool:
        # WHY: All characters matched successfully
        if idx == len(word):
            return True

        # WHY: Check bounds and whether cell is already visited in this path
        if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited:
            return False

        # WHY: Current cell must match the current character of the word
        if board[r][c] != word[idx]:
            return False

        # WHY: Mark current cell as visited before exploring neighbors
        visited.add((r, c))

        # WHY: Explore all 4 directions: down, up, right, left
        directions: List[Tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dr, dc in directions:
            # WHY: Recurse into neighbor with next character index
            if dfs(r + dr, c + dc, idx + 1):
                return True

        # WHY: Backtrack - unmark this cell so other paths can use it
        visited.discard((r, c))
        return False

    # WHY: Try starting DFS from every cell on the board
    for r in range(rows):
        for c in range(cols):
            # WHY: If first character matches, attempt DFS from this cell
            if board[r][c] == word[0] and dfs(r, c, 0):
                return True

    # WHY: Word not found starting from any cell
    return False


# ===== 最优解法 =====
# 思路: DFS + backtracking with in-place marking. Instead of using a visited set,
#       temporarily modify the board cell to a placeholder character ('#'), then
#       restore it after exploring. This avoids O(L) hash set operations per call.
# 复杂度: O(m * n * 4^L) time, O(L) space for recursion stack (no extra visited set)
def solution_optimal(board: List[List[str]], word: str) -> bool:
    """
    Search for word in board using DFS with in-place board marking for O(1) visited check.
    """
    if not board or not board[0]:
        # WHY: Empty board cannot contain any word
        return False

    rows, cols = len(board), len(board[0])

    # WHY: Helper performs DFS from position (r, c) looking for word from index idx
    def dfs(r: int, c: int, idx: int) -> bool:
        # WHY: All characters matched successfully
        if idx == len(word):
            return True

        # WHY: Check bounds — current position must be within the board
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False

        # WHY: Current cell must match the expected character
        if board[r][c] != word[idx]:
            return False

        # WHY: Save original character and mark cell as visited in-place (using '#')
        original_char: str = board[r][c]
        board[r][c] = '#'

        # WHY: Explore all 4 directions: down, up, right, left
        found: bool = (
            dfs(r + 1, c, idx + 1) or
            dfs(r - 1, c, idx + 1) or
            dfs(r, c + 1, idx + 1) or
            dfs(r, c - 1, idx + 1)
        )

        # WHY: Restore original character (backtrack) so other paths see the correct value
        board[r][c] = original_char

        return found

    # WHY: Try starting DFS from every cell on the board
    for r in range(rows):
        for c in range(cols):
            # WHY: Start search if first character matches
            if board[r][c] == word[0] and dfs(r, c, 0):
                return True

    # WHY: Word not found starting from any cell
    return False


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Word Search...")

    # Test case 1: Standard case
    board1 = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]
    assert solution_optimal(board1, "ABCCED") == True, "Test 1 failed"
    # WHY: Reset board for brute force test since optimal modifies in-place
    board1b = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]
    assert solution_brute(board1b, "ABCCED") == True, "Test 1 brute failed"
    print("Test 1 passed: ABCCED found")

    # Test case 2: Word not present
    board2 = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]
    assert solution_optimal(board2, "ABCB") == False, "Test 2 failed"
    board2b = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]
    assert solution_brute(board2b, "ABCB") == False, "Test 2 brute failed"
    print("Test 2 passed: ABCB not found")

    # Test case 3: Single character board and word
    board3 = [["A"]]
    assert solution_optimal(board3, "A") == True, "Test 3 failed"
    board3b = [["A"]]
    assert solution_brute(board3b, "A") == True, "Test 3 brute failed"
    print("Test 3 passed: single char")

    # Test case 4: Word longer than board cells
    board4 = [["A", "B"], ["C", "D"]]
    assert solution_optimal(board4, "ABCDE") == False, "Test 4 failed"
    board4b = [["A", "B"], ["C", "D"]]
    assert solution_brute(board4b, "ABCDE") == False, "Test 4 brute failed"
    print("Test 4 passed: word too long")

    print(f"Brute force verification (board1): {solution_brute([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], 'SEE')}")
    print("All tests passed!")
