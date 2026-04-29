"""
LC 15. 三数之和 (3Sum)
Difficulty: Medium
Tags: Array, Two Pointers, Sorting
Link: https://leetcode.cn/problems/3sum/
Category: 02-two-pointers
"""

from typing import List


# ===== 暴力解法 =====
# 思路: 三重循环枚举所有三元组，用集合去重后返回。
# 复杂度: O(n³) time, O(n) space for set
def solution_brute(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    # WHY: 使用集合去重，避免重复的三元组
    result_set = set()

    # WHY: 三重循环枚举所有可能的三元组
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # WHY: 检查三数之和是否为 0
                if nums[i] + nums[j] + nums[k] == 0:
                    # WHY: 排序后转元组，确保集合去重能正确判断
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    result_set.add(triplet)

    # WHY: 将元组集合转回列表格式
    return [list(t) for t in result_set]


# ===== 最优解法 =====
# 思路: 先排序，固定第一个数 i，再用双指针 left/right 在 i 右侧找两数之和为 -nums[i]。
#       排序后天然去重（相邻相同值跳过），双指针将内层 O(n) 优化到 O(n)。
# 复杂度: O(n²) time, O(log n) ~ O(n) space for sorting
def solution_optimal(nums: List[int]) -> List[List[int]]:
    # WHY: 排序是双指针的前提，让数组有序才能用左右指针逼近
    nums.sort()
    n = len(nums)
    result: List[List[int]] = []

    # WHY: 只需遍历到 n-2，因为至少需要三个数
    for i in range(n - 2):
        # WHY: 跳过重复的固定元素，避免结果中出现重复三元组
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # WHY: 当前最小值已大于 0，后面不可能凑出和为 0 的三元组
        if nums[i] > 0:
            break

        # WHY: 双指针在 i 之后的区间中查找两数之和为 -nums[i]
        left = i + 1
        right = n - 1
        target = -nums[i]

        while left < right:
            cur_sum = nums[left] + nums[right]

            if cur_sum == target:
                # WHY: 找到一组解，加入结果
                result.append([nums[i], nums[left], nums[right]])
                # WHY: 跳过左侧重复值
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                # WHY: 跳过右侧重复值
                right -= 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif cur_sum < target:
                # WHY: 和太小，左指针右移增大和
                left += 1
            else:
                # WHY: 和太大，右指针左移减小和
                right -= 1

    return result


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing 3Sum...")

    # Test case 1 - 基础用例
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution_optimal(nums1)
    expected1 = [[-1, -1, 2], [-1, 0, 1]]
    sorted_result1 = sorted([sorted(t) for t in result1])
    sorted_expected1 = sorted([sorted(t) for t in expected1])
    print(f"Test 1: {sorted_result1} == {sorted_expected1} -> {'PASS' if sorted_result1 == sorted_expected1 else 'FAIL'}")

    # Test case 2 - 无解
    nums2 = [0, 1, 1]
    result2 = solution_optimal(nums2)
    print(f"Test 2: {result2} == [] -> {'PASS' if result2 == [] else 'FAIL'}")

    # Test case 3 - 全零
    nums3 = [0, 0, 0]
    result3 = solution_optimal(nums3)
    print(f"Test 3: {result3} == [[0,0,0]] -> {'PASS' if result3 == [[0,0,0]] else 'FAIL'}")

    # Test case 4 - 不足三个元素
    nums4 = [0]
    result4 = solution_optimal(nums4)
    print(f"Test 4: {result4} == [] -> {'PASS' if result4 == [] else 'FAIL'}")

    # 验证暴力解法
    print("\nBrute force verification:")
    sorted_brute1 = sorted([sorted(t) for t in solution_brute(nums1)])
    print(f"Brute Test 1: {sorted_brute1}")

    print("\nAll tests complete!")
