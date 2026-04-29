"""
LC 75. Sort Colors (颜色分类)
Difficulty: Medium
Tags: Array, Two Pointers, Sorting
Link: https://leetcode.cn/problems/sort-colors/
Category: 17-tricks
"""

from typing import List


# ===== 暴力解法 =====
# 思路: 计数排序，先遍历一遍统计0、1、2的个数，然后按顺序覆盖原数组。
#        需要两次遍历。
# 复杂度: O(n) time, O(1) space
def solution_brute(nums: List[int]) -> None:
    # WHY: 初始化三个颜色计数器
    count0 = count1 = count2 = 0
    # WHY: 第一次遍历，统计每种颜色的数量
    for num in nums:
        if num == 0:
            count0 += 1
        elif num == 1:
            count1 += 1
        else:
            count2 += 1
    # WHY: 第二次遍历，按顺序覆盖原数组（先0，再1，最后2）
    for i in range(len(nums)):
        if i < count0:
            nums[i] = 0
        elif i < count0 + count1:
            nums[i] = 1
        else:
            nums[i] = 2


# ===== 最优解法 =====
# 思路: 荷兰国旗问题（Dutch National Flag），使用三个指针p0、curr、p2。
#        p0始终指向下一个0应该放置的位置，p2始终指向下一个2应该放置的位置。
#        curr遍历数组，遇到0与p0交换，遇到2与p2交换，遇到1跳过。
#        只需一次遍历。
# 复杂度: O(n) time, O(1) space
def solution_optimal(nums: List[int]) -> None:
    # WHY: p0指向下一个0应该放置的位置（从左向右）
    p0 = 0
    # WHY: p2指向下一个2应该放置的位置（从右向左）
    p2 = len(nums) - 1
    # WHY: curr是当前遍历指针
    curr = 0
    # WHY: 一次遍历，直到curr超过p2
    while curr <= p2:
        # WHY: 如果当前元素是0，将其交换到左侧p0位置
        if nums[curr] == 0:
            # WHY: 交换curr和p0位置的元素
            nums[curr], nums[p0] = nums[p0], nums[curr]
            # WHY: p0右移，curr右移（因为交换过来的p0元素一定是处理过的）
            p0 += 1
            curr += 1
        # WHY: 如果当前元素是2，将其交换到右侧p2位置
        elif nums[curr] == 2:
            # WHY: 交换curr和p2位置的元素
            nums[curr], nums[p2] = nums[p2], nums[curr]
            # WHY: p2左移，curr不移动（因为交换过来的新元素还需要检查）
            p2 -= 1
        else:
            # WHY: 当前元素是1，不需要交换，直接跳过
            curr += 1


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Sort Colors...")

    # 测试用例1: [2,0,2,1,1,0] → [0,0,1,1,2,2]
    test1 = [2, 0, 2, 1, 1, 0]
    expected1 = [0, 0, 1, 1, 2, 2]
    test1_copy = test1.copy()
    solution_brute(test1_copy)
    assert test1_copy == expected1, f"brute test1 failed: {test1_copy}"
    test1_copy2 = test1.copy()
    solution_optimal(test1_copy2)
    assert test1_copy2 == expected1, f"optimal test1 failed: {test1_copy2}"

    # 测试用例2: [2,0,1] → [0,1,2]
    test2 = [2, 0, 1]
    expected2 = [0, 1, 2]
    test2_copy = test2.copy()
    solution_brute(test2_copy)
    assert test2_copy == expected2, f"brute test2 failed: {test2_copy}"
    test2_copy2 = test2.copy()
    solution_optimal(test2_copy2)
    assert test2_copy2 == expected2, f"optimal test2 failed: {test2_copy2}"

    print(f"Brute force (counting sort): {test1_copy}")
    print("All tests passed!")
