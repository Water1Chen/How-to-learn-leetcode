"""
LC 206. Reverse Linked List (反转链表)
Difficulty: Easy
Tags: Linked List, Recursion
Link: https://leetcode.cn/problems/reverse-linked-list/
Category: 07-linked-list
"""

from typing import Optional


class ListNode:
    # WHY: 链表节点类定义，val存储值，next指向下一个节点
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


# ===== 暴力解法 =====
# 思路: 遍历链表将值存入栈，然后重新构建反转后的链表
# 复杂度: O(n) time, O(n) space
def solution_brute(head: Optional[ListNode]) -> Optional[ListNode]:
    # WHY: 使用栈（后进先出）天然支持反转，但需要额外空间
    if not head:
        return None

    stack = []  # WHY: 栈用于存储所有节点的值
    current = head
    while current:
        stack.append(current.val)  # WHY: 按顺序入栈
        current = current.next

    # WHY: 从栈中弹出值构建反转链表（后进先出实现反转）
    new_head = ListNode(stack.pop())  # WHY: 弹出的第一个值是原链表的尾
    current = new_head
    while stack:
        current.next = ListNode(stack.pop())  # WHY: 依次弹出并创建新节点
        current = current.next

    return new_head


# ===== 最优解法 =====
# 思路: 迭代法（三指针）— 用prev、current、next三个指针原地反转指向
#       每次将当前节点的next指向前一个节点，三个指针同步前进
# 复杂度: O(n) time, O(1) space
def solution_optimal_iterative(head: Optional[ListNode]) -> Optional[ListNode]:
    # WHY: 三指针原地反转，无需额外空间
    # WHY: 相比栈方法，省去了O(n)的栈空间
    prev = None  # WHY: 前一个节点，初始为None（新链表的尾）
    current = head  # WHY: 当前正在处理的节点

    while current:
        next_temp = current.next  # WHY: 暂存下一个节点，防止断链
        current.next = prev       # WHY: 反转指向：当前节点指向前一个节点
        prev = current            # WHY: prev前进到当前节点
        current = next_temp       # WHY: current前进到下一个节点

    return prev  # WHY: prev指向原链表的最后一个节点，即新链表的头


# ===== 递归解法 =====
# 思路: 递归地反转子链表，然后将当前节点接到反转后的子链表末尾
#       递归的核心是"假设子链表已反转好，处理当前节点"
# 复杂度: O(n) time, O(n) space (递归栈空间)
def solution_optimal_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    # WHY: 递归解法代码简洁，但需要理解递归的"递"和"归"过程
    # WHY: 递归利用了函数调用栈天然保存状态，但也因此需要O(n)栈空间
    if not head or not head.next:
        # WHY: 基本情况：空链表或只有一个节点，直接返回
        return head

    # WHY: 递归反转head.next之后的子链表
    new_head = solution_optimal_recursive(head.next)

    # WHY: 此时head.next是新子链表的最后一个节点
    # WHY: 将head.next的next指向head，完成局部反转
    head.next.next = head
    # WHY: 将head的next置空（head成为新的尾节点）
    head.next = None

    return new_head


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
    print("Testing Reverse Linked List...")

    # 测试用例1: 标准链表
    head1 = build_linked_list([1, 2, 3, 4, 5])
    expected_str1 = "5 -> 4 -> 3 -> 2 -> 1"
    result1 = solution_optimal_iterative(head1)
    print(f"Test 1 (iterative): {print_linked_list(result1)} == {expected_str1} -> {'PASS' if print_linked_list(result1) == expected_str1 else 'FAIL'}")

    # 测试用例2: 两个节点
    head2 = build_linked_list([1, 2])
    expected_str2 = "2 -> 1"
    result2 = solution_optimal_iterative(head2)
    print(f"Test 2 (iterative): {print_linked_list(result2)} == {expected_str2} -> {'PASS' if print_linked_list(result2) == expected_str2 else 'FAIL'}")

    # 测试用例3: 递归版本测试
    head3 = build_linked_list([1, 2, 3, 4, 5])
    result3 = solution_optimal_recursive(head3)
    print(f"Test 3 (recursive): {print_linked_list(result3)} == {expected_str1} -> {'PASS' if print_linked_list(result3) == expected_str1 else 'FAIL'}")

    # 测试用例4: 空链表
    result4 = solution_optimal_iterative(None)
    print(f"Test 4 (empty): {'PASS' if result4 is None else 'FAIL'}")

    # 测试用例5: 单节点
    head5 = build_linked_list([42])
    result5 = solution_optimal_iterative(head5)
    print(f"Test 5 (single): {print_linked_list(result5)} == 42 -> {'PASS' if print_linked_list(result5) == '42' else 'FAIL'}")

    print("\nAll tests complete!")
