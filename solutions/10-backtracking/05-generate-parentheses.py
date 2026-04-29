"""
LC 22. Generate Parentheses (括号生成)
Difficulty: Medium
Tags: String, Backtracking
Link: https://leetcode.cn/problems/generate-parentheses/
Category: backtracking
"""

from typing import List


# ===== 暴力解法 =====
# 思路: Generate all possible 2^(2n) strings of '(' and ')', then filter valid ones.
#       A valid string must have equal number of '(' and ')', and at no prefix does
#       the count of ')' exceed '('.
# 复杂度: O(2^(2n) * n) time, O(n) space for recursion stack
def solution_brute(n: int) -> List[str]:
    """
    Generate all well-formed parentheses combinations using brute force.
    """
    results: List[str] = []

    # WHY: Helper to generate all 2^(2n) strings recursively
    def backtrack(current: str, pos: int, max_len: int) -> None:
        # WHY: Base case - when current string reaches full length 2n
        if pos == max_len:
            # WHY: Validate the generated string before adding to results
            if is_valid(current):
                results.append(current)
            return
        # WHY: Try adding '(' at current position, exploring this branch
        backtrack(current + '(', pos + 1, max_len)
        # WHY: Try adding ')' at current position, exploring alternative branch
        backtrack(current + ')', pos + 1, max_len)

    # WHY: Helper to check if a parentheses string is well-formed
    def is_valid(s: str) -> bool:
        balance = 0
        # WHY: Scan each character, tracking the net balance
        for ch in s:
            # WHY: '(' increases balance, ')' decreases it
            balance += 1 if ch == '(' else -1
            # WHY: If balance goes negative, ')' appeared without matching '('
            if balance < 0:
                return False
        # WHY: Valid only if balance returns to exactly zero at end
        return balance == 0

    backtrack('', 0, 2 * n)
    return results


# ===== 最优解法 =====
# 思路: Backtracking with pruning — only add '(' if used < n, only add ')' if
#       used_right < used_left. This ensures we never generate invalid strings,
#       reducing the search space from 2^(2n) to the Catalan number C_n.
# 复杂度: O(4^n / sqrt(n)) time (Catalan number), O(n) space for recursion stack
def solution_optimal(n: int) -> List[str]:
    """
    Generate all well-formed parentheses using backtracking with pruning.
    """
    results: List[str] = []

    # WHY: Backtrack with tracking of used left/right parentheses counts
    def backtrack(current: str, left_used: int, right_used: int) -> None:
        # WHY: Base case - when both types have been used n times each, string is complete
        if left_used == n and right_used == n:
            results.append(current)
            return

        # WHY: Pruning: we can add '(' as long as we haven't used all n left parentheses
        if left_used < n:
            # WHY: Adding '(' is always safe at this point
            backtrack(current + '(', left_used + 1, right_used)

        # WHY: Pruning: we can add ')' only if there are unmatched '(' left
        if right_used < left_used:
            # WHY: Adding ')' maintains validity because we have an open '(' to match
            backtrack(current + ')', left_used, right_used + 1)

    backtrack('', 0, 0)
    return results


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Generate Parentheses...")

    # Test case 1: n=3
    expected_3 = {"((()))", "(()())", "(())()", "()(())", "()()()"}
    result_3_opt = set(solution_optimal(3))
    result_3_brute = set(solution_brute(3))
    assert result_3_opt == expected_3, f"Optimal n=3 failed: {result_3_opt}"
    assert result_3_brute == expected_3, f"Brute n=3 failed: {result_3_brute}"
    print("Test n=3 passed!")

    # Test case 2: n=1
    expected_1 = {"()"}
    result_1_opt = set(solution_optimal(1))
    result_1_brute = set(solution_brute(1))
    assert result_1_opt == expected_1, f"Optimal n=1 failed: {result_1_opt}"
    assert result_1_brute == expected_1, f"Brute n=1 failed: {result_1_brute}"
    print("Test n=1 passed!")

    # Test case 3: n=0 (edge case)
    assert solution_optimal(0) == [''], f"Optimal n=0 failed"
    assert solution_brute(0) == [''], f"Brute n=0 failed"
    print("Test n=0 passed!")

    print(f"Brute force verification (n=3): {sorted(solution_brute(3))}")
    print("All tests passed!")
