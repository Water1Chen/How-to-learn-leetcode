"""
LC 141. Linked List Cycle (环形链表)
Difficulty: Easy
Tags: Hash Table, Linked List, Two Pointers
Link: https://leetcode.cn/problems/linked-list-cycle/
Category: 07-linked-list
"""

from typing import Optional, Set


class ListNode:
    # WHY: 链表节点类定义，val存储值，next指向下一个节点
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


# ===== 暴力解法 =====
# 思路: 使用HashSet记录访问过的节点，遇到重复节点说明有环
# 复杂度: O(n) time, O(n) space
def solution_brute(head: Optional[ListNode]) -> bool:
    # WHY: HashSet记录已访问节点，空间换时间的经典做法
    visited: Set[ListNode] = set()  # WHY: 用集合存储节点引用
    current = head
    while current:
        if current in visited:
            # WHY: 当前节点已访问过，说明存在环
            return True
        visited.add(current)  # WHY: 标记当前节点为已访问
        current = current.next
    return False  # WHY: 遍历到末尾，无环


# ===== 最优解法 =====
# 思路: Floyd判圈算法（快慢指针）— 快指针每次走两步，慢指针每次走一步
#       如果有环，快指针最终会追上慢指针（在环内相遇）
#       如果无环，快指针会先到达末尾
# 复杂度: O(n) time, O(1) space
def solution_optimal(head: Optional[ListNode]) -> bool:
    # WHY: 快慢指针法，O(1)额外空间检测环
    # WHY: 相比HashSet法，省去了O(n)的集合空间
    if not head or not head.next:
        return False  # WHY: 少于两个节点不可能有环

    slow = head   # WHY: 慢指针，每次走一步
    fast = head   # WHY: 快指针，每次走两步

    while fast and fast.next:
        slow = slow.next       # WHY: 慢指针前进一步
        fast = fast.next.next  # WHY: 快指针前进两步
        if slow is fast:
            # WHY: 快慢指针相遇，说明有环
            # WHY: 在环内，快指针每次比慢指针多走一步，最终会追上
            return True

    return False  # WHY: 快指针到达末尾，无环


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
    # WHY: 如果pos >= 0，将尾节点连接到pos位置的节点形成环
    if 0 <= pos < len(nodes):
        current.next = nodes[pos]
    return head


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Linked List Cycle...")

    # 测试用例1: 有环
    head1 = build_linked_list([3, 2, 0, -4], pos=1)  # WHY: 尾节点连接到索引1
    expected1 = True
    result1 = solution_optimal(head1)
    print(f"Test 1: {result1} == {expected1} -> {'PASS' if result1 == expected1 else 'FAIL'}")

    # 测试用例2: 无环
    head2 = build_linked_list([1, 2], pos=-1)
    expected2 = False
    result2 = solution_optimal(head2)
    print(f"Test 2: {result2} == {expected2} -> {'PASS' if result2 == expected2 else 'FAIL'}")

    # 测试用例3: 单节点无环
    head3 = build_linked_list([1], pos=-1)
    expected3 = False
    result3 = solution_optimal(head3)
    print(f"Test 3: {result3} == {expected3} -> {'PASS' if result3 == expected3 else 'FAIL'}")

    # 测试用例4: 单节点自环
    head4 = build_linked_list([1], pos=0)
    expected4 = True
    result4 = solution_optimal(head4)
    print(f"Test 4: {result4} == {expected4} -> {'PASS' if result4 == expected4 else 'FAIL'}")

    print("\nAll tests complete!")
