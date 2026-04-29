"""
LC 138. 随机链表的复制 (Copy List with Random Pointer)
Difficulty: Medium
Tags: Hash Table, Linked List
Link: https://leetcode.cn/problems/copy-list-with-random-pointer/
Category: 07-linked-list
"""


# Definition for a Node with random pointer
class Node:
    def __init__(self, val: int = 0, next: 'Node | None' = None, random: 'Node | None' = None):
        # WHY: val 是节点值，next 指向下一个节点，random 指向任意节点或 None
        self.val = val
        self.next = next
        self.random = random


# ===== 暴力解法 (HashMap) =====
# 思路: 第一遍遍历创建所有新节点并建立旧→新映射；第二遍遍历根据映射
#       设置 next 和 random 指针。用 HashMap 建立新老节点对应关系。
# 复杂度: O(n) time, O(n) space
def solution_brute(head: Node | None) -> Node | None:
    if not head:
        return None

    # WHY: 存储原节点到新节点的映射，用于快速查找 random 指向的对应新节点
    old_to_new: dict[Node, Node] = {}

    # WHY: 第一遍遍历：创建所有新节点并建立映射关系
    cur = head
    while cur:
        # WHY: 为当前原节点创建一个值相同的新节点
        old_to_new[cur] = Node(cur.val)
        cur = cur.next

    # WHY: 第二遍遍历：设置新节点的 next 和 random 指针
    cur = head
    while cur:
        # WHY: 从映射中取出当前原节点对应的新节点
        new_node = old_to_new[cur]
        # WHY: 如果原节点有 next，则新节点的 next 指向对应映射中的新节点
        if cur.next:
            new_node.next = old_to_new[cur.next]
        # WHY: 如果原节点有 random，则新节点的 random 指向对应映射中的新节点
        if cur.random:
            new_node.random = old_to_new[cur.random]
        cur = cur.next

    # WHY: 返回原头节点对应的新头节点
    return old_to_new[head]


# ===== 最优解法 (Interleave O(1) Extra Space) =====
# 思路: 三步走：(1) 在每个原节点后面插入一个克隆节点；
#       (2) 利用"克隆节点在原节点后面"的特性设置 random 指针；
#       (3) 将交错链表拆分为原链表和新链表。
#       额外空间 O(1) 不计算输出空间。
# 复杂度: O(n) time, O(1) extra space (不计输出)
def solution_optimal(head: Node | None) -> Node | None:
    if not head:
        return None

    # WHY: 第一步：在每个原节点后插入克隆节点，构建交错链表
    # WHY: 这样克隆节点和原节点的位置关系固定，后续可据此设置 random
    cur = head
    while cur:
        # WHY: 创建当前原节点的克隆节点，值相同，next 指向原节点的下一个
        clone = Node(cur.val, cur.next, None)
        # WHY: 将克隆节点插入到当前原节点和原 next 之间
        cur.next = clone
        # WHY: 跳过刚插入的克隆节点，继续处理下一个原节点
        cur = clone.next

    # WHY: 第二步：设置克隆节点的 random 指针
    # WHY: 因为克隆节点就在原节点后面，原节点.random 的 next 就是对应的克隆节点
    cur = head
    while cur:
        # WHY: 如果原节点有 random 指针，它的克隆节点就在原节点后面
        if cur.random:
            # WHY: cur.next 是当前原节点的克隆节点
            # WHY: cur.random.next 是原节点 random 指向的节点的克隆节点
            cur.next.random = cur.random.next  # type: ignore[union-attr]
        cur = cur.next.next  # type: ignore[union-attr]

    # WHY: 第三步：拆分交错链表，恢复原链表并提取新链表
    dummy = Node(0)
    new_cur = dummy
    cur = head
    while cur:
        # WHY: 提取克隆节点到新链表
        clone = cur.next
        new_cur.next = clone  # type: ignore[union-attr]
        new_cur = clone  # type: ignore[union-attr]
        # WHY: 恢复原链表：当前原节点的 next 指向原 next 的克隆节点之后
        cur.next = clone.next  # type: ignore[union-attr]
        # WHY: 移动到下一个原节点
        cur = clone.next  # type: ignore[union-attr]

    # WHY: 返回新链表的头节点
    return dummy.next


# ===== 辅助函数 =====
def list_with_random_to_array(head: Node | None) -> list[list[int | None]]:
    # WHY: 将链表转换为 [[val, random_index], ...] 格式用于测试对比
    result: list[list[int | None]] = []
    # WHY: 先收集所有节点，建立节点到索引的映射
    nodes: list[Node] = []
    cur = head
    while cur:
        nodes.append(cur)
        cur = cur.next
    # WHY: 遍历节点，记录值和 random 指针的索引位置
    for i, node in enumerate(nodes):
        random_idx: int | None = None
        if node.random is not None:
            # WHY: 在节点列表中查找 random 指向的节点的索引
            random_idx = nodes.index(node.random)
        result.append([node.val, random_idx])
    return result


def array_to_list_with_random(arr: list[list[int | None]]) -> Node | None:
    # WHY: 从 [[val, random_index], ...] 格式构建链表
    if not arr:
        return None
    nodes: list[Node] = [Node(v[0]) for v in arr]  # type: ignore[misc]
    for i, node in enumerate(nodes):
        if i + 1 < len(nodes):
            node.next = nodes[i + 1]
        ri = arr[i][1]
        if ri is not None:
            node.random = nodes[ri]
    return nodes[0] if nodes else None


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Copy List with Random Pointer...")

    # Test 1: [[7,null],[13,0],[11,4],[10,2],[1,0]]
    arr1: list[list[int | None]] = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    head1 = array_to_list_with_random(arr1)
    result1 = solution_optimal(head1)
    assert list_with_random_to_array(result1) == arr1, "Test 1 failed!"
    # WHY: 验证是深拷贝，修改原链表不影响新链表
    assert result1 is not head1, "Test 1 failed: not a deep copy!"

    # Test 2: 空链表
    head2 = array_to_list_with_random([])
    result2 = solution_optimal(head2)
    assert list_with_random_to_array(result2) == [], "Test 2 failed!"

    # Test 3: 只有两个节点 [[1,1],[2,0]]
    arr3: list[list[int | None]] = [[1, 1], [2, 0]]
    head3 = array_to_list_with_random(arr3)
    result3 = solution_optimal(head3)
    assert list_with_random_to_array(result3) == arr3, "Test 3 failed!"

    print("All tests passed!")
