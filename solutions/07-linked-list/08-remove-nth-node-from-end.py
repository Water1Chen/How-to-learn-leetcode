"""
LC 19. 删除链表的倒数第 N 个结点 (Remove Nth Node From End of List)
Difficulty: Medium
Tags: Linked List, Two Pointers
Link: https://leetcode.cn/problems/remove-nth-node-from-end-of-list/
Category: 07-linked-list
"""


class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val = val
        self.next = next


# ===== 暴力解法 (Two Pass) =====
# 思路: 先遍历一次计算链表总长度 L, 再遍历一次删除第 L-n 个节点。
#       需要处理删除头节点的特殊情况。
# 复杂度: O(n) time, O(1) space
def solution_brute(head: ListNode | None, n: int) -> ListNode | None:
    # WHY: 使用哨兵节点统一处理删除头节点的边界情况，避免单独写 if 分支
    dummy = ListNode(0, head)
    # WHY: 第一次遍历只为了统计链表长度，这是两趟算法的本质限制
    length = 0
    cur = head
    while cur:
        # WHY: 每经过一个节点计数器加1，最终得到总节点数
        length += 1
        cur = cur.next

    # WHY: 找到待删除节点的前驱节点，方便执行删除操作
    cur = dummy
    # WHY: 要跳过的步数是 L-n，走完后 cur 指向待删节点的前驱
    for _ in range(length - n):
        cur = cur.next

    # WHY: 将前驱节点的 next 指向待删节点的后继，从而跳过待删节点
    cur.next = cur.next.next  # type: ignore[union-attr]
    # WHY: 返回 dummy.next 而非 head，防止 head 被删除的情况
    return dummy.next


# ===== 最优解法 (Fast/Slow One Pass) =====
# 思路: 快指针先走 n 步，然后快慢指针同步前进。当快指针到达末尾时，
#       慢指针恰好指向倒数第 n 个节点的前驱。一趟遍历完成删除。
# 复杂度: O(n) time, O(1) space
def solution_optimal(head: ListNode | None, n: int) -> ListNode | None:
    # WHY: 哨兵节点消除了对"删除头节点"这个特殊情况的判断代码
    dummy = ListNode(0, head)
    # WHY: 快慢指针都从 dummy 出发，保证慢指针最终指向待删节点的前驱
    fast = dummy
    slow = dummy

    # WHY: 快指针先走 n 步，制造一个宽度为 n 的滑动窗口
    for _ in range(n):
        # WHY: 题目保证 n 有效，所以 fast 不会变成 None
        fast = fast.next  # type: ignore[union-attr]

    # WHY: 快慢指针同步前进，当快指针到末尾时，慢指针正好在目标前驱
    while fast.next:
        fast = fast.next
        slow = slow.next

    # WHY: 跳过目标节点，Python 垃圾回收会自动处理悬空的节点
    slow.next = slow.next.next  # type: ignore[union-attr]
    # WHY: 返回哨兵的下一个节点，应对头节点被删除的场景
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
    print("Testing Remove Nth Node From End of List...")

    # Test 1: 标准场景 1->2->3->4->5, n=2 -> 1->2->3->5
    head1 = array_to_list([1, 2, 3, 4, 5])
    result1 = solution_optimal(head1, 2)
    assert list_to_array(result1) == [1, 2, 3, 5], "Test 1 failed!"

    # Test 2: 删除头节点, n=5 -> []
    head2 = array_to_list([1, 2, 3, 4, 5])
    result2 = solution_optimal(head2, 5)
    assert list_to_array(result2) == [2, 3, 4, 5], "Test 2 failed!"

    # Test 3: 只有一个节点, n=1 -> []
    head3 = array_to_list([1])
    result3 = solution_optimal(head3, 1)
    assert list_to_array(result3) == [], "Test 3 failed!"

    # Test 4: 删除最后一个节点, n=1
    head4 = array_to_list([1, 2, 3])
    result4 = solution_optimal(head4, 1)
    assert list_to_array(result4) == [1, 2], "Test 4 failed!"

    print("All tests passed!")
