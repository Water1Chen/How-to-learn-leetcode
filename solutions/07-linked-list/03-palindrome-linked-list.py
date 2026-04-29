"""
LC 234. Palindrome Linked List (回文链表)
Difficulty: Easy
Tags: Linked List, Two Pointers, Stack, Recursion
Link: https://leetcode.cn/problems/palindrome-linked-list/
Category: 07-linked-list
"""

from typing import Optional


class ListNode:
    # WHY: 链表节点类定义，val存储值，next指向下一个节点
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


# ===== 暴力解法 =====
# 思路: 遍历链表将值复制到数组，然后用双指针在数组上判断回文
# 复杂度: O(n) time, O(n) space
def solution_brute(head: Optional[ListNode]) -> bool:
    # WHY: 将链表转为数组，利用数组的随机访问特性判断回文
    values = []  # WHY: 存储链表所有节点的值
    current = head
    while current:
        values.append(current.val)  # WHY: 按顺序收集所有值
        current = current.next

    # WHY: 双指针从数组两端向中间移动，比较是否相等
    left, right = 0, len(values) - 1
    while left < right:
        if values[left] != values[right]:
            return False  # WHY: 发现不对称，不是回文
        left += 1
        right -= 1

    return True  # WHY: 所有元素对称，是回文


# ===== 最优解法 =====
# 思路: 三步走 — ①快慢指针找中点 ②反转后半部分 ③比较前后半部分
#       关键优化: 原地反转后半部分，无需额外空间
#       注意: 题目通常允许修改链表结构，如需还原可再反转一次
# 复杂度: O(n) time, O(1) space
def solution_optimal(head: Optional[ListNode]) -> bool:
    # WHY: 通过快慢指针找中点+反转后半部分，实现O(1)额外空间判断回文
    # WHY: 相比数组法，省去了O(n)的存储空间
    if not head or not head.next:
        return True  # WHY: 空链表或单节点链表视为回文

    # WHY: 第一步：快慢指针找到链表中点
    slow = fast = head
    while fast and fast.next:
        slow = slow.next       # WHY: 慢指针每次走一步
        fast = fast.next.next  # WHY: 快指针每次走两步
    # WHY: 此时slow指向中点（奇数个时指向正中间，偶数个时指向后半部分开头）

    # WHY: 第二步：反转后半部分链表
    prev = None
    current = slow
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    # WHY: prev现在指向反转后的后半部分的头

    # WHY: 第三步：比较前半部分和反转后的后半部分
    left, right = head, prev
    while right:  # WHY: 只遍历后半部分（后半部分可能更短或等长）
        if left.val != right.val:
            return False  # WHY: 值不相等，不是回文
        left = left.next
        right = right.next

    return True  # WHY: 所有对应节点值相等，是回文


# ===== 辅助函数 =====
def build_linked_list(values: list) -> Optional[ListNode]:
    # WHY: 根据值列表构建链表，用于测试
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Palindrome Linked List...")

    # 测试用例1: 偶数长度回文
    head1 = build_linked_list([1, 2, 2, 1])
    expected1 = True
    result1 = solution_optimal(head1)
    print(f"Test 1: {result1} == {expected1} -> {'PASS' if result1 == expected1 else 'FAIL'}")

    # 测试用例2: 非回文
    head2 = build_linked_list([1, 2, 3])
    expected2 = False
    result2 = solution_optimal(head2)
    print(f"Test 2: {result2} == {expected2} -> {'PASS' if result2 == expected2 else 'FAIL'}")

    # 测试用例3: 奇数长度回文
    head3 = build_linked_list([1, 2, 3, 2, 1])
    expected3 = True
    result3 = solution_optimal(head3)
    print(f"Test 3: {result3} == {expected3} -> {'PASS' if result3 == expected3 else 'FAIL'}")

    # 测试用例4: 单节点
    head4 = build_linked_list([1])
    expected4 = True
    result4 = solution_optimal(head4)
    print(f"Test 4: {result4} == {expected4} -> {'PASS' if result4 == expected4 else 'FAIL'}")

    # 测试用例5: 空链表
    result5 = solution_optimal(None)
    expected5 = True
    print(f"Test 5: {result5} == {expected5} -> {'PASS' if result5 == expected5 else 'FAIL'}")

    print("\nAll tests complete!")
