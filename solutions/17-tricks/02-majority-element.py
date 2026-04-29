"""
LC 169. Majority Element (多数元素)
Difficulty: Easy
Tags: Array, Hash Table, Divide and Conquer, Counting
Link: https://leetcode.cn/problems/majority-element/
Category: 17-tricks
"""

from typing import List


# ===== 暴力解法 =====
# 思路: 使用哈希表统计每个元素出现的次数，找出出现次数超过n/2的元素。
# 复杂度: O(n) time, O(n) space
def solution_brute(nums: List[int]) -> int:
    # WHY: 计算多数元素需要出现的阈值（超过n/2）
    threshold = len(nums) // 2
    # WHY: 创建哈希表统计每个元素出现次数
    count_map: dict = {}
    # WHY: 遍历数组统计每个数字的出现次数
    for num in nums:
        count_map[num] = count_map.get(num, 0) + 1
    # WHY: 遍历哈希表，找出出现次数超过阈值的元素
    for num, count in count_map.items():
        if count > threshold:
            return num
    # WHY: 根据题意一定存在多数元素，返回-1只是为了类型安全
    return -1


# ===== 最优解法 =====
# 思路: Boyer-Moore投票算法。核心思想是不同元素相互抵消。维护一个候选元素和计数器，
#        遍历数组，如果计数器为0则更新候选元素；遇到相同元素计数+1，不同元素计数-1。
#        由于多数元素出现次数超过n/2，最后剩下的候选元素一定是多数元素。
# 复杂度: O(n) time, O(1) space
def solution_optimal(nums: List[int]) -> int:
    # WHY: 初始化候选元素和计数器
    candidate = nums[0]
    count = 0
    # WHY: 遍历数组中的所有元素
    for num in nums:
        # WHY: 如果计数器为0，将当前元素设为新的候选者
        if count == 0:
            candidate = num
        # WHY: 如果当前元素等于候选者，计数加1（投支持票）
        if num == candidate:
            count += 1
        else:
            # WHY: 当前元素不等于候选者，计数减1（不同元素相互抵消）
            count -= 1
    # WHY: 最终的候选者就是多数元素（因为多数元素数量超过n/2，不会被完全抵消）
    return candidate


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Majority Element...")

    # 测试用例1: [3,2,3] → 3
    test1 = [3, 2, 3]
    expected1 = 3
    assert solution_brute(test1) == expected1, f"brute test1 failed"
    assert solution_optimal(test1) == expected1, f"optimal test1 failed"

    # 测试用例2: [2,2,1,1,1,2,2] → 2
    test2 = [2, 2, 1, 1, 1, 2, 2]
    expected2 = 2
    assert solution_brute(test2) == expected2, f"brute test2 failed"
    assert solution_optimal(test2) == expected2, f"optimal test2 failed"

    # 测试用例3: [1] → 1
    test3 = [1]
    expected3 = 1
    assert solution_brute(test3) == expected3, f"brute test3 failed"
    assert solution_optimal(test3) == expected3, f"optimal test3 failed"

    print(f"Hash map: {solution_brute(test1)}")
    print("All tests passed!")
