"""
LC 142. Linked List Cycle II (环形链表 II)
Difficulty: Medium
Tags: Hash Table, Linked List, Two Pointers
Link: https://leetcode.cn/problems/linked-list-cycle-ii/
Category: 07-linked-list
"""

from typing import Optional, Set


class ListNode:
    # WHY: 链表节点类定义，val存储值，next指向下一个节点
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


# ===== 暴力解法 =====
# 思路: 使用HashSet记录访问过的节点，第一个重复节点就是环的入口
# 复杂度: O(n) time, O(n) space
def solution_brute(head: Optional[ListNode]) -> Optional[ListNode]:
    # WHY: HashSet记录已访问节点，返回第一个重复节点
    visited: Set[ListNode] = set()
    current = head
    while current:
        if current in visited:
            # WHY: 当前节点已访问过，该节点即为环的入口
            return current
        visited.add(current)
        current = current.next
    return None  # WHY: 无环


# ===== 最优解法 =====
# 思路: Floyd判圈算法 + 数学推导
#       第一阶段: 快慢指针相遇（检测是否有环）
#       第二阶段: 将其中一个指针重置到头节点，两指针同速移动，相遇点即为环入口
#       数学原理: 设head到环入口距离为a，入口到相遇点距离为b，环剩余距离为c
#               慢指针走了 a+b，快指针走了 a+b+k(b+c)
#               由2(a+b) = a+b+k(b+c) 得 a = k(b+c)-b = (k-1)(b+c)+c
#               所以从头节点和相遇点同速移动，会在入口相遇
# 复杂度: O(n) time, O(1) space
def solution_optimal(head: Optional[ListNode]) -> Optional[ListNode]:
    # WHY: Floyd算法+数学推导，O(1)额外空间找到环入口
    # WHY: 相比HashSet法，省去了O(n)的集合空间
    if not head or not head.next:
        return None  # WHY: 少于两个节点不可能有环

    # WHY: 第一阶段：检测环，找到快慢指针的相遇点
    slow = fast = head
    has_cycle = False

    while fast and fast.next:
        slow = slow.next       # WHY: 慢指针每次走一步
        fast = fast.next.next  # WHY: 快指针每次走两步
        if slow is fast:
            has_cycle = True
            break  # WHY: 相遇，存在环

    if not has_cycle:
        return None  # WHY: 无环

    # WHY: 第二阶段：找环入口
    # WHY: 将slow重置到头节点，fast留在相遇点，两指针同速（每次一步）移动
    slow = head
    while slow is not fast:
        slow = slow.next  # WHY: 从头节点出发
        fast = fast.next  # WHY: 从相遇点出发
    # WHY: 相遇点即为环入口（数学推导保证）

    return slow


# ===== 辅助函数 =====
def build_linked_list(values: list, pos: int = -1) -> Optional[ListNode]:
    # WHY: 根据值列表构建链表，pos指定环的入口索引（-1表示无环）
    if not values:
        return None
    head = ListNode(values[0])
    nodes = [head]
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
        nodes.append(current)
    if 0 <= pos < len(nodes):
        current.next = nodes[pos]
    return head


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Linked List Cycle II...")

    # 测试用例1: 标准环（入口在索引1）
    head1 = build_linked_list([3, 2, 0, -4], pos=1)
    result1 = solution_optimal(head1)
    expected_val1 = 2  # WHY: 入口节点值为2（索引1）
    print(f"Test 1: entry val = {result1.val if result1 else None} == {expected_val1} -> {'PASS' if result1 and result1.val == expected_val1 else 'FAIL'}")

    # 测试用例2: 头节点就是环入口
    head2 = build_linked_list([1, 2], pos=0)
    result2 = solution_optimal(head2)
    expected_val2 = 1
    print(f"Test 2: entry val = {result2.val if result2 else None} == {expected_val2} -> {'PASS' if result2 and result2.val == expected_val2 else 'FAIL'}")

    # 测试用例3: 无环
    head3 = build_linked_list([1, 2, 3], pos=-1)
    result3 = solution_optimal(head3)
    print(f"Test 3: no cycle -> {'PASS' if result3 is None else 'FAIL'}")

    # 测试用例4: 单节点自环
    head4 = build_linked_list([1], pos=0)
    result4 = solution_optimal(head4)
    expected_val4 = 1
    print(f"Test 4: entry val = {result4.val if result4 else None} == {expected_val4} -> {'PASS' if result4 and result4.val == expected_val4 else 'FAIL'}")

    print("\nAll tests complete!")
