"""
LC 56. Merge Intervals (合并区间)
Difficulty: Medium
Tags: Array, Sorting
Link: https://leetcode.cn/problems/merge-intervals/
Category: 05-array
"""

from typing import List


# ===== 暴力解法 =====
# 思路: 两层循环，对每个区间检查是否与其他区间重叠，合并后标记已处理
# 复杂度: O(n^2) time, O(n) space
def solution_brute(intervals: List[List[int]]) -> List[List[int]]:
    # WHY: 暴力法需要反复扫描和合并，实现复杂且低效
    # 简化思路：排序后两两合并，但这里演示真正的O(n^2)暴力思路
    if not intervals:
        return []

    merged = [list(interval) for interval in intervals]  # WHY: 拷贝一份用于合并操作
    changed = True  # WHY: 标记本轮是否有合并发生
    while changed:
        changed = False
        i = 0
        while i < len(merged):
            j = i + 1
            while j < len(merged):
                # WHY: 检查merged[i]和merged[j]是否重叠
                # 重叠条件: 一个区间的start <= 另一个区间的end
                if not (merged[i][1] < merged[j][0] or merged[j][1] < merged[i][0]):
                    # WHY: 合并两个区间: 取较小的start和较大的end
                    merged[i][0] = min(merged[i][0], merged[j][0])
                    merged[i][1] = max(merged[i][1], merged[j][1])
                    merged.pop(j)  # WHY: 删除被合并的区间
                    changed = True
                    # WHY: 合并后重新检查merged[i]是否与其他区间重叠
                else:
                    j += 1
            i += 1
    return merged


# ===== 最优解法 =====
# 思路: 先按区间起点排序，然后一次遍历合并重叠区间
#       排序后，重叠的区间必然连续出现，只需维护当前合并区间的终点
# 复杂度: O(n log n) time (排序是瓶颈), O(n) space (存储结果)
def solution_optimal(intervals: List[List[int]]) -> List[List[int]]:
    # WHY: 排序是关键优化 — 按起点排序后，重叠区间必然相邻，无需回溯
    # WHY: 相比暴力法O(n^2)，排序+一次遍历降至O(n log n)
    if not intervals:
        return []

    # WHY: 按区间起点排序，保证后续遍历时重叠关系只向后延伸
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0][:]]  # WHY: 第一个区间直接加入结果，作为初始合并区间

    for i in range(1, len(intervals)):
        current_start, current_end = intervals[i]
        last_merged = merged[-1]  # WHY: 获取当前最后一个已合并的区间

        if current_start <= last_merged[1]:
            # WHY: 当前区间与已合并区间重叠，扩展已合并区间的终点
            # WHY: 取较大值作为新终点，因为排序只保证了起点有序
            last_merged[1] = max(last_merged[1], current_end)
        else:
            # WHY: 不重叠，将当前区间作为新的独立区间加入结果
            merged.append([current_start, current_end])

    return merged


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Merge Intervals...")

    # 测试用例1: 标准情况
    intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    expected1 = [[1, 6], [8, 10], [15, 18]]
    result1 = solution_optimal(intervals1)
    print(f"Test 1: {result1} == {expected1} -> {'PASS' if result1 == expected1 else 'FAIL'}")

    # 测试用例2: 完全覆盖
    intervals2 = [[1, 4], [4, 5]]
    expected2 = [[1, 5]]
    result2 = solution_optimal(intervals2)
    print(f"Test 2: {result2} == {expected2} -> {'PASS' if result2 == expected2 else 'FAIL'}")

    # 测试用例3: 无重叠
    intervals3 = [[1, 2], [3, 4], [5, 6]]
    expected3 = [[1, 2], [3, 4], [5, 6]]
    result3 = solution_optimal(intervals3)
    print(f"Test 3: {result3} == {expected3} -> {'PASS' if result3 == expected3 else 'FAIL'}")

    # 测试用例4: 完全包含
    intervals4 = [[1, 10], [2, 6], [3, 5]]
    expected4 = [[1, 10]]
    result4 = solution_optimal(intervals4)
    print(f"Test 4: {result4} == {expected4} -> {'PASS' if result4 == expected4 else 'FAIL'}")

    print("\nAll tests complete!")
