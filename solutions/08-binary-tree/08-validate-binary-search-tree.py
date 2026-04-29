"""
LC 98. 验证二叉搜索树 (Validate Binary Search Tree)
Difficulty: Medium
Tags: Tree, Binary Search Tree, Depth-First Search, Binary Tree
Link: https://leetcode.cn/problems/validate-binary-search-tree/
Category: 08-binary-tree
"""


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right


# ===== 暴力解法 (Inorder + Check Sorted) =====
# 思路: BST 的中序遍历结果一定是严格递增序列。先中序遍历得到数组，
#       再检查数组是否严格递增（相邻元素不相等）。
# 复杂度: O(n) time, O(n) space
def solution_brute(root: TreeNode | None) -> bool:
    # WHY: 存储中序遍历的结果，用于后续的递增性检查
    values: list[int] = []

    # WHY: 递归中序遍历，按左-根-右顺序收集节点值
    def inorder(node: TreeNode | None) -> None:
        if not node:
            return
        inorder(node.left)
        values.append(node.val)
        inorder(node.right)

    inorder(root)

    # WHY: 检查数组是否严格递增：如果存在相邻相等或递减则不是 BST
    for i in range(1, len(values)):
        # WHY: BST 不允许重复值，所以是 < 而不是 <=
        if values[i] <= values[i - 1]:
            return False

    return True


# ===== 最优解法 (Recursive Range Check) =====
# 思路: 递归遍历时传递每个节点允许的数值范围 [low, high]。
#       左子树的节点值必须在 (low, root.val) 之间，
#       右子树的节点值必须在 (root.val, high) 之间。
# 复杂度: O(n) time, O(h) space (h 是树高)
def solution_optimal(root: TreeNode | None) -> bool:
    # WHY: 辅助函数检查以 node 为根的子树是否满足 BST 约束
    # WHY: low 是下限（不含），high 是上限（不含）
    def validate(node: TreeNode | None, low: float, high: float) -> bool:
        # WHY: 空节点视为有效 BST
        if not node:
            return True

        # WHY: 当前节点的值必须在 (low, high) 范围内
        # WHY: 使用 float('inf') 和 float('-inf') 处理根节点的无界情况
        if node.val <= low or node.val >= high:
            return False

        # WHY: 递归验证左子树：上限更新为当前节点值
        # WHY: 左子树的所有节点必须小于当前节点值
        if not validate(node.left, low, node.val):
            return False
        # WHY: 递归验证右子树：下限更新为当前节点值
        # WHY: 右子树的所有节点必须大于当前节点值
        if not validate(node.right, node.val, high):
            return False

        # WHY: 当前节点和左右子树都满足 BST 约束
        return True

    # WHY: 根节点的取值范围是 (-inf, +inf)，即无限制
    return validate(root, float('-inf'), float('inf'))


# ===== 方法二：Inorder with Prev Tracking (O(h) space) =====
# 思路: 在中序遍历的过程中实时检查前驱节点的值，无需额外数组。
#       每访问一个节点就与之前访问的节点比较。
# 复杂度: O(n) time, O(h) space (递归栈)
def solution_inorder_prev(root: TreeNode | None) -> bool:
    # WHY: 使用列表存储前驱节点值，以便在递归中修改外部变量的值
    prev: list[float] = [float('-inf')]
    # WHY: 标志位，当发现违反 BST 性质时提前终止递归
    is_valid: list[bool] = [True]

    # WHY: 中序遍历函数，同时检查递增性
    def inorder(node: TreeNode | None) -> None:
        if not node or not is_valid[0]:
            return

        # WHY: 遍历左子树
        inorder(node.left)

        # WHY: 如果当前节点值 <= 前驱值，违反 BST 性质
        if node.val <= prev[0]:
            is_valid[0] = False
            return
        # WHY: 更新前驱值为当前节点值
        prev[0] = float(node.val)

        # WHY: 遍历右子树
        inorder(node.right)

    inorder(root)
    return is_valid[0]


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
    print("Testing Validate Binary Search Tree...")

    # Test 1: [2,1,3] -> True
    root1 = array_to_tree([2, 1, 3])
    assert solution_optimal(root1) is True, "Test 1 failed!"
    assert solution_inorder_prev(root1) is True, "Test 1 (inorder) failed!"

    # Test 2: [5,1,4,null,null,3,6] -> False（5 的右子树中有 3 < 5）
    root2 = array_to_tree([5, 1, 4, None, None, 3, 6])
    assert solution_optimal(root2) is False, "Test 2 failed!"
    assert solution_inorder_prev(root2) is False, "Test 2 (inorder) failed!"

    # Test 3: 空树 -> True
    assert solution_optimal(None) is True, "Test 3 failed!"

    # Test 4: [2,2,2] -> False（重复值不是 BST）
    root4 = array_to_tree([2, 2, 2])
    assert solution_optimal(root4) is False, "Test 4 failed!"

    # Test 5: 左子树有右节点超过根节点值的情况 [5,4,6,null,null,3,7]
    # 节点 3 在 5 的右子树的左子树中，小于 5 但位置不对
    root5 = array_to_tree([5, 4, 6, None, None, 3, 7])
    assert solution_optimal(root5) is False, "Test 5 failed!"

    print("All tests passed!")
