"""
LC 148. 排序链表 (Sort List)
Difficulty: Medium
Tags: Linked List, Two Pointers, Divide and Conquer, Sorting, Merge Sort
Link: https://leetcode.cn/problems/sort-list/
Category: 07-linked-list
"""


class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val = val
        self.next = next


# ===== 暴力解法 =====
# 思路: 遍历链表收集所有节点值到数组中，调用内置排序，再按顺序
#       将排序后的值写回到链表节点中。利用了 Python 的 Timsort。
# 复杂度: O(n log n) time, O(n) space
def solution_brute(head: ListNode | None) -> ListNode | None:
    if not head:
        return None

    # WHY: 将链表值收集到数组中以便使用 Python 内置的 Timsort 排序
    values: list[int] = []
    cur = head
    while cur:
        values.append(cur.val)
        cur = cur.next

    # WHY: Python 的 sort() 是稳定的 Timsort，O(n log n) 时间复杂度
    values.sort()

    # WHY: 将排序后的值写回链表，复用原有节点节省内存分配
    cur = head
    for v in values:
        cur.val = v
        cur = cur.next  # type: ignore[assignment]

    return head


# ===== 最优解法 (Merge Sort Top-Down) =====
# 思路: 用快慢指针找到链表的中点，递归地对左右两半排序，然后合并两个
#       有序链表。归并排序保证 O(n log n)，适合链表的顺序访问特性。
# 复杂度: O(n log n) time, O(log n) recursion stack space
def solution_optimal(head: ListNode | None) -> ListNode | None:
    # WHY: 辅助函数：合并两个有序链表（标准双指针归并）
    def merge(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        # WHY: 哨兵节点简化合并过程中的指针操作
        dummy = ListNode(0)
        cur = dummy
        # WHY: 同时遍历两个链表，每次取较小的节点
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        # WHY: 将剩余部分直接接上（最多只有一个链表还有剩余节点）
        cur.next = l1 if l1 else l2
        return dummy.next

    # WHY: 递归终止条件：空链表或只有一个节点时直接返回
    if not head or not head.next:
        return head

    # WHY: 使用快慢指针找到链表中点（快指针走两步，慢指针走一步）
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # WHY: 从中点处切分链表：mid_next 是右半部分的头节点
    mid_next = slow.next
    # WHY: 切断左半部分和右半部分的连接
    slow.next = None

    # WHY: 递归排序左右两半
    left = solution_optimal(head)
    right = solution_optimal(mid_next)

    # WHY: 合并两个有序链表
    return merge(left, right)


# ===== 辅助函数 =====
def list_to_array(head: ListNode | None) -> list[int]:
    result: list[int] = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def array_to_list(arr: list[int]) -> ListNode | None:
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
    print("Testing Sort List...")

    # Test 1: 标准乱序 4->2->1->3 -> 1->2->3->4
    head1 = array_to_list([4, 2, 1, 3])
    result1 = solution_optimal(head1)
    assert list_to_array(result1) == [1, 2, 3, 4], "Test 1 failed!"

    # Test 2: 已经有序 -1->5->3->4->0 -> -1->0->3->4->5
    head2 = array_to_list([-1, 5, 3, 4, 0])
    result2 = solution_optimal(head2)
    assert list_to_array(result2) == [-1, 0, 3, 4, 5], "Test 2 failed!"

    # Test 3: 空链表
    head3 = array_to_list([])
    result3 = solution_optimal(head3)
    assert list_to_array(result3) == [], "Test 3 failed!"

    # Test 4: 只有一个节点
    head4 = array_to_list([1])
    result4 = solution_optimal(head4)
    assert list_to_array(result4) == [1], "Test 4 failed!"

    print("All tests passed!")
