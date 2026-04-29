"""
LC 146. LRU 缓存 (LRU Cache)
Difficulty: Medium
Tags: Design, Hash Table, Linked List, Doubly-Linked List
Link: https://leetcode.cn/problems/lru-cache/
Category: 07-linked-list
"""


class _DLinkedNode:
    """双向链表节点，比普通节点多一个 prev 指针支持 O(1) 删除"""
    def __init__(self, key: int = 0, val: int = 0):
        # WHY: key 用于在哈希表中定位，val 是缓存的值
        self.key = key
        self.val = val
        # WHY: prev 和 next 实现双向链接，支持 O(1) 插入和删除
        self.prev: _DLinkedNode | None = None
        self.next: _DLinkedNode | None = None


# ===== 暴力解法 (List-based) =====
# 思路: 用 Python list 存储 (key, value) 对，每次访问时线性查找并将
#       访问项移到末尾，容量满时删除第一项。
# 复杂度: get O(n), put O(n) time; O(n) space
class LRUCacheBrute:
    def __init__(self, capacity: int):
        # WHY: 直接用 list 模拟缓存行为，不使用哈希索引
        self.capacity = capacity
        self.cache: list[tuple[int, int]] = []

    def get(self, key: int) -> int:
        # WHY: 线性查找 key 在缓存中的位置
        for i, (k, v) in enumerate(self.cache):
            if k == key:
                # WHY: 将访问的项移到末尾，表示最近使用
                item = self.cache.pop(i)
                self.cache.append(item)
                return v
        return -1

    def put(self, key: int, value: int) -> None:
        # WHY: 先查找 key 是否存在
        for i, (k, _v) in enumerate(self.cache):
            if k == key:
                # WHY: 存在则更新值并移到末尾
                self.cache.pop(i)
                self.cache.append((key, value))
                return
        # WHY: 不存在则检查容量，满了先淘汰最久未使用（第一项）
        if len(self.cache) >= self.capacity:
            self.cache.pop(0)
        # WHY: 添加新项到末尾（最近使用的位置）
        self.cache.append((key, value))


# ===== 最优解法 (HashMap + Doubly Linked List) =====
# 思路: 双向链表维护访问顺序（头部最近使用，尾部最久未使用），
#       哈希表提供 O(1) 的节点查找。get 和 put 都在 O(1) 完成。
# 复杂度: get O(1), put O(1) time; O(capacity) space
class LRUCache:
    def __init__(self, capacity: int):
        # WHY: capacity 决定了缓存的最大条目数
        self.capacity = capacity
        # WHY: 哈希表提供 key 到链表节点的 O(1) 映射
        self.cache: dict[int, _DLinkedNode] = {}

        # WHY: 虚拟头尾节点避免边界判断，头节点的 next 是最新使用的
        self.head = _DLinkedNode()
        self.tail = _DLinkedNode()
        # WHY: 初始时头尾相连，链表为空
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_to_head(self, node: _DLinkedNode) -> None:
        """将节点添加到链表头部（最近使用的位置）"""
        # WHY: 新节点的 next 指向当前第一个真实节点
        node.next = self.head.next
        # WHY: 新节点的 prev 指向虚拟头节点
        node.prev = self.head
        # WHY: 原第一个节点的 prev 指向新节点
        self.head.next.prev = node  # type: ignore[union-attr]
        # WHY: 虚拟头节点的 next 指向新节点，完成插入
        self.head.next = node

    def _remove_node(self, node: _DLinkedNode) -> None:
        """从链表中删除指定节点（O(1) 时间）"""
        # WHY: 将前后节点直接连接，跳过当前节点
        node.prev.next = node.next  # type: ignore[union-attr]
        node.next.prev = node.prev  # type: ignore[union-attr]

    def _move_to_head(self, node: _DLinkedNode) -> None:
        """将节点移动到头部（标记为最近使用）"""
        # WHY: 先删除后插入，两步完成"移动到头部"这个复合操作
        self._remove_node(node)
        self._add_to_head(node)

    def _pop_tail(self) -> _DLinkedNode:
        """移除并返回链表尾部的节点（最久未使用）"""
        # WHY: tail.prev 是最后一个真实节点
        node = self.tail.prev  # type: ignore[union-attr]
        self._remove_node(node)
        return node

    def get(self, key: int) -> int:
        # WHY: 通过哈希表 O(1) 查找节点是否存在
        node = self.cache.get(key)
        if not node:
            return -1
        # WHY: 访问过的节点要移到头部，标记为最近使用
        self._move_to_head(node)
        return node.val

    def put(self, key: int, val: int) -> None:
        # WHY: 检查 key 是否已存在
        node = self.cache.get(key)
        if node:
            # WHY: 已存在则更新值并移到头部
            node.val = val
            self._move_to_head(node)
            return

        # WHY: 不存在则创建新节点
        new_node = _DLinkedNode(key, val)
        self.cache[key] = new_node
        # WHY: 新节点添加到头部（最近使用）
        self._add_to_head(new_node)

        # WHY: 如果超过容量，淘汰最久未使用的节点
        if len(self.cache) > self.capacity:
            # WHY: 从链表尾部移除最久未使用的节点
            tail = self._pop_tail()
            # WHY: 同时从哈希表中删除映射，保持数据一致性
            del self.cache[tail.key]


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing LRU Cache...")

    # Test 1: 标准测试用例
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1, "Test 1 get(1) failed!"
    cache.put(3, 3)    # 淘汰 key 2
    assert cache.get(2) == -1, "Test 1 get(2) failed!"
    cache.put(4, 4)    # 淘汰 key 1
    assert cache.get(1) == -1, "Test 1 get(1) after put(4) failed!"
    assert cache.get(3) == 3, "Test 1 get(3) failed!"
    assert cache.get(4) == 4, "Test 1 get(4) failed!"
    print("Test 1 passed!")

    # Test 2: get 不存在的 key
    cache2 = LRUCache(1)
    cache2.put(2, 1)
    assert cache2.get(2) == 1, "Test 2 get(2) failed!"
    assert cache2.get(3) == -1, "Test 2 get(3) failed!"
    print("Test 2 passed!")

    # Test 3: 更新已有的 key
    cache3 = LRUCache(2)
    cache3.put(1, 1)
    cache3.put(1, 2)
    assert cache3.get(1) == 2, "Test 3 failed!"
    print("Test 3 passed!")

    # Test 4: 暴力解法也跑一遍确保正确
    bf = LRUCacheBrute(2)
    bf.put(1, 1)
    bf.put(2, 2)
    assert bf.get(1) == 1, "Brute Test 1 failed!"
    bf.put(3, 3)
    assert bf.get(2) == -1, "Brute Test 2 failed!"
    print("Brute force test passed!")

    print("All tests passed!")
