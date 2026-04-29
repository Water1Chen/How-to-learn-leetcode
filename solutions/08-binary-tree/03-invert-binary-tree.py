"""
LC 226. 翻转二叉树 (Invert Binary Tree)
Difficulty: Easy
Tags: Tree, Depth-First Search, Breadth-First Search, Binary Tree
Link: https://leetcode.cn/problems/invert-binary-tree/
Category: 08-binary-tree
"""

from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right


# ===== 暴力解法 (Recursive DFS Swap) =====
# 思路: 递归地翻转左右子树，然后将当前节点的左右子树交换。
#       从叶子节点开始向上翻转，每层交换左右孩子。
# 复杂度: O(n) time, O(h) space (h 是树高)
def solution_brute(root: TreeNode | None) -> TreeNode | None:
    # WHY: 空节点不处理，直接返回
    if not root:
        return None

    # WHY: 递归翻转左子树，返回翻转后的左子树根节点
    left = solution_brute(root.left)
    # WHY: 递归翻转右子树，返回翻转后的右子树根节点
    right = solution_brute(root.right)

    # WHY: 交换左右子树：翻转后的右子树成为新的左子树
    root.left = right
    # WHY: 翻转后的左子树成为新的右子树
    root.right = left

    # WHY: 返回翻转后的当前节点给上层
    return root


# ===== 最优解法 (Iterative BFS/DFS Swap) =====
# 思路: 使用队列进行层序遍历，每取出一个节点就交换其左右子树，
#       然后将子节点入队继续处理。迭代方式避免了递归栈溢出。
# 复杂度: O(n) time, O(n) space (队列存储)
def solution_optimal(root: TreeNode | None) -> TreeNode | None:
    if not root:
        return None

    # WHY: 使用 deque 实现 BFS 队列，popleft 保证 O(1) 的出队操作
    queue: deque[TreeNode] = deque([root])

    # WHY: 遍历每个节点，对其执行左右子树交换
    while queue:
        # WHY: 取出一个当前节点进行处理
        node = queue.popleft()

        # WHY: 交换当前节点的左右子树，这是翻转的核心操作
        node.left, node.right = node.right, node.left

        # WHY: 如果左子树存在，入队等待后续翻转
        if node.left:
            queue.append(node.left)
        # WHY: 如果右子树存在，入队等待后续翻转
        if node.right:
            queue.append(node.right)

    # WHY: 返回翻转后的根节点
    return root


# ===== 辅助函数 =====
def tree_to_array(root: TreeNode | None) -> list[int | None]:
    """将二叉树转为层序遍历数组（仅用于测试对比）"""
    if not root:
        return []
    result: list[int | None] = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # WHY: 去掉末尾的 None，使其更简洁
    while result and result[-1] is None:
        result.pop()
    return result


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
    print("Testing Invert Binary Tree...")

    # Test 1: [4,2,7,1,3,6,9] -> [4,7,2,9,6,3,1]
    root1 = array_to_tree([4, 2, 7, 1, 3, 6, 9])
    result1 = solution_optimal(root1)
    assert tree_to_array(result1) == [4, 7, 2, 9, 6, 3, 1], "Test 1 failed!"

    # Test 2: [2,1,3] -> [2,3,1]
    root2 = array_to_tree([2, 1, 3])
    result2 = solution_optimal(root2)
    assert tree_to_array(result2) == [2, 3, 1], "Test 2 failed!"

    # Test 3: 空树 -> []
    result3 = solution_optimal(None)
    assert tree_to_array(result3) == [], "Test 3 failed!"

    # Test 4: [1] -> [1]
    root4 = array_to_tree([1])
    result4 = solution_optimal(root4)
    assert tree_to_array(result4) == [1], "Test 4 failed!"

    print("All tests passed!")
