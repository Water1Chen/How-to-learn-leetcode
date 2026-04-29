"""
LC 136. Single Number (只出现一次的数字)
Difficulty: Easy
Tags: Bit Manipulation, Array
Link: https://leetcode.cn/problems/single-number/
Category: 17-tricks
"""

from typing import List


# ===== 暴力解法 =====
# 思路: 使用哈希表统计每个数字出现的次数，然后找出出现次数为1的数字。
# 复杂度: O(n) time, O(n) space
def solution_brute(nums: List[int]) -> int:
    # WHY: 创建哈希表用于统计每个数字的出现次数
    count_map: dict = {}
    # WHY: 遍历数组，统计每个数字的出现次数
    for num in nums:
        count_map[num] = count_map.get(num, 0) + 1
    # WHY: 遍历哈希表，找出出现次数为1的数字
    for num, count in count_map.items():
        if count == 1:
            return num
    # WHY: 根据题意一定存在结果，这里返回-1只是为了通过类型检查
    return -1


# ===== 最优解法 =====
# 思路: 利用异或运算的性质：a^a=0（相同数字异或为0），a^0=a（任何数字和0异或为自身）。
#        对数组中所有数字进行异或，成对出现的数字会抵消为0，最终结果就是只出现一次的数字。
#        异或运算满足交换律和结合律，所以顺序不影响结果。
# 复杂度: O(n) time, O(1) space
def solution_optimal(nums: List[int]) -> int:
    # WHY: 初始化结果为0（0异或任何数等于该数本身）
    result = 0
    # WHY: 遍历数组中的所有数字，逐个异或
    for num in nums:
        # WHY: 异或运算：相同的数字会抵消（a^a=0），最终剩下列表中只出现一次的数字
        result ^= num
    # WHY: 返回只出现一次的数字
    return result


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Single Number...")

    # 测试用例1: [2,2,1] → 1
    test1 = [2, 2, 1]
    expected1 = 1
    assert solution_brute(test1) == expected1, f"brute test1 failed"
    assert solution_optimal(test1) == expected1, f"optimal test1 failed"

    # 测试用例2: [4,1,2,1,2] → 4
    test2 = [4, 1, 2, 1, 2]
    expected2 = 4
    assert solution_brute(test2) == expected2, f"brute test2 failed"
    assert solution_optimal(test2) == expected2, f"optimal test2 failed"

    # 测试用例3: [1] → 1
    test3 = [1]
    expected3 = 1
    assert solution_brute(test3) == expected3, f"brute test3 failed"
    assert solution_optimal(test3) == expected3, f"optimal test3 failed"

    print(f"Hash map: {solution_brute(test1)}")
    print("All tests passed!")
