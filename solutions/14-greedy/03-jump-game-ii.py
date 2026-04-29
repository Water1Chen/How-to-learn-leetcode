"""
LC 45. Jump Game II (跳跃游戏 II)
Difficulty: Medium
Tags: Array, Dynamic Programming, Greedy, BFS
Link: https://leetcode.cn/problems/jump-game-ii/
Category: greedy
"""

from typing import List


# ===== 暴力解法 =====
# 思路: DP: dp[i] = minimum jumps to reach position i from start.
#       Initialize dp[0] = 0, all others = infinity.
#       For each position i, for each reachable position j from i, update dp[j].
# 复杂度: O(n^2) time, O(n) space for DP array
def solution_brute(nums: List[int]) -> int:
    """
    Find minimum jumps to reach last index using DP.
    """
    n: int = len(nums)
    if n == 1:
        # WHY: Already at the last index, no jumps needed
        return 0

    # WHY: dp[i] = minimum jumps to reach position i
    dp: List[int] = [10**9] * n
    dp[0] = 0

    # WHY: Iterate through each position as a potential jump start
    for i in range(n):
        # WHY: Try all possible jump lengths from position i
        for j in range(1, nums[i] + 1):
            # WHY: Calculate the landing position
            next_pos: int = i + j
            # WHY: Stop if beyond array bounds
            if next_pos >= n:
                break
            # WHY: Update dp for the landing position (one more jump from i)
            dp[next_pos] = min(dp[next_pos], dp[i] + 1)

    # WHY: Return minimum jumps to reach the last index
    return dp[n - 1]


# ===== 最优解法 =====
# 思路: BFS/greedy with boundary marking. Use the concept of "levels" like BFS.
#       current_end marks the farthest index reachable with the current number of jumps.
#       farthest tracks the absolute farthest index reachable from the current level.
#       When we reach current_end, we increment jumps and set current_end = farthest.
# 复杂度: O(n) time, O(1) space
def solution_optimal(nums: List[int]) -> int:
    """
    Find minimum jumps to reach last index using greedy BFS approach.
    """
    n: int = len(nums)
    if n == 1:
        # WHY: Already at the last index, no jumps needed
        return 0

    # WHY: jumps counts the number of jumps taken so far
    jumps: int = 0
    # WHY: current_end marks the furthest index reachable with the current number of jumps
    current_end: int = 0
    # WHY: farthest tracks the absolute furthest index reachable from the current level
    farthest: int = 0

    # WHY: Iterate through positions up to n-2 (we don't need to jump from last position)
    for i in range(n - 1):
        # WHY: Update the farthest position reachable from current position
        farthest = max(farthest, i + nums[i])

        # WHY: If we have reached the end of the current jump range
        if i == current_end:
            # WHY: Take a jump (moving to the next level)
            jumps += 1
            # WHY: Set the new boundary to the farthest position reachable
            current_end = farthest

            # WHY: If we can already reach the last index, early exit
            if current_end >= n - 1:
                break

    return jumps


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Jump Game II...")

    # Test case 1: Standard case
    nums1 = [2, 3, 1, 1, 4]
    assert solution_optimal(nums1) == 2, f"Test 1 optimal failed: {solution_optimal(nums1)}"
    assert solution_brute(nums1) == 2, f"Test 1 brute failed"
    print("Test 1 ([2,3,1,1,4] -> 2) passed!")

    # Test case 2: Single element (already at destination)
    assert solution_optimal([0]) == 0, "Test 2 optimal failed"
    assert solution_brute([0]) == 0, "Test 2 brute failed"
    print("Test 2 ([0] -> 0) passed!")

    # Test case 3: Two elements
    nums3 = [2, 1]
    assert solution_optimal(nums3) == 1, f"Test 3 optimal failed"
    assert solution_brute(nums3) == 1, f"Test 3 brute failed"
    print("Test 3 ([2,1] -> 1) passed!")

    # Test case 4: Large first jump skips many
    nums4 = [5, 1, 1, 1, 1, 1]
    assert solution_optimal(nums4) == 1, f"Test 4 optimal failed"
    assert solution_brute(nums4) == 1, f"Test 4 brute failed"
    print("Test 4 ([5,1,1,1,1,1] -> 1) passed!")

    # Test case 5: Each jump is 1
    nums5 = [1, 1, 1, 1, 1]
    assert solution_optimal(nums5) == 4, f"Test 5 optimal failed: {solution_optimal(nums5)}"
    assert solution_brute(nums5) == 4, f"Test 5 brute failed"
    print("Test 5 ([1,1,1,1,1] -> 4) passed!")

    print(f"Brute force verification: {solution_brute([2,3,1,1,4])}")
    print("All tests passed!")
