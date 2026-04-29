"""
LC 94. 二叉树的中序遍历 (Binary Tree Inorder Traversal)
Difficulty: Easy
Tags: Stack, Tree, Depth-First Search, Binary Tree
Link: https://leetcode.cn/problems/binary-tree-inorder-traversal/
Category: 08-binary-tree
"""


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right


# ===== 暴力解法 (Recursive) =====
# 思路: 递归地按照 左→根→右 的顺序访问节点。实现简单直接，
#       但递归深度受调用栈限制，最坏情况下 O(n) 栈空间。
# 复杂度: O(n) time, O(h) space (h 是树高，最坏 O(n))
def solution_brute(root: TreeNode | None) -> list[int]:
    # WHY: 结果列表在递归过程中需要共享，用嵌套函数来避免传参
    result: list[int] = []

    def inorder(node: TreeNode | None) -> None:
        if not node:
            return
        # WHY: 先遍历左子树，利用递归调用栈天然支持回溯
        inorder(node.left)
        # WHY: 在左子树访问完后记录根节点值（中序的核心：左-根-右）
        result.append(node.val)
        # WHY: 最后遍历右子树，完成整个中序遍历
        inorder(node.right)

    inorder(root)
    return result


# ===== 最优解法 (Iterative using Stack) =====
# 思路: 使用显式栈模拟递归过程。先将左子树全部入栈，然后弹出访问，
#       再处理右子树。避免了递归调用栈溢出的风险。
# 复杂度: O(n) time, O(h) space (h 是树高)
def solution_optimal(root: TreeNode | None) -> list[int]:
    # WHY: 结果列表存储遍历顺序
    result: list[int] = []
    # WHY: 显式栈用于模拟递归调用，存储等待处理的节点
    stack: list[TreeNode] = []
    cur = root

    # WHY: cur 不为空或栈不为空时继续遍历
    while cur or stack:
        # WHY: 尽可能深入左子树，将沿途所有节点压栈
        # WHY: 这模拟了递归中不断调用 inorder(node.left) 的过程
        while cur:
            stack.append(cur)
            cur = cur.left

        # WHY: 弹出栈顶节点（最近一个无左子树的节点）
        cur = stack.pop()
        # WHY: 访问该节点（中序遍历：左子树访问完后再访问根）
        result.append(cur.val)
        # WHY: 转向右子树，下一轮循环处理右子树的中序遍历
        cur = cur.right

    return result


# ===== 辅助函数 =====
def array_to_tree(arr: list[int | None]) -> TreeNode | None:
    """根据层序遍历数组构建二叉树"""
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
    print("Testing Binary Tree Inorder Traversal...")

    # Test 1: [1,null,2,3] -> [1,3,2]
    root1 = array_to_tree([1, None, 2, 3])
    result1 = solution_optimal(root1)
    assert result1 == [1, 3, 2], f"Test 1 failed! Got {result1}"

    # Test 2: 空树 -> []
    result2 = solution_optimal(None)
    assert result2 == [], f"Test 2 failed! Got {result2}"

    # Test 3: [1] -> [1]
    root3 = array_to_tree([1])
    result3 = solution_optimal(root3)
    assert result3 == [1], f"Test 3 failed! Got {result3}"

    # Test 4: [1,2,3,4,5] -> [4,2,5,1,3]
    root4 = array_to_tree([1, 2, 3, 4, 5])
    result4 = solution_optimal(root4)
    assert result4 == [4, 2, 5, 1, 3], f"Test 4 failed! Got {result4}"

    print("All tests passed!")
