"""
LC 84. Largest Rectangle in Histogram (柱状图中最大的矩形)
Difficulty: Hard
Tags: Array, Stack, Monotonic Stack
Link: https://leetcode.cn/problems/largest-rectangle-in-histogram/
Category: stack
"""

from typing import List


# ===== 暴力解法 =====
# 思路: For each bar, expand left and right to find the maximum width where this bar's
#       height is the minimum. The area = height * (right - left + 1). Take the max
#       across all bars. This is O(n^2).
# 复杂度: O(n^2) time, O(1) space
def solution_brute(heights: List[int]) -> int:
    """
    Find the largest rectangle in histogram using brute force expansion.
    """
    n: int = len(heights)
    max_area: int = 0

    # WHY: Treat each bar as the shortest bar in a candidate rectangle
    for i in range(n):
        h: int = heights[i]

        # WHY: Expand to the left while bars are at least as tall as current
        left: int = i
        while left > 0 and heights[left - 1] >= h:
            left -= 1

        # WHY: Expand to the right while bars are at least as tall as current
        right: int = i
        while right < n - 1 and heights[right + 1] >= h:
            right += 1

        # WHY: Calculate area with current bar height as the minimum height
        area: int = h * (right - left + 1)
        # WHY: Update global maximum
        max_area = max(max_area, area)

    return max_area


# ===== 最优解法 =====
# 思路: Monotonic increasing stack. When we encounter a bar shorter than the top of stack,
#       we pop the taller bar and calculate the largest rectangle that uses it as the
#       limiting height. The stack always maintains indices with increasing heights.
#       Adding a sentinel 0 at the end ensures all bars are processed.
# 复杂度: O(n) time (each bar pushed/popped once), O(n) space for stack
def solution_optimal(heights: List[int]) -> int:
    """
    Find the largest rectangle in histogram using monotonic increasing stack.
    """
    # WHY: Sentinel: add a 0 at the end to force processing all remaining bars in stack
    bars: List[int] = heights + [0]
    n: int = len(bars)
    # WHY: Stack stores indices with increasing heights
    stack: List[int] = []
    max_area: int = 0

    # WHY: Iterate through all bars including the sentinel
    for i in range(n):
        # WHY: While current bar breaks the increasing height order (or sentinel triggers)
        while stack and bars[i] < bars[stack[-1]]:
            # WHY: Pop the taller bar's index — this bar's height limits the rectangle
            h: int = bars[stack.pop()]

            # WHY: If stack is empty, the rectangle extends from 0 to i
            # WHY: Otherwise, left bound is the new top of stack (last bar shorter than h)
            left: int = stack[-1] if stack else -1
            # WHY: Width = right_bound - left_bound - 1 = i - left - 1
            width: int = i - left - 1

            # WHY: Calculate area and update global maximum
            max_area = max(max_area, h * width)

        # WHY: Push current index onto stack (maintaining increasing height order)
        stack.append(i)

    return max_area


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Largest Rectangle in Histogram...")

    # Test case 1: Standard case
    heights1 = [2, 1, 5, 6, 2, 3]
    result_1_opt = solution_optimal(heights1)
    result_1_brute = solution_brute(heights1)
    assert result_1_opt == 10, f"Test 1 optimal failed: {result_1_opt}"
    assert result_1_brute == 10, f"Test 1 brute failed"
    print("Test 1 ([2,1,5,6,2,3] -> 10) passed!")

    # Test case 2: Single bar
    assert solution_optimal([5]) == 5, "Test 2 optimal failed"
    assert solution_brute([5]) == 5, "Test 2 brute failed"
    print("Test 2 ([5] -> 5) passed!")

    # Test case 3: Decreasing heights
    heights3 = [6, 5, 4, 3, 2, 1]
    result_3_opt = solution_optimal(heights3)
    result_3_brute = solution_brute(heights3)
    # WHY: The largest rectangle is the shortest bar spanning all bars: 1 * 6 = 6
    assert result_3_opt == 6, f"Test 3 optimal failed: {result_3_opt}"
    assert result_3_brute == 6, f"Test 3 brute failed"
    print("Test 3 (decreasing -> 6) passed!")

    # Test case 4: All same height
    heights4 = [2, 2, 2, 2]
    result_4_opt = solution_optimal(heights4)
    result_4_brute = solution_brute(heights4)
    assert result_4_opt == 8, f"Test 4 optimal failed: {result_4_opt}"
    assert result_4_brute == 8, f"Test 4 brute failed"
    print("Test 4 (all 2s -> 8) passed!")

    # Test case 5: Empty histogram
    assert solution_optimal([]) == 0, "Test 5 optimal failed"
    assert solution_brute([]) == 0, "Test 5 brute failed"
    print("Test 5 (empty) passed!")

    print(f"Brute force verification: {solution_brute([2,1,5,6,2,3])}")
    print("All tests passed!")
