"""
LC 25. K 个一组翻转链表 (Reverse Nodes in k-Group)
Difficulty: Hard
Tags: Linked List, Recursion
Link: https://leetcode.cn/problems/reverse-nodes-in-k-group/
Category: 07-linked-list
"""


class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val = val
        self.next = next


# ===== 暴力解法 =====
# 思路: 遍历链表将值收集到数组中，按 k 分段反转数组，再写回链表。
#       完全依赖数组操作来规避指针操作的复杂性。
# 复杂度: O(n) time, O(n) space
def solution_brute(head: ListNode | None, k: int) -> ListNode | None:
    # WHY: 将链表转为数组，利用 Python 列表的分片操作简化反转逻辑
    values: list[int] = []
    cur = head
    while cur:
        values.append(cur.val)
        cur = cur.next

    # WHY: 按 k 个一组遍历数组，不足 k 个的剩余部分保持不动
    n = len(values)
    i = 0
    while i + k <= n:
        # WHY: 反转当前组 [i, i+k) 的元素，注意是原地反转
        left, right = i, i + k - 1
        while left < right:
            values[left], values[right] = values[right], values[left]
            left += 1
            right -= 1
        i += k

    # WHY: 将反转后的值写回链表，复用原始节点减少内存分配
    cur = head
    for v in values:
        cur.val = v  # type: ignore[union-attr]
        cur = cur.next  # type: ignore[union-attr]
    return head


# ===== 最优解法 (Recursive Reverse + Recurse) =====
# 思路: 先检查剩余节点是否够 k 个，够则反转这 k 个节点，然后递归处理
#       剩余部分并连接。反转操作使用经典的迭代三指针法。
# 复杂度: O(n) time, O(n/k) recursion stack ≈ O(n) space worst
def solution_optimal(head: ListNode | None, k: int) -> ListNode | None:
    # WHY: 辅助函数：反转从 head 开始的 k 个节点，返回新的头节点
    def reverse_k(node: ListNode | None, k: int) -> ListNode | None:
        # WHY: 三指针迭代反转：prev 指向已反转部分，cur 是当前处理节点
        prev: ListNode | None = None
        cur = node
        # WHY: 只反转 k 个节点，不处理后续部分
        for _ in range(k):
            # WHY: 保存下一个节点防止断链后丢失引用
            next_node = cur.next  # type: ignore[union-attr]
            # WHY: 核心操作：当前节点的 next 指向前一个节点，实现反转
            cur.next = prev  # type: ignore[union-attr]
            # WHY: prev 和 cur 同步前进一个位置
            prev = cur
            cur = next_node
        # WHY: prev 成为反转后 k 个节点中的新头节点
        return prev

    # WHY: 统计从 head 开始的节点数，判断是否达到 k 个
    count = 0
    cur = head
    while cur and count < k:
        cur = cur.next
        count += 1

    # WHY: 如果剩余节点数 >= k，执行反转；否则直接返回 (不足 k 不反转)
    if count == k:
        # WHY: 反转前 k 个节点：new_head 是这 k 个节点中原来的第 k 个
        new_head = reverse_k(head, k)
        # WHY: 反转后 head.next 指向的是剩余链表的头部
        # WHY: 递归处理剩余部分并接在当前 k 组的末尾 (head 现在是尾节点)
        head.next = solution_optimal(cur, k)  # type: ignore[union-attr]
        # WHY: 返回新的头节点给上一层
        return new_head

    # WHY: 不足 k 个节点，不需要反转，直接返回原来的头节点
    return head


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
    print("Testing Reverse Nodes in k-Group...")

    # Test 1: 1->2->3->4->5, k=2 -> 2->1->4->3->5
    head1 = array_to_list([1, 2, 3, 4, 5])
    result1 = solution_optimal(head1, 2)
    assert list_to_array(result1) == [2, 1, 4, 3, 5], "Test 1 failed!"

    # Test 2: 1->2->3->4->5, k=3 -> 3->2->1->4->5
    head2 = array_to_list([1, 2, 3, 4, 5])
    result2 = solution_optimal(head2, 3)
    assert list_to_array(result2) == [3, 2, 1, 4, 5], "Test 2 failed!"

    # Test 3: 空链表
    head3 = array_to_list([])
    result3 = solution_optimal(head3, 2)
    assert list_to_array(result3) == [], "Test 3 failed!"

    # Test 4: k=1 相当于不反转
    head4 = array_to_list([1, 2, 3])
    result4 = solution_optimal(head4, 1)
    assert list_to_array(result4) == [1, 2, 3], "Test 4 failed!"

    print("All tests passed!")
