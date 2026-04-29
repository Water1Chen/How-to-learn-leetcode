"""
LC 31. Next Permutation (下一个排列)
Difficulty: Medium
Tags: Array, Two Pointers
Link: https://leetcode.cn/problems/next-permutation/
Category: 17-tricks
"""

from typing import List


# ===== 暴力解法 =====
# 思路: 生成所有可能的排列，排序后找到当前排列的下一个排列。
#        使用itertools.permutations生成所有排列，去重后排序。
# 复杂度: O(n!) time, O(n!) space
def solution_brute(nums: List[int]) -> None:
    # WHY: 导入itertools生成所有排列
    import itertools
    # WHY: 保存原数组的副本，用于查找位置
    original = tuple(nums)
    # WHY: 生成所有排列，去重并排序
    perms = sorted(set(itertools.permutations(nums)))
    # WHY: 找到当前排列在排序后列表中的位置
    idx = perms.index(original)
    # WHY: 如果存在下一个排列，取下一个；否则取第一个（循环）
    next_perm = perms[(idx + 1) % len(perms)]
    # WHY: 修改原数组为下一个排列
    nums[:] = list(next_perm)


# ===== 最优解法 =====
# 思路: 从右向左找到第一个下降点（nums[i] < nums[i+1]），
#        然后从右向左找到第一个大于nums[i]的元素（即刚好比nums[i]大的数），
#        交换两者，然后将i之后的序列反转（因为后面的序列是降序的，反转后变为升序，即最小排列）。
# 复杂度: O(n) time, O(1) space
def solution_optimal(nums: List[int]) -> None:
    # WHY: 处理边界情况，长度小于2时无需操作
    if len(nums) < 2:
        return

    # WHY: 步骤1：从右向左找到第一个下降点i，即nums[i] < nums[i+1]
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    # WHY: 如果找到了下降点（即i >= 0），说明不是最后一个排列
    if i >= 0:
        # WHY: 步骤2：从右向左找到第一个大于nums[i]的元素（刚好比nums[i]大的最右边的元素）
        j = len(nums) - 1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1
        # WHY: 步骤3：交换nums[i]和nums[j]，完成"进位"
        nums[i], nums[j] = nums[j], nums[i]

    # WHY: 步骤4：将i之后的序列反转（原来为降序，反转后变为升序，即最小排列）
    left = i + 1
    right = len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Next Permutation...")

    # 测试用例1: [1,2,3] → [1,3,2]
    test1 = [1, 2, 3]
    expected1 = [1, 3, 2]
    test1_copy = test1.copy()
    solution_optimal(test1_copy)
    assert test1_copy == expected1, f"optimal test1 failed: {test1_copy}"

    # 测试用例2: [3,2,1] → [1,2,3] (降序排列，下一个是升序的第一个排列)
    test2 = [3, 2, 1]
    expected2 = [1, 2, 3]
    test2_copy = test2.copy()
    solution_optimal(test2_copy)
    assert test2_copy == expected2, f"optimal test2 failed: {test2_copy}"

    # 测试用例3: [1,1,5] → [1,5,1]
    test3 = [1, 1, 5]
    expected3 = [1, 5, 1]
    test3_copy = test3.copy()
    solution_optimal(test3_copy)
    assert test3_copy == expected3, f"optimal test3 failed: {test3_copy}"

    print("All tests passed!")
