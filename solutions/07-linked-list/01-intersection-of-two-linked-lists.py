"""
LC 160. Intersection of Two Linked Lists (相交链表)
Difficulty: Easy
Tags: Hash Table, Linked List, Two Pointers
Link: https://leetcode.cn/problems/intersection-of-two-linked-lists/
Category: 07-linked-list
"""

from typing import Optional, Set


class ListNode:
    # WHY: 链表节点类定义，val存储值，next指向下一个节点
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


# ===== 暴力解法 =====
# 思路: 遍历链表A，将所有节点存入HashSet；再遍历链表B，第一个在HashSet中存在的节点即为交点
# 复杂度: O(m + n) time, O(m) space
def solution_brute(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    # WHY: 使用HashSet记录链表A的所有节点，空间换时间
    visited: Set[ListNode] = set()  # WHY: 用集合存储节点引用，O(1)查找

    # WHY: 遍历链表A，将所有节点加入集合
    current = headA
    while current:
        visited.add(current)  # WHY: 记录节点引用（Python中对象引用可哈希）
        current = current.next

    # WHY: 遍历链表B，第一个在集合中出现的节点就是交点
    current = headB
    while current:
        if current in visited:  # WHY: O(1)时间判断是否存在
            return current
        current = current.next

    return None  # WHY: 没有交点


# ===== 最优解法 =====
# 思路: 双指针法 — 指针pA从headA开始，pB从headB开始
#       当pA到达末尾时重定向到headB，当pB到达末尾时重定向到headA
#       如果相交，两个指针会在交点相遇；如果不相交，会同时到达null
#       数学原理: 两指针走过的路径长度相同（都走了A+B的长度）
# 复杂度: O(m + n) time, O(1) space
def solution_optimal(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    # WHY: 双指针法消除长度差，无需额外空间
    # WHY: 相比HashSet法，省去了O(m)的集合空间
    if not headA or not headB:
        return None

    pA, pB = headA, headB

    # WHY: 两指针同时移动，当一方到达末尾时转向另一链表头部
    # WHY: 这样两指针走过的总路程相等，确保在交点相遇
    while pA is not pB:
        # WHY: pA走到末尾则转向headB，否则继续前进
        pA = pA.next if pA else headB
        # WHY: pB走到末尾则转向headA，否则继续前进
        pB = pB.next if pB else headA

    # WHY: 相遇时要么在交点，要么都是None（无交点）
    return pA


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
    print("Testing Intersection of Two Linked Lists...")

    # 测试用例1: 相交链表
    # A: 1 -> 2 -> 3 -> 4 -> 5
    #               ^
    # B:       9 ---+
    common = ListNode(3, ListNode(4, ListNode(5)))
    headA = ListNode(1, ListNode(2, common))
    headB = ListNode(9, common)
    result1 = solution_optimal(headA, headB)
    expected1 = common
    print(f"Test 1: intersection node val = {result1.val if result1 else None} == 3 -> {'PASS' if result1 == expected1 else 'FAIL'}")

    # 测试用例2: 不相交
    headA2 = build_linked_list([1, 2, 3])
    headB2 = build_linked_list([4, 5, 6])
    result2 = solution_optimal(headA2, headB2)
    print(f"Test 2: no intersection -> {'PASS' if result2 is None else 'FAIL'}")

    # 测试用例3: 一个链表为空
    result3 = solution_optimal(None, build_linked_list([1]))  # type: ignore
    print(f"Test 3: one empty -> {'PASS' if result3 is None else 'FAIL'}")

    print("\nAll tests complete!")
