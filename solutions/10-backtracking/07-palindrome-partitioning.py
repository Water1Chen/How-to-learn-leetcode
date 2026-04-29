"""
LC 131. Palindrome Partitioning (分割回文串)
Difficulty: Medium
Tags: String, Dynamic Programming, Backtracking
Link: https://leetcode.cn/problems/palindrome-partitioning/
Category: backtracking
"""

from typing import List


# ===== 暴力解法 =====
# 思路: Generate all possible partitions of the string (O(2^n) possibilities by
#       cutting or not cutting at each position). Check each substring for palindrome
#       property, filtering out non-palindrome partitions.
# 复杂度: O(n * 2^n) time, O(n) space for recursion stack
def solution_brute(s: str) -> List[List[str]]:
    """
    Partition s into substrings such that every substring is a palindrome.
    Uses brute force generating all partitions.
    """
    results: List[List[str]] = []

    # WHY: Helper to check if substring s[l:r+1] is a palindrome by two-pointer scan
    def is_palindrome(s: str, l: int, r: int) -> bool:
        # WHY: Compare characters from both ends moving inward
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    # WHY: Backtracking to generate all partitions starting from index `start`
    def backtrack(start: int, current: List[str]) -> None:
        # WHY: Reached end of string — a complete partition is formed
        if start == len(s):
            # WHY: Add a copy of current partition to results
            results.append(current[:])
            return

        # WHY: Try all possible end positions for the substring starting at `start`
        for end in range(start, len(s)):
            # WHY: Extract substring from start to end (inclusive)
            substring: str = s[start:end + 1]
            # WHY: Only recurse if the current substring is a palindrome
            if is_palindrome(s, start, end):
                # WHY: Choose — add this palindrome substring to current path
                current.append(substring)
                # WHY: Explore — recurse with next starting position after the substring
                backtrack(end + 1, current)
                # WHY: Unchoose — remove the substring to try other partitions
                current.pop()

    backtrack(0, [])
    return results


# ===== 最优解法 =====
# 思路: Backtracking with DP precomputation of palindrome table. Precompute all
#       palindrome substrings using DP (is_pal[i][j] = (s[i]==s[j]) and is_pal[i+1][j-1])
#       for O(1) palindrome lookup, avoiding repeated O(n) checks.
# 复杂度: O(n^2 + n * 2^n) time, O(n^2) space for palindrome DP table
def solution_optimal(s: str) -> List[List[str]]:
    """
    Partition s into palindrome substrings using backtracking with DP precomputed table.
    """
    n: int = len(s)
    results: List[List[str]] = []

    # WHY: dp[i][j] indicates whether substring s[i:j+1] is a palindrome
    # WHY: Initialize n x n table with False for all entries
    dp: List[List[bool]] = [[False] * n for _ in range(n)]

    # WHY: Fill DP table for palindrome detection in O(1) later
    # WHY: Iterate end index (right pointer) from 0 to n-1
    for end in range(n):
        # WHY: Iterate start index (left pointer) from 0 to end
        for start in range(end + 1):
            # WHY: A substring is palindrome if chars match AND (length <= 2 or inner substring is palindrome)
            if s[start] == s[end] and (end - start <= 2 or dp[start + 1][end - 1]):
                dp[start][end] = True

    # WHY: Backtracking to build partitions using O(1) palindrome lookups
    def backtrack(start: int, current: List[str]) -> None:
        # WHY: Base case — reached end of string, partition is complete
        if start == n:
            results.append(current[:])
            return

        # WHY: Try all possible end positions for the substring starting at `start`
        for end in range(start, n):
            # WHY: O(1) check if substring s[start:end+1] is a palindrome using DP table
            if dp[start][end]:
                # WHY: Choose this palindrome substring
                current.append(s[start:end + 1])
                # WHY: Continue partitioning from next character
                backtrack(end + 1, current)
                # WHY: Backtrack — remove the substring to try alternative partitions
                current.pop()

    backtrack(0, [])
    return results


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Palindrome Partitioning...")

    # Test case 1: s = "aab"
    expected_1: List[List[str]] = [["a", "a", "b"], ["aa", "b"]]
    result_1_opt: List[List[str]] = solution_optimal("aab")
    result_1_brute: List[List[str]] = solution_brute("aab")
    # WHY: Sort results for deterministic comparison
    assert sorted([sorted(p) for p in result_1_opt]) == sorted([sorted(p) for p in expected_1]), \
        f"Optimal test 1 failed: {result_1_opt}"
    assert sorted([sorted(p) for p in result_1_brute]) == sorted([sorted(p) for p in expected_1]), \
        f"Brute test 1 failed: {result_1_brute}"
    print("Test 1 (aab) passed!")

    # Test case 2: s = "a" (single character)
    expected_2: List[List[str]] = [["a"]]
    assert solution_optimal("a") == expected_2, f"Optimal test 2 failed"
    assert solution_brute("a") == expected_2, f"Brute test 2 failed"
    print("Test 2 (a) passed!")

    # Test case 3: s = "" (empty string)
    assert solution_optimal("") == [[]], f"Optimal test 3 failed"
    assert solution_brute("") == [[]], f"Brute test 3 failed"
    print("Test 3 (empty) passed!")

    # Test case 4: s = "aa" (all same)
    expected_4: List[List[str]] = [["a", "a"], ["aa"]]
    result_4_opt = solution_optimal("aa")
    result_4_brute = solution_brute("aa")
    assert sorted([sorted(p) for p in result_4_opt]) == sorted([sorted(p) for p in expected_4])
    assert sorted([sorted(p) for p in result_4_brute]) == sorted([sorted(p) for p in expected_4])
    print("Test 4 (aa) passed!")

    print(f"Brute force verification (aab): {solution_brute('aab')}")
    print("All tests passed!")
