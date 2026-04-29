"""
LC 70. Climbing Stairs (爬楼梯)
Difficulty: Easy
Tags: Math, Dynamic Programming, Memoization
Link: https://leetcode.cn/problems/climbing-stairs/
Category: dp
"""


# ===== 暴力解法 =====
# 思路: Pure recursion: f(n) = f(n-1) + f(n-2). This is the Fibonacci sequence.
#       To reach step n, you either come from step n-1 (1 step) or step n-2 (2 steps).
#       Base cases: f(1) = 1, f(2) = 2.
# 复杂度: O(2^n) time (exponential — each call branches into 2), O(n) space for recursion stack
def solution_brute(n: int) -> int:
    """
    Count distinct ways to climb n stairs using brute force recursion.
    """
    # WHY: Base case: 1 way to climb 1 step (just one 1-step)
    if n == 1:
        return 1
    # WHY: Base case: 2 ways to climb 2 steps (1+1 or 2)
    if n == 2:
        return 2

    # WHY: Recurrence: ways to reach step n = ways to step n-1 + ways to step n-2
    return solution_brute(n - 1) + solution_brute(n - 2)


# ===== 最优解法 =====
# 思路: DP with rolling variables (space optimization). Instead of an array, maintain
#       only the last two computed values. dp[i] = dp[i-1] + dp[i-2], iterating
#       from 1 to n. This is essentially computing the Fibonacci number.
# 复杂度: O(n) time, O(1) space
def solution_optimal(n: int) -> int:
    """
    Count distinct ways to climb n stairs using DP with rolling variables.
    """
    # WHY: Base case: 1 way to climb 1 step
    if n == 1:
        return 1
    # WHY: Base case: 2 ways to climb 2 steps
    if n == 2:
        return 2

    # WHY: Initialize rolling variables for the first two steps
    prev2: int = 1  # WHY: f(1) — ways to reach step 1
    prev1: int = 2  # WHY: f(2) — ways to reach step 2

    # WHY: Iterate from step 3 up to n, computing each value from previous two
    for _ in range(3, n + 1):
        # WHY: Current step's ways = sum of ways for previous two steps
        current: int = prev1 + prev2
        # WHY: Shift rolling window: move prev1 to prev2, current to prev1
        prev2 = prev1
        prev1 = current

    # WHY: prev1 now holds f(n) after the loop
    return prev1


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Climbing Stairs...")

    # Test case 1: n=1
    assert solution_optimal(1) == 1, f"Test 1 optimal failed"
    assert solution_brute(1) == 1, f"Test 1 brute failed"
    print("Test 1 (n=1 -> 1) passed!")

    # Test case 2: n=2
    assert solution_optimal(2) == 2, f"Test 2 optimal failed"
    assert solution_brute(2) == 2, f"Test 2 brute failed"
    print("Test 2 (n=2 -> 2) passed!")

    # Test case 3: n=3
    assert solution_optimal(3) == 3, f"Test 3 optimal failed: {solution_optimal(3)}"
    assert solution_brute(3) == 3, f"Test 3 brute failed"
    print("Test 3 (n=3 -> 3) passed!")

    # Test case 4: n=5 (Fibonacci: 1,2,3,5,8)
    assert solution_optimal(5) == 8, f"Test 4 optimal failed: {solution_optimal(5)}"
    assert solution_brute(5) == 8, f"Test 4 brute failed"
    print("Test 4 (n=5 -> 8) passed!")

    # Test case 5: n=10
    assert solution_optimal(10) == 89, f"Test 5 optimal failed: {solution_optimal(10)}"
    assert solution_brute(10) == 89, f"Test 5 brute failed"
    print("Test 5 (n=10 -> 89) passed!")

    print(f"Brute force verification (n=10): {solution_brute(10)}")
    print("All tests passed!")
