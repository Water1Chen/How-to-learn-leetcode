"""
LC 102. 二叉树的层序遍历 (Binary Tree Level Order Traversal)
Difficulty: Medium
Tags: Tree, Breadth-First Search, Binary Tree
Link: https://leetcode.cn/problems/binary-tree-level-order-traversal/
Category: 08-binary-tree
"""

from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right


# ===== 暴力解法 (Recursive with level param) =====
# 思路: 前序遍历时携带层级参数 level，将节点值放入结果列表中
#       对应层级的位置。需要预先知道树的高度或动态扩展列表。
# 复杂度: O(n) time, O(h) space (递归栈 + 结果数组)
def solution_brute(root: TreeNode | None) -> list[list[int]]:
    # WHY: 结果列表，result[level] 存储该层的所有节点值
    result: list[list[int]] = []

    # WHY: 辅助递归函数，level 表示当前节点所在的层数（从 0 开始）
    def traverse(node: TreeNode | None, level: int) -> None:
        if not node:
            return

        # WHY: 如果当前层还没有在 result 中创建列表，则新建一个
        if len(result) <= level:
            result.append([])

        # WHY: 将当前节点的值加入对应层的列表中
        result[level].append(node.val)

        # WHY: 递归遍历左子树，层级加 1
        traverse(node.left, level + 1)
        # WHY: 递归遍历右子树，层级加 1
        traverse(node.right, level + 1)

    traverse(root, 0)
    return result


# ===== 最优解法 (BFS with Queue and Level Size) =====
# 思路: 使用队列进行层序遍历。每轮循环开始时记录当前队列长度
#       （即当前层的节点数），然后一次性处理完这一层的所有节点。
#       每处理完一层，将其加入结果列表。
# 复杂度: O(n) time, O(w) space (w 是最大宽度)
def solution_optimal(root: TreeNode | None) -> list[list[int]]:
    if not root:
        return []

    # WHY: 结果列表，每个元素是一层的节点值列表
    result: list[list[int]] = []
    # WHY: 使用 deque 实现 O(1) 的入队和出队操作
    queue: deque[TreeNode] = deque([root])

    # WHY: 队列不为空说明还有节点需要处理
    while queue:
        # WHY: 记录当前层的节点数，这是 BFS 按层处理的关键
        level_size = len(queue)
        # WHY: 存储当前层的所有节点值
        current_level: list[int] = []

        # WHY: 只处理 level_size 个节点，确保不会越界到下一层
        for _ in range(level_size):
            # WHY: 从队列头部取出一个节点
            node = queue.popleft()
            # WHY: 记录当前节点的值到当前层的列表中
            current_level.append(node.val)
            # WHY: 将左右子节点入队，它们属于下一层
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # WHY: 当前层处理完毕，将结果加入最终列表
        result.append(current_level)

    return result


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
    print("Testing Binary Tree Level Order Traversal...")

    # Test 1: [3,9,20,null,null,15,7] -> [[3],[9,20],[15,7]]
    root1 = array_to_tree([3, 9, 20, None, None, 15, 7])
    result1 = solution_optimal(root1)
    assert result1 == [[3], [9, 20], [15, 7]], f"Test 1 failed! Got {result1}"

    # Test 2: [1] -> [[1]]
    root2 = array_to_tree([1])
    result2 = solution_optimal(root2)
    assert result2 == [[1]], f"Test 2 failed! Got {result2}"

    # Test 3: 空树 -> []
    result3 = solution_optimal(None)
    assert result3 == [], f"Test 3 failed! Got {result3}"

    # Test 4: [1,2,3,4,null,null,5] -> [[1],[2,3],[4,5]]
    root4 = array_to_tree([1, 2, 3, 4, None, None, 5])
    result4 = solution_optimal(root4)
    assert result4 == [[1], [2, 3], [4, 5]], f"Test 4 failed! Got {result4}"

    print("All tests passed!")
