"""
LC 152. Maximum Product Subarray (乘积最大子数组)
Difficulty: Medium
Tags: Array, Dynamic Programming
Link: https://leetcode.cn/problems/maximum-product-subarray/
Category: 15-dp
"""

from typing import List


# ===== 暴力解法 =====
# 思路: 枚举所有可能的子数组，计算每个子数组的乘积，记录最大值。
# 复杂度: O(n^2) time, O(1) space
def solution_brute(nums: List[int]) -> int:
    # WHY: 处理空数组的边界情况
    if not nums:
        return 0
    # WHY: 初始化最大乘积为数组第一个元素
    max_prod = nums[0]
    # WHY: 枚举所有子数组的起始位置
    for i in range(len(nums)):
        # WHY: curr记录从i开始到当前j的子数组乘积
        curr = 1
        # WHY: 枚举所有子数组的结束位置
        for j in range(i, len(nums)):
            # WHY: 累乘当前元素到当前子数组乘积
            curr *= nums[j]
            # WHY: 更新全局最大乘积
            max_prod = max(max_prod, curr)
    # WHY: 返回最大乘积
    return max_prod


# ===== 最优解法 =====
# 思路: 由于负数乘以负数会得到正数，所以需要同时跟踪当前的最大乘积和最小乘积（最小乘积可能是负数）。
#        对于每个新元素，新的最大值可能是：当前元素本身、最大乘积×当前元素、最小乘积×当前元素。
# 复杂度: O(n) time, O(1) space
def solution_optimal(nums: List[int]) -> int:
    # WHY: 处理空数组的边界情况
    if not nums:
        return 0
    # WHY: 初始化全局最大乘积为第一个元素
    max_product = nums[0]
    # WHY: cur_max和cur_min分别表示以当前元素结尾的子数组的最大和最小乘积
    cur_max = nums[0]
    cur_min = nums[0]
    # WHY: 从第二个元素开始遍历
    for i in range(1, len(nums)):
        # WHY: 当前元素
        num = nums[i]
        # WHY: 暂存cur_max的旧值，因为计算cur_min时需要用到旧值
        temp_max = cur_max
        # WHY: 新的最大乘积：可能是当前元素、最大乘积×当前元素、最小乘积×当前元素（负负得正）
        cur_max = max(num, cur_max * num, cur_min * num)
        # WHY: 新的最小乘积：可能是当前元素、最大乘积×当前元素、最小乘积×当前元素
        cur_min = min(num, temp_max * num, cur_min * num)
        # WHY: 更新全局最大乘积
        max_product = max(max_product, cur_max)
    # WHY: 返回全局最大乘积
    return max_product


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Maximum Product Subarray...")

    # 测试用例1: [2,3,-2,4] → 6 (子数组[2,3])
    test1 = [2, 3, -2, 4]
    expected1 = 6
    assert solution_brute(test1) == expected1, f"brute test1 failed"
    assert solution_optimal(test1) == expected1, f"optimal test1 failed"

    # 测试用例2: [-2,0,-1] → 0 (子数组[0])
    test2 = [-2, 0, -1]
    expected2 = 0
    assert solution_brute(test2) == expected2, f"brute test2 failed"
    assert solution_optimal(test2) == expected2, f"optimal test2 failed"

    # 测试用例3: [-2,3,-4] → 24 (子数组[-2,3,-4], 负数×正数×负数=正数)
    test3 = [-2, 3, -4]
    expected3 = 24
    assert solution_brute(test3) == expected3, f"brute test3 failed"
    assert solution_optimal(test3) == expected3, f"optimal test3 failed"

    print(f"Brute force: {solution_brute(test1)}")
    print("All tests passed!")
