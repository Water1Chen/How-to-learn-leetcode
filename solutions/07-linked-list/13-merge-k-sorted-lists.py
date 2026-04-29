"""
LC 23. 合并 K 个升序链表 (Merge k Sorted Lists)
Difficulty: Hard
Tags: Linked List, Heap (Priority Queue), Divide and Conquer, Merge Sort
Link: https://leetcode.cn/problems/merge-k-sorted-lists/
Category: 07-linked-list
"""

import heapq


class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val = val
        self.next = next


# ===== 暴力解法 =====
# 思路: 遍历所有链表收集值到数组，整体排序，再构建新链表。
#       没有利用"每个链表已排序"这个条件。
# 复杂度: O(N log N) time, O(N) space, 其中 N 是所有节点总数
def solution_brute(lists: list[ListNode | None]) -> ListNode | None:
    # WHY: 收集所有节点的值到一个数组中，完全忽略各链表内部的顺序信息
    values: list[int] = []
    for head in lists:
        cur = head
        while cur:
            values.append(cur.val)
            cur = cur.next

    if not values:
        return None

    # WHY: 整体排序，利用了 Python 的 Timsort，但丢弃了已排序链表的局部有序性
    values.sort()

    # WHY: 用排序后的值构建一个新的链表返回
    dummy = ListNode(0)
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


# ===== 方法一：最小堆 =====
# 思路: 将每个链表的头节点放入最小堆，每次弹出最小值节点，
#       然后将该节点的 next 入堆。利用堆维护 k 个候选头中的最小值。
# 复杂度: O(N log k) time, O(k) space (堆的大小)
def solution_min_heap(lists: list[ListNode | None]) -> ListNode | None:
    # WHY: 自定义堆元素格式：(val, index, node)，index 用于打破值相等时的比较
    # WHY: ListNode 不支持比较，所以不能直接存 node 到堆中
    heap: list[tuple[int, int, ListNode]] = []

    # WHY: 将每个非空链表的头节点入堆
    for i, node in enumerate(lists):
        if node:
            # WHY: 使用 (val, i, node) 三元组，i 确保 val 相同时不会比较 ListNode
            heapq.heappush(heap, (node.val, i, node))

    dummy = ListNode(0)
    cur = dummy

    # WHY: 不断从堆中弹出最小值节点，将其接到结果链表末尾
    while heap:
        # WHY: 弹出最小值的节点
        _, i, node = heapq.heappop(heap)
        cur.next = node
        cur = cur.next

        # WHY: 如果弹出的节点还有下一个节点，将其入堆继续参与比较
        if node.next:
            # WHY: 仍然使用相同的索引 i 来保持唯一性
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next


# ===== 方法二：分治归并 =====
# 思路: 两两合并链表，每轮合并后链表数量减半，直到只剩一个链表。
#       利用了合并两个有序链表的归并操作。
# 复杂度: O(N log k) time, O(1) extra space (不计算递归栈)
def solution_divide_conquer(lists: list[ListNode | None]) -> ListNode | None:
    if not lists:
        return None

    # WHY: 辅助函数：合并两个有序链表
    def merge_two(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy.next

    # WHY: 从单一链表开始，每轮将相邻两两合并
    # WHY: 每轮后链表数量减半，只需要 O(log k) 轮
    step = 1
    while step < len(lists):
        # WHY: 每步跨越 2*step 的距离，将 i 和 i+step 合并
        for i in range(0, len(lists) - step, 2 * step):
            lists[i] = merge_two(lists[i], lists[i + step])
        step *= 2

    # WHY: lists[0] 就是最终合并后的完整链表
    return lists[0]


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


def test_solution(solution_fn) -> None:
    """对单个解法函数运行测试"""
    # Test 1: [[1,4,5],[1,3,4],[2,6]] -> [1,1,2,3,4,4,5,6]
    lists1 = [array_to_list([1, 4, 5]), array_to_list([1, 3, 4]), array_to_list([2, 6])]
    result1 = solution_fn(lists1)
    assert list_to_array(result1) == [1, 1, 2, 3, 4, 4, 5, 6], \
        f"{solution_fn.__name__} Test 1 failed!"

    # Test 2: 空列表 -> []
    result2 = solution_fn([])
    assert list_to_array(result2) == [], f"{solution_fn.__name__} Test 2 failed!"

    # Test 3: 包含空链表的列表
    lists3 = [array_to_list([]), array_to_list([1]), array_to_list([2])]
    result3 = solution_fn(lists3)
    assert list_to_array(result3) == [1, 2], f"{solution_fn.__name__} Test 3 failed!"

    # Test 4: 单个链表
    lists4 = [array_to_list([1, 2, 3])]
    result4 = solution_fn(lists4)
    assert list_to_array(result4) == [1, 2, 3], f"{solution_fn.__name__} Test 4 failed!"


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Merge k Sorted Lists...")
    test_solution(solution_brute)
    test_solution(solution_min_heap)
    test_solution(solution_divide_conquer)
    print("All tests passed!")
