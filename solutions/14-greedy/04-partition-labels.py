"""
LC 763. Partition Labels (划分字母区间)
Difficulty: Medium
Tags: String, Hash Table, Two Pointers, Greedy
Link: https://leetcode.cn/problems/partition-labels/
Category: greedy
"""

from typing import List


# ===== 暴力解法 =====
# 思路: Try all possible partition positions. For each candidate partition [start, end],
#       check if any character in this segment appears outside the segment.
#       If all characters are confined, commit the partition and start a new segment.
# 复杂度: O(n^2) time, O(1) space (excluding output)
def solution_brute(s: str) -> List[int]:
    """
    Partition the string so that each character appears in at most one segment.
    Uses brute force checking all partitions.
    """
    n: int = len(s)
    result: List[int] = []
    start: int = 0

    # WHY: Keep partitioning until we reach the end of string
    while start < n:
        # WHY: Candidate end position for current partition
        end: int = start

        # WHY: Expand the partition end until all characters are confined
        while end < n:
            # WHY: Extract the current candidate segment chars (set for unique check)
            segment_chars: set = set(s[start:end + 1])
            # WHY: Check if any character in the segment appears after `end`
            overlap: bool = False
            for ch in segment_chars:
                # WHY: If character appears after end, the partition is not valid
                if ch in s[end + 1:]:
                    overlap = True
                    # WHY: Move end to the last occurrence of this character
                    end = s.rindex(ch, end + 1)
                    break

            if not overlap:
                # WHY: All characters in this segment are confined — commit partition
                break

        # WHY: Record the length of this partition
        result.append(end - start + 1)
        # WHY: Move start to the next position after the committed partition
        start = end + 1

    return result


# ===== 最优解法 =====
# 思路: Two-pass greedy. First pass: record the last occurrence index of each character.
#       Second pass: iterate through the string, tracking the furthest last occurrence
#       seen so far (current_end). When current index reaches current_end, a partition
#       ends. Record its length and start a new partition.
# 复杂度: O(n) time, O(1) space (hash map has at most 26 entries for lowercase letters)
def solution_optimal(s: str) -> List[int]:
    """
    Partition the string so that each character appears in at most one segment.
    Uses greedy approach with last-occurrence tracking.
    """
    # WHY: First pass: record the last index where each character appears
    last_occurrence: dict = {}
    for i, ch in enumerate(s):
        # WHY: Each iteration updates/replaces the character's last seen index
        last_occurrence[ch] = i

    result: List[int] = []
    # WHY: Track the start of the current partition
    partition_start: int = 0
    # WHY: Track the furthest last occurrence seen in the current partition
    current_end: int = 0

    # WHY: Second pass: determine partition boundaries
    for i, ch in enumerate(s):
        # WHY: Extend the current partition's end to include this character's last occurrence
        current_end = max(current_end, last_occurrence[ch])

        # WHY: If current index reaches the partition end, this partition is complete
        if i == current_end:
            # WHY: Record the partition length
            result.append(i - partition_start + 1)
            # WHY: Start a new partition at the next index
            partition_start = i + 1

    return result


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Partition Labels...")

    # Test case 1: Standard case
    s1 = "ababcbacadefegdehijhklij"
    expected1 = [9, 7, 8]
    assert solution_optimal(s1) == expected1, f"Test 1 optimal failed: {solution_optimal(s1)}"
    assert solution_brute(s1) == expected1, f"Test 1 brute failed: {solution_brute(s1)}"
    print("Test 1 passed!")

    # Test case 2: Single character
    assert solution_optimal("a") == [1], "Test 2 optimal failed"
    assert solution_brute("a") == [1], "Test 2 brute failed"
    print("Test 2 (\"a\" -> [1]) passed!")

    # Test case 3: All distinct characters (each in its own partition)
    s3 = "abcdef"
    expected3 = [1, 1, 1, 1, 1, 1]
    assert solution_optimal(s3) == expected3, f"Test 3 optimal failed"
    assert solution_brute(s3) == expected3, f"Test 3 brute failed"
    print("Test 3 (\"abcdef\" -> [1,1,1,1,1,1]) passed!")

    # Test case 4: All same character (one partition)
    assert solution_optimal("aaa") == [3], "Test 4 optimal failed"
    assert solution_brute("aaa") == [3], "Test 4 brute failed"
    print("Test 4 (\"aaa\" -> [3]) passed!")

    # Test case 5: No overlap between groups
    s5 = "abac"
    expected5 = [3, 1]
    assert solution_optimal(s5) == expected5, f"Test 5 optimal failed: {solution_optimal(s5)}"
    assert solution_brute(s5) == expected5, f"Test 5 brute failed"
    print("Test 5 (\"abac\" -> [3,1]) passed!")

    print(f"Brute force verification: {solution_brute('ababcbacadefegdehijhklij')}")
    print("All tests passed!")
