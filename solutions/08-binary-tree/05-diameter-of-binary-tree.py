"""
LC 543. 二叉树的直径 (Diameter of Binary Tree)
Difficulty: Easy
Tags: Tree, Depth-First Search, Binary Tree
Link: https://leetcode.cn/problems/diameter-of-binary-tree/
Category: 08-binary-tree
"""


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right


# ===== 暴力解法 (Naive per-node depth) =====
# 思路: 对每个节点计算左子树深度和右子树深度，直径 = left_depth + right_depth，
#       取全局最大值。但每个节点都要重复计算子树深度，效率低。
# 复杂度: O(n²) time in worst case (skewed tree), O(h) space
def depth(node: TreeNode | None) -> int:
    """计算以 node 为根的子树的最大深度"""
    if not node:
        return 0
    # WHY: 递归计算左右子树深度，取较大值加 1
    return max(depth(node.left), depth(node.right)) + 1


def solution_brute(root: TreeNode | None) -> int:
    if not root:
        return 0

    # WHY: 计算经过当前节点的直径（左深度 + 右深度）
    left_depth = depth(root.left)
    right_depth = depth(root.right)
    current_diameter = left_depth + right_depth

    # WHY: 递归计算左子树和右子树内部的直径，取三者中的最大值
    left_diameter = solution_brute(root.left)
    right_diameter = solution_brute(root.right)

    # WHY: 最大直径可能是经过当前节点，也可能在左子树或右子树内部
    return max(current_diameter, left_diameter, right_diameter)


# ===== 最优解法 (DFS with global max) =====
# 思路: 在后序遍历的过程中同时计算深度和更新全局最大直径。
#       每个节点只访问一次，避免了重复计算。
# 复杂度: O(n) time, O(h) space (递归栈)
def solution_optimal(root: TreeNode | None) -> int:
    # WHY: 使用列表存储全局最大直径，在嵌套函数中可以修改外部变量
    max_diameter: list[int] = [0]

    # WHY: 后序遍历函数，返回子树深度，同时更新全局最大直径
    def dfs(node: TreeNode | None) -> int:
        if not node:
            return 0

        # WHY: 递归计算左右子树的深度
        left_depth = dfs(node.left)
        right_depth = dfs(node.right)

        # WHY: 经过当前节点的直径 = 左深度 + 右深度
        # WHY: 更新全局最大值，因为直径可以不经过根节点
        max_diameter[0] = max(max_diameter[0], left_depth + right_depth)

        # WHY: 返回当前子树的深度供父节点使用
        return max(left_depth, right_depth) + 1

    dfs(root)
    return max_diameter[0]


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
    print("Testing Diameter of Binary Tree...")

    # Test 1: [1,2,3,4,5] -> 3 (路径 4->2->1->3 或 5->2->1->3)
    root1 = array_to_tree([1, 2, 3, 4, 5])
    assert solution_optimal(root1) == 3, "Test 1 failed!"

    # Test 2: [1,2] -> 1
    root2 = array_to_tree([1, 2])
    assert solution_optimal(root2) == 1, "Test 2 failed!"

    # Test 3: 空树 -> 0
    assert solution_optimal(None) == 0, "Test 3 failed!"

    # Test 4: 单链 [1,2,3,4] -> 3
    root4 = array_to_tree([1, 2, 3, 4])
    assert solution_optimal(root4) == 3, "Test 4 failed!"

    print("All tests passed!")
