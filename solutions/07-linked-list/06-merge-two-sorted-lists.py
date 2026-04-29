"""
LC 21. Merge Two Sorted Lists (合并两个有序链表)
Difficulty: Easy
Tags: Linked List, Recursion
Link: https://leetcode.cn/problems/merge-two-sorted-lists/
Category: 07-linked-list
"""

from typing import Optional, List


class ListNode:
    # WHY: 链表节点类定义，val存储值，next指向下一个节点
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


# ===== 暴力解法 =====
# 思路: 将两个链表的所有值收集到数组，排序后重建新链表
# 复杂度: O(n log n) time (排序), O(n) space
def solution_brute(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # WHY: 收集所有值到数组，利用排序简化合并逻辑
    values: List[int] = []

    # WHY: 遍历第一个链表收集值
    current = list1
    while current:
        values.append(current.val)
        current = current.next

    # WHY: 遍历第二个链表收集值
    current = list2
    while current:
        values.append(current.val)
        current = current.next

    if not values:
        return None  # WHY: 两个链表都为空

    values.sort()  # WHY: 排序后重建链表，O(n log n)

    # WHY: 根据排序后的值重建链表
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


# ===== 最优解法 =====
# 思路: 双指针法（迭代）— 使用虚拟头节点，两个指针分别遍历两个链表
#       每次取较小值接到结果链表末尾，直到其中一个链表遍历完，再将剩余部分接上
# 复杂度: O(n) time, O(1) space
def solution_optimal_iterative(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # WHY: 双指针合并利用链表已排序的性质，一次遍历完成
    # WHY: 相比数组+排序法，避免了排序开销O(n log n)和额外数组空间O(n)
    dummy = ListNode(0)  # WHY: 虚拟头节点简化边界处理，无需单独处理第一个节点
    current = dummy      # WHY: current指向结果链表的尾节点

    p1, p2 = list1, list2  # WHY: 两个指针分别遍历两个链表

    while p1 and p2:
        if p1.val <= p2.val:
            # WHY: 选较小的节点（p1），接到结果链表末尾
            current.next = p1
            p1 = p1.next  # WHY: p1指针前进
        else:
            current.next = p2
            p2 = p2.next
        current = current.next  # WHY: current指针前进到新的尾节点

    # WHY: 将剩余部分（至少一个链表已遍历完）接到结果末尾
    # WHY: 剩余部分本身就是有序的，直接连接即可
    current.next = p1 if p1 else p2

    return dummy.next  # WHY: 跳过虚拟头节点，返回真正的头


# ===== 递归解法 =====
# 思路: 递归比较两个链表的头节点，较小者指向剩余部分的合并结果
# 复杂度: O(n) time, O(n) space (递归栈空间)
def solution_optimal_recursive(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # WHY: 递归解法代码简洁优雅，利用函数调用栈自动管理状态
    if not list1:
        return list2  # WHY: 链表1为空，直接返回链表2（剩余部分都是链表2的）
    if not list2:
        return list1  # WHY: 同理

    # WHY: 比较两个头节点，选择较小的作为结果的头
    if list1.val <= list2.val:
        # WHY: list1更小，它作为当前头，其next指向剩余部分的合并结果
        list1.next = solution_optimal_recursive(list1.next, list2)
        return list1
    else:
        list2.next = solution_optimal_recursive(list1, list2.next)
        return list2


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
    print("Testing Merge Two Sorted Lists...")

    # 测试用例1: 两个非空等长链表
    list1 = build_linked_list([1, 2, 4])
    list2 = build_linked_list([1, 3, 4])
    expected_str1 = "1 -> 1 -> 2 -> 3 -> 4 -> 4"
    result1 = solution_optimal_iterative(list1, list2)
    print(f"Test 1 (iterative): {print_linked_list(result1)} == {expected_str1} -> {'PASS' if print_linked_list(result1) == expected_str1 else 'FAIL'}")

    # 测试用例2: 一个为空
    list3 = build_linked_list([])
    list4 = build_linked_list([0])
    expected_str2 = "0"
    result2 = solution_optimal_iterative(list3, list4)
    print(f"Test 2: {print_linked_list(result2)} == {expected_str2} -> {'PASS' if print_linked_list(result2) == expected_str2 else 'FAIL'}")

    # 测试用例3: 递归版本测试
    list5 = build_linked_list([1, 2, 4])
    list6 = build_linked_list([1, 3, 4])
    result3 = solution_optimal_recursive(list5, list6)
    print(f"Test 3 (recursive): {print_linked_list(result3)} == {expected_str1} -> {'PASS' if print_linked_list(result3) == expected_str1 else 'FAIL'}")

    # 测试用例4: 两个都为空
    result4 = solution_optimal_iterative(None, None)
    print(f"Test 4: both empty -> {'PASS' if result4 is None else 'FAIL'}")

    # 测试用例5: 长度不同
    list7 = build_linked_list([1, 5])
    list8 = build_linked_list([2, 3, 4, 6])
    expected_str5 = "1 -> 2 -> 3 -> 4 -> 5 -> 6"
    result5 = solution_optimal_iterative(list7, list8)
    print(f"Test 5: {print_linked_list(result5)} == {expected_str5} -> {'PASS' if print_linked_list(result5) == expected_str5 else 'FAIL'}")

    print("\nAll tests complete!")
