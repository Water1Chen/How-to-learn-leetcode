"""
LC 104. 二叉树的最大深度 (Maximum Depth of Binary Tree)
Difficulty: Easy
Tags: Tree, Depth-First Search, Breadth-First Search, Binary Tree
Link: https://leetcode.cn/problems/maximum-depth-of-binary-tree/
Category: 08-binary-tree
"""

from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right


# ===== 暴力解法 (DFS Recursive) =====
# 思路: 递归计算左右子树的最大深度，取较大者加 1。自底向上
#       逐层返回深度值，代码简洁但递归深度受限于树高。
# 复杂度: O(n) time, O(h) space (h 是树高，最坏 O(n))
def solution_brute(root: TreeNode | None) -> int:
    # WHY: 空节点的深度为 0，作为递归的终止条件
    if not root:
        return 0
    # WHY: 递归计算左子树的深度，DFS 会一直向下直到叶子节点
    left_depth = solution_brute(root.left)
    # WHY: 递归计算右子树的深度
    right_depth = solution_brute(root.right)
    # WHY: 当前节点的深度 = 左右子树最大深度 + 1（加上当前层）
    return max(left_depth, right_depth) + 1


# ===== 最优解法 (BFS Level-Order) =====
# 思路: 按层遍历，每遍历完一层深度加 1。当队列为空时得到的
#       深度就是最大深度。BFS 在求深度问题中空间效率可控。
# 复杂度: O(n) time, O(w) space (w 是最大宽度，最坏 O(n/2))
def solution_optimal(root: TreeNode | None) -> int:
    if not root:
        return 0

    # WHY: 使用 deque 实现 BFS 队列，popleft 是 O(1) 操作
    queue: deque[TreeNode] = deque([root])
    depth = 0

    # WHY: 按层处理，每处理完一层 depth 加 1
    while queue:
        # WHY: 记录当前层的节点数，确保只处理当前层的节点
        level_size = len(queue)
        # WHY: 一次性处理完当前层的所有节点
        for _ in range(level_size):
            # WHY: 取出当前层的一个节点
            node = queue.popleft()
            # WHY: 将下一层的子节点加入队列，供后续轮次处理
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        # WHY: 当前层处理完毕，深度增加 1
        depth += 1

    return depth


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
    print("Testing Maximum Depth of Binary Tree...")

    # Test 1: [3,9,20,null,null,15,7] -> 3
    root1 = array_to_tree([3, 9, 20, None, None, 15, 7])
    assert solution_optimal(root1) == 3, "Test 1 failed!"

    # Test 2: [1,null,2] -> 2 (单链)
    root2 = array_to_tree([1, None, 2])
    assert solution_optimal(root2) == 2, "Test 2 failed!"

    # Test 3: 空树 -> 0
    assert solution_optimal(None) == 0, "Test 3 failed!"

    # Test 4: [1] -> 1
    root4 = array_to_tree([1])
    assert solution_optimal(root4) == 1, "Test 4 failed!"

    print("All tests passed!")
