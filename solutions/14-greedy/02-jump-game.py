"""
LC 55. Jump Game (跳跃游戏)
Difficulty: Medium
Tags: Array, Dynamic Programming, Greedy
Link: https://leetcode.cn/problems/jump-game/
Category: greedy
"""

from typing import List


# ===== 暴力解法 =====
# 思路: DP with memoization: dp[i] indicates whether we can reach the last index
#       from position i. Starting from the last position (which is trivially reachable),
#       work backwards. For each position i, try all jump lengths from 1 to nums[i]
#       and see if any reachable position exists ahead.
# 复杂度: O(n^2) time (worst case: each position jumps to all later positions),
#         O(n) space for DP array
def solution_brute(nums: List[int]) -> bool:
    """
    Determine if we can reach the last index using DP.
    """
    n: int = len(nums)
    if n == 0:
        return False

    # WHY: dp[i] = True if we can reach the last index from position i
    dp: List[bool] = [False] * n
    # WHY: Last position is always reachable from itself
    dp[n - 1] = True

    # WHY: Work backwards from second-to-last position to start
    for i in range(n - 2, -1, -1):
        # WHY: Determine the farthest position we can jump to from position i
        max_jump: int = min(i + nums[i], n - 1)
        # WHY: Try all possible landing positions from (i+1) to max_jump
        for j in range(i + 1, max_jump + 1):
            # WHY: If any landing position can reach the end, then i can also reach the end
            if dp[j]:
                dp[i] = True
                # WHY: No need to check further jumps from i
                break

    # WHY: Return whether we can reach the last index from position 0
    return dp[0]


# ===== 最优解法 =====
# 思路: Greedy: track the farthest index reachable so far. Iterate through the array,
#       updating the farthest reachable position. If at any point i exceeds the
#       farthest reachable position, we are stuck. If the farthest reachable position
#       reaches or passes the last index, return True.
# 复杂度: O(n) time, O(1) space
def solution_optimal(nums: List[int]) -> bool:
    """
    Determine if we can reach the last index using greedy approach.
    """
    n: int = len(nums)
    # WHY: Track the farthest position we can reach from any visited position so far
    farthest: int = 0

    # WHY: Iterate through each position in the array
    for i in range(n):
        # WHY: If current index is beyond our farthest reachable position, we are stuck
        if i > farthest:
            return False

        # WHY: Update farthest reachable position from current position
        # WHY: From i, we can jump up to i + nums[i]
        farthest = max(farthest, i + nums[i])

        # WHY: Early exit — if farthest already reaches or passes the last index
        if farthest >= n - 1:
            return True

    # WHY: Should have returned True already; fallback check
    return farthest >= n - 1


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Jump Game...")

    # Test case 1: Can reach the end
    nums1 = [2, 3, 1, 1, 4]
    assert solution_optimal(nums1) == True, f"Test 1 optimal failed"
    assert solution_brute(nums1) == True, f"Test 1 brute failed"
    print("Test 1 ([2,3,1,1,4] -> true) passed!")

    # Test case 2: Cannot reach the end
    nums2 = [3, 2, 1, 0, 4]
    assert solution_optimal(nums2) == False, f"Test 2 optimal failed"
    assert solution_brute(nums2) == False, f"Test 2 brute failed"
    print("Test 2 ([3,2,1,0,4] -> false) passed!")

    # Test case 3: Single element (already at end)
    assert solution_optimal([0]) == True, "Test 3 optimal failed"
    assert solution_brute([0]) == True, "Test 3 brute failed"
    print("Test 3 ([0] -> true) passed!")

    # Test case 4: All zeros except first (cannot proceed)
    nums4 = [1, 0, 0, 0]
    assert solution_optimal(nums4) == False, f"Test 4 optimal failed"
    assert solution_brute(nums4) == False, f"Test 4 brute failed"
    print("Test 4 ([1,0,0,0] -> false) passed!")

    # Test case 5: Large jumps
    nums5 = [10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert solution_optimal(nums5) == True, f"Test 5 optimal failed"
    assert solution_brute(nums5) == True, f"Test 5 brute failed"
    print("Test 5 (large first jump) passed!")

    print(f"Brute force verification: {solution_brute([2,3,1,1,4])}")
    print("All tests passed!")
