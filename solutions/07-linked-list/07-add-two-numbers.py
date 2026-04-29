"""
LC 2. Add Two Numbers (两数相加)
Difficulty: Medium
Tags: Linked List, Math, Recursion
Link: https://leetcode.cn/problems/add-two-numbers/
Category: 07-linked-list
"""

from typing import Optional


class ListNode:
    # WHY: 链表节点类定义，val存储值，next指向下一个节点
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


# ===== 暴力解法 =====
# 思路: 将两个链表分别转换为整数，相加后再将结果转换为链表
#       注意: 该方法在链表很长时会溢出（Python虽然支持大整数，但违反了题目本意）
# 复杂度: O(m + n) time, O(max(m, n)) space
def solution_brute(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # WHY: 将链表转为整数再相加，思路直观但存在溢出风险（题目要求不准这样做）
    num1 = 0
    current = l1
    multiplier = 1  # WHY: 当前位权重（个位为1，十位为10...）
    while current:
        num1 += current.val * multiplier
        multiplier *= 10
        current = current.next

    num2 = 0
    current = l2
    multiplier = 1
    while current:
        num2 += current.val * multiplier
        multiplier *= 10
        current = current.next

    total = num1 + num2
    if total == 0:
        return ListNode(0)

    # WHY: 将整数反转并构建链表（注意链表是逆序存储）
    dummy = ListNode(0)
    current = dummy
    while total > 0:
        current.next = ListNode(total % 10)  # WHY: 取最低位
        total //= 10
        current = current.next

    return dummy.next


# ===== 最优解法 =====
# 思路: 模拟竖式加法 — 从最低位（链表头部）开始逐位相加，处理进位
#       两个指针分别遍历两个链表，同时维护进位标志
#       关键点: 按位相加，进位传递到下一位
# 复杂度: O(max(m, n)) time, O(max(m, n)) space
def solution_optimal(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # WHY: 模拟竖式加法逐位计算，避免了整数溢出问题
    # WHY: 相比转换整数法，不依赖语言的大整数特性，更符合题目本意
    dummy = ListNode(0)  # WHY: 虚拟头节点简化边界处理
    current = dummy      # WHY: 结果链表的当前尾节点
    carry = 0            # WHY: 进位值，初始为0

    p1, p2 = l1, l2

    # WHY: 只要还有节点未处理或有进位，继续循环
    while p1 or p2 or carry:
        # WHY: 获取当前位的值（如果链表已走完则视为0）
        val1 = p1.val if p1 else 0
        val2 = p2.val if p2 else 0

        # WHY: 计算当前位的和及进位
        total = val1 + val2 + carry
        carry = total // 10   # WHY: 进位给下一位
        current_digit = total % 10  # WHY: 当前位的值

        # WHY: 创建当前位的节点并连接
        current.next = ListNode(current_digit)
        current = current.next

        # WHY: 指针前进（如果还有节点的话）
        if p1:
            p1 = p1.next
        if p2:
            p2 = p2.next

    return dummy.next


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


def print_linked_list(head: Optional[ListNode]) -> str:
    # WHY: 将链表转换为易读的字符串表示，用于测试输出
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    return " -> ".join(values) if values else "None"


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Add Two Numbers...")

    # 测试用例1: 标准情况 342 + 465 = 807
    # l1 = [2,4,3] 表示 342
    # l2 = [5,6,4] 表示 465
    # 结果 = [7,0,8] 表示 807
    l1 = build_linked_list([2, 4, 3])
    l2 = build_linked_list([5, 6, 4])
    expected_str1 = "7 -> 0 -> 8"
    result1 = solution_optimal(l1, l2)
    print(f"Test 1: {print_linked_list(result1)} == {expected_str1} -> {'PASS' if print_linked_list(result1) == expected_str1 else 'FAIL'}")

    # 测试用例2: 0 + 0 = 0
    l3 = build_linked_list([0])
    l4 = build_linked_list([0])
    expected_str2 = "0"
    result2 = solution_optimal(l3, l4)
    print(f"Test 2: {print_linked_list(result2)} == {expected_str2} -> {'PASS' if print_linked_list(result2) == expected_str2 else 'FAIL'}")

    # 测试用例3: 不同长度 99 + 1 = 100
    # l1 = [9,9] 表示 99
    # l2 = [1] 表示 1
    # 结果 = [0,0,1] 表示 100
    l5 = build_linked_list([9, 9])
    l6 = build_linked_list([1])
    expected_str3 = "0 -> 0 -> 1"
    result3 = solution_optimal(l5, l6)
    print(f"Test 3: {print_linked_list(result3)} == {expected_str3} -> {'PASS' if print_linked_list(result3) == expected_str3 else 'FAIL'}")

    # 测试用例4: 产生多个进位 999 + 1 = 1000
    l7 = build_linked_list([9, 9, 9])
    l8 = build_linked_list([1])
    expected_str4 = "0 -> 0 -> 0 -> 1"
    result4 = solution_optimal(l7, l8)
    print(f"Test 4: {print_linked_list(result4)} == {expected_str4} -> {'PASS' if print_linked_list(result4) == expected_str4 else 'FAIL'}")

    print("\nAll tests complete!")
