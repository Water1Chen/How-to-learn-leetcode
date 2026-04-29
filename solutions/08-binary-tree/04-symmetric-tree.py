"""
LC 101. 对称二叉树 (Symmetric Tree)
Difficulty: Easy
Tags: Tree, Depth-First Search, Breadth-First Search, Binary Tree
Link: https://leetcode.cn/problems/symmetric-tree/
Category: 08-binary-tree
"""

from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right


# ===== 暴力解法 (Recursive Mirror Check) =====
# 思路: 递归检查左右子树是否互为镜像。两个节点对称的条件是：
#       (1) 值相等 (2) A.left 与 B.right 对称 (3) A.right 与 B.left 对称。
# 复杂度: O(n) time, O(h) space (h 是树高)
def solution_brute(root: TreeNode | None) -> bool:
    # WHY: 辅助函数判断两个子树是否互为镜像
    def is_mirror(t1: TreeNode | None, t2: TreeNode | None) -> bool:
        # WHY: 两个都为空 => 对称
        if not t1 and not t2:
            return True
        # WHY: 一个为空一个不为空 => 不对称
        if not t1 or not t2:
            return False
        # WHY: 值必须相等，且 t1.left 和 t2.right 互为镜像，t1.right 和 t2.left 互为镜像
        return (t1.val == t2.val and
                is_mirror(t1.left, t2.right) and
                is_mirror(t1.right, t2.left))

    # WHY: 从根节点开始，检查左右子树是否镜像对称
    return is_mirror(root.left if root else None, root.right if root else None)


# ===== 最优解法 (Iterative BFS Pair Check) =====
# 思路: 使用队列成对地插入和取出节点进行比较。每次取出两个节点
#       检查值是否相等，然后按镜像顺序插入它们的子节点。
# 复杂度: O(n) time, O(n) space (队列存储)
def solution_optimal(root: TreeNode | None) -> bool:
    if not root:
        return True

    # WHY: 使用 deque 实现队列，初始放入左右子节点作为第一对待比较对
    queue: deque[TreeNode | None] = deque([root.left, root.right])

    while queue:
        # WHY: 每次取出两个节点进行比较（它们应该互为镜像位置）
        t1 = queue.popleft()
        t2 = queue.popleft()

        # WHY: 两个都是 None，当前镜像位置正确，继续检查其他对
        if not t1 and not t2:
            continue
        # WHY: 其中一个为 None，另一个不为 None，不对称
        if not t1 or not t2:
            return False
        # WHY: 两个节点的值必须相等，否则不对称
        if t1.val != t2.val:
            return False

        # WHY: 按镜像顺序插入子节点对，保证后续比较的是镜像位置
        # WHY: t1.left 应该和 t2.right 对称
        queue.append(t1.left)
        queue.append(t2.right)
        # WHY: t1.right 应该和 t2.left 对称
        queue.append(t1.right)
        queue.append(t2.left)

    # WHY: 所有成对节点都通过了检查，树是对称的
    return True


# ===== 辅助函数 =====
def array_to_tree(arr: list[int | None]) -> TreeNode | None:
    if not arr or arr[0] is None:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while i < len(arr):
        node = queue.pop(0)
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])  # type: ignore[arg-type]
            queue.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])  # type: ignore[arg-type]
            queue.append(node.right)
        i += 1
    return root


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Symmetric Tree...")

    # Test 1: [1,2,2,3,4,4,3] -> True
    root1 = array_to_tree([1, 2, 2, 3, 4, 4, 3])
    assert solution_optimal(root1) is True, "Test 1 failed!"

    # Test 2: [1,2,2,null,3,null,3] -> False
    root2 = array_to_tree([1, 2, 2, None, 3, None, 3])
    assert solution_optimal(root2) is False, "Test 2 failed!"

    # Test 3: 空树 -> True
    assert solution_optimal(None) is True, "Test 3 failed!"

    # Test 4: [1] -> True
    root4 = array_to_tree([1])
    assert solution_optimal(root4) is True, "Test 4 failed!"

    print("All tests passed!")
