"""
LC 24. 两两交换链表中的节点 (Swap Nodes in Pairs)
Difficulty: Medium
Tags: Linked List, Recursion
Link: https://leetcode.cn/problems/swap-nodes-in-pairs/
Category: 07-linked-list
"""


class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val = val
        self.next = next


# ===== 暴力解法 =====
# 思路: 遍历链表收集所有节点的值到数组中，然后按两两交换规则重新赋值，
#       不修改节点间的连接关系。虽然结果正确，但浪费了指针操作的优势。
# 复杂度: O(n) time, O(n) space
def solution_brute(head: ListNode | None) -> ListNode | None:
    # WHY: 收集所有节点值以便在数组层面执行交换，避免直接操作指针
    values: list[int] = []
    cur = head
    while cur:
        # WHY: 顺序很重要，要保持原始顺序以便后续按索引配对交换
        values.append(cur.val)
        cur = cur.next

    # WHY: 按步长为2遍历数组，交换每一对相邻元素
    i = 0
    while i + 1 < len(values):
        # WHY: 交换 i 和 i+1 位置的值，模拟节点配对翻转
        values[i], values[i + 1] = values[i + 1], values[i]
        i += 2

    # WHY: 将交换后的值重新写回链表节点，复用原有节点结构
    cur = head
    for v in values:
        cur.val = v  # type: ignore[union-attr]
        cur = cur.next  # type: ignore[union-attr]
    # WHY: 链表结构未变，head 指针依然有效
    return head


# ===== 最优解法 (Iterative Swap) =====
# 思路: 使用 prev 指针追踪已处理部分的末尾，每次取出两个节点交换位置，
#       然后将 prev 连接到交换后的节点上。一趟扫描完成。
# 复杂度: O(n) time, O(1) space
def solution_optimal(head: ListNode | None) -> ListNode | None:
    # WHY: 哨兵节点简化了头节点变更的逻辑，prev 始终指向已处理段的末尾
    dummy = ListNode(0, head)
    prev = dummy

    # WHY: 每次处理两个节点，确保两者都不为空才进行交换
    while prev.next and prev.next.next:
        # WHY: 标识出本次要交换的两个节点
        first = prev.next
        second = prev.next.next

        # WHY: 执行三步骤指针重连: prev->second, second->first, first->next
        # WHY: 第一步: prev 跳过 first 直接指向 second
        prev.next = second
        # WHY: 第二步: first 指向 second 后面的节点 (保存剩余链表)
        first.next = second.next
        # WHY: 第三步: second 的 next 指向 first，完成交换
        second.next = first

        # WHY: 移动 prev 到已处理段的末尾 (即 first)，准备下一轮
        prev = first

    # WHY: 哨兵的下一个节点始终是新链表的头
    return dummy.next


# ===== 辅助函数 =====
def list_to_array(head: ListNode | None) -> list[int]:
    # WHY: 方便在测试中直观对比结果
    result: list[int] = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def array_to_list(arr: list[int]) -> ListNode | None:
    # WHY: 从测试数据快速构建链表
    if not arr:
        return None
    dummy = ListNode(0)
    cur = dummy
    for v in arr:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Swap Nodes in Pairs...")

    # Test 1: 偶数个节点 1->2->3->4 -> 2->1->4->3
    head1 = array_to_list([1, 2, 3, 4])
    result1 = solution_optimal(head1)
    assert list_to_array(result1) == [2, 1, 4, 3], "Test 1 failed!"

    # Test 2: 奇数个节点 1->2->3 -> 2->1->3 (最后一个节点不动)
    head2 = array_to_list([1, 2, 3])
    result2 = solution_optimal(head2)
    assert list_to_array(result2) == [2, 1, 3], "Test 2 failed!"

    # Test 3: 空链表
    head3 = array_to_list([])
    result3 = solution_optimal(head3)
    assert list_to_array(result3) == [], "Test 3 failed!"

    # Test 4: 两个节点 1->2 -> 2->1
    head4 = array_to_list([1, 2])
    result4 = solution_optimal(head4)
    assert list_to_array(result4) == [2, 1], "Test 4 failed!"

    print("All tests passed!")
