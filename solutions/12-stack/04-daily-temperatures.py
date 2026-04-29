"""
LC 739. Daily Temperatures (每日温度)
Difficulty: Medium
Tags: Array, Stack, Monotonic Stack
Link: https://leetcode.cn/problems/daily-temperatures/
Category: stack
"""

from typing import List


# ===== 暴力解法 =====
# 思路: For each day, scan forward to find the next day with a higher temperature.
#       The answer[i] is the number of days to wait (j - i) or 0 if none.
# 复杂度: O(n^2) time, O(1) extra space (excluding output)
def solution_brute(temperatures: List[int]) -> List[int]:
    """
    Calculate days to wait for warmer temperature using brute force.
    """
    n: int = len(temperatures)
    # WHY: Initialize result array with zeros (0 means no warmer day ahead)
    result: List[int] = [0] * n

    # WHY: For each day, scan forward to find a warmer temperature
    for i in range(n):
        # WHY: Look ahead from i+1 to the end
        for j in range(i + 1, n):
            # WHY: Found the first warmer day
            if temperatures[j] > temperatures[i]:
                # WHY: Days to wait is the difference in indices
                result[i] = j - i
                # WHY: Stop scanning once we found the next warmer day
                break

    return result


# ===== 最优解法 =====
# 思路: Monotonic decreasing stack. Iterate through temperatures from left to right.
#       Maintain a stack of indices with decreasing temperatures. When we find a
#       temperature that breaks the decreasing order, it means this is the "next
#       warmer" day for all colder days on the stack.
# 复杂度: O(n) time (each element pushed/popped at most once), O(n) space for stack
def solution_optimal(temperatures: List[int]) -> List[int]:
    """
    Calculate days to wait for warmer temperature using monotonic decreasing stack.
    """
    n: int = len(temperatures)
    # WHY: Initialize result array with zeros
    result: List[int] = [0] * n
    # WHY: Stack stores indices of temperatures in decreasing order
    stack: List[int] = []

    # WHY: Iterate through each day's temperature
    for i in range(n):
        # WHY: While current temp > temp at top of stack (warmer than previous colder days)
        while stack and temperatures[i] > temperatures[stack[-1]]:
            # WHY: Pop the index of the colder day
            prev_idx: int = stack.pop()
            # WHY: The current day is the next warmer day for the popped day
            result[prev_idx] = i - prev_idx

        # WHY: Push current index onto stack (it will be colder than future temps)
        stack.append(i)

    # WHY: Remaining indices in stack never found a warmer day — result stays 0
    return result


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Daily Temperatures...")

    # Test case 1: Standard case
    temps1 = [73, 74, 75, 71, 69, 72, 76, 73]
    expected1 = [1, 1, 4, 2, 1, 1, 0, 0]
    assert solution_optimal(temps1) == expected1, \
        f"Test 1 optimal failed: {solution_optimal(temps1)}"
    assert solution_brute(temps1) == expected1, \
        f"Test 1 brute failed"
    print("Test 1 passed!")

    # Test case 2: Strictly decreasing (no warmer day for any)
    temps2 = [30, 29, 28, 27]
    expected2 = [0, 0, 0, 0]
    assert solution_optimal(temps2) == expected2, f"Test 2 optimal failed"
    assert solution_brute(temps2) == expected2, f"Test 2 brute failed"
    print("Test 2 (decreasing) passed!")

    # Test case 3: Strictly increasing (each day has warmer next day)
    temps3 = [30, 31, 32, 33]
    expected3 = [1, 1, 1, 0]
    assert solution_optimal(temps3) == expected3, f"Test 3 optimal failed"
    assert solution_brute(temps3) == expected3, f"Test 3 brute failed"
    print("Test 3 (increasing) passed!")

    # Test case 4: Single day
    assert solution_optimal([50]) == [0], "Test 4 optimal failed"
    assert solution_brute([50]) == [0], "Test 4 brute failed"
    print("Test 4 (single) passed!")

    # Test case 5: Same temperatures (no warmer day)
    temps5 = [70, 70, 70]
    expected5 = [0, 0, 0]
    assert solution_optimal(temps5) == expected5, f"Test 5 optimal failed"
    assert solution_brute(temps5) == expected5, f"Test 5 brute failed"
    print("Test 5 (same temps) passed!")

    print(f"Brute force verification: {solution_brute([73,74,75,71,69,72,76,73])}")
    print("All tests passed!")
