"""
LC 287. Find the Duplicate Number (寻找重复数)
Difficulty: Medium
Tags: Bit Manipulation, Array, Two Pointers, Binary Search
Link: https://leetcode.cn/problems/find-the-duplicate-number/
Category: 17-tricks
"""

from typing import List


# ===== 暴力解法 =====
# 思路: 使用哈希集合（或排序）。遍历数组，如果当前元素已经在集合中，则找到重复数。
#        或者先排序，然后检查相邻元素是否相等。
# 复杂度: O(n) time (HashSet) / O(n log n) time (sort), O(n) space
def solution_brute(nums: List[int]) -> int:
    # WHY: 使用集合存储已经遍历过的元素
    seen: set = set()
    # WHY: 遍历数组中的每个元素
    for num in nums:
        # WHY: 如果当前元素已在集合中，说明找到了重复数
        if num in seen:
            return num
        # WHY: 否则将当前元素加入集合
        seen.add(num)
    # WHY: 根据题意一定存在重复数，这里返回-1只是为了类型安全
    return -1


# ===== 方法一：Floyd判圈算法（最优）=====
# 思路: 将数组视为一个链表，索引i指向nums[i]（因为数字范围在1~n之间）。
#        重复的数字会导致环的出现。使用快慢指针找到环的入口，即为重复数。
#        第一阶段：快慢指针在环内相遇。第二阶段：重新从头和相遇点同步前进，相遇点即为环入口。
# 复杂度: O(n) time, O(1) space
def solution_floyd(nums: List[int]) -> int:
    # WHY: 第一阶段：快慢指针寻找环内的相遇点
    # WHY: 慢指针每次走一步
    slow = nums[0]
    # WHY: 快指针每次走两步
    fast = nums[0]
    # WHY: 先移动一次找到初始差异，或者用do-while方式
    # WHY: 快慢指针在环内移动直到相遇
    while True:
        # WHY: 慢指针走一步
        slow = nums[slow]
        # WHY: 快指针走两步
        fast = nums[nums[fast]]
        # WHY: 如果快慢指针相遇，说明找到环内的一个点
        if slow == fast:
            break

    # WHY: 第二阶段：从头和相遇点同步前进，相遇处即为环入口（重复数）
    # WHY: 新指针从头开始
    finder = nums[0]
    # WHY: 当头指针与慢指针相遇时，该点即为环入口
    while finder != slow:
        # WHY: 两指针都以相同速度前进
        finder = nums[finder]
        slow = nums[slow]
    # WHY: 返回环入口，即重复的数字
    return finder


# ===== 方法二：二分查找 =====
# 思路: 对数字范围[1, n]进行二分查找。对于中间值mid，统计数组中<=mid的元素个数cnt。
#        如果cnt > mid，说明重复数在[1, mid]范围内，否则在[mid+1, n]范围内。
#        基于鸽巢原理。
# 复杂度: O(n log n) time, O(1) space
def solution_binary_search(nums: List[int]) -> int:
    # WHY: 定义搜索范围[1, n-1]
    left = 1
    right = len(nums) - 1
    # WHY: 二分查找
    while left < right:
        # WHY: 计算中间值
        mid = (left + right) // 2
        # WHY: 统计数组中值小于等于mid的元素个数
        count = 0
        for num in nums:
            if num <= mid:
                count += 1
        # WHY: 如果count > mid，说明[1,mid]中有重复数（鸽巢原理）
        if count > mid:
            right = mid
        else:
            # WHY: 否则重复数在[mid+1, right]中
            left = mid + 1
    # WHY: 返回找到的重复数
    return left


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Find the Duplicate Number...")

    # 测试用例1: [1,3,4,2,2] → 2
    test1 = [1, 3, 4, 2, 2]
    expected1 = 2
    assert solution_brute(test1) == expected1, f"brute test1 failed"
    assert solution_floyd(test1) == expected1, f"floyd test1 failed"
    assert solution_binary_search(test1) == expected1, f"binary search test1 failed"

    # 测试用例2: [3,1,3,4,2] → 3
    test2 = [3, 1, 3, 4, 2]
    expected2 = 3
    assert solution_brute(test2) == expected2, f"brute test2 failed"
    assert solution_floyd(test2) == expected2, f"floyd test2 failed"
    assert solution_binary_search(test2) == expected2, f"binary search test2 failed"

    # 测试用例3: [1,1] → 1
    test3 = [1, 1]
    expected3 = 1
    assert solution_brute(test3) == expected3, f"brute test3 failed"
    assert solution_floyd(test3) == expected3, f"floyd test3 failed"
    assert solution_binary_search(test3) == expected3, f"binary search test3 failed"

    print(f"Brute force (HashSet): {solution_brute(test1)}")
    print("All tests passed!")
