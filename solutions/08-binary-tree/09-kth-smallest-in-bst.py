"""
LC 230. Kth Smallest Element in a BST
Difficulty: Medium
Tags: Tree, Binary Search Tree, Depth-First Search
Link: https://leetcode.cn/problems/kth-smallest-element-in-a-bst/
Category: 08-binary-tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ===== 暴力解法 =====
# 思路: 中序遍历BST得到有序数组，直接返回第k-1个元素
# 复杂度: O(n) time, O(n) space
def solution_brute(root: TreeNode, k: int) -> int:
    # WHY: 使用列表存储完整的中序遍历结果
    vals = []
    # WHY: 定义递归中序遍历函数
    def inorder(node):
        # WHY: 空节点直接返回
        if not node:
            return
        # WHY: 先遍历左子树（BST中左子树所有节点值更小）
        inorder(node.left)
        # WHY: 访问当前节点，将值加入列表
        vals.append(node.val)
        # WHY: 再遍历右子树（BST中右子树所有节点值更大）
        inorder(node.right)
    # WHY: 执行中序遍历
    inorder(root)
    # WHY: 返回有序数组中第k-1个元素（第k小的元素）
    return vals[k - 1]


# ===== 最优解法 =====
# 思路: 中序遍历时维护计数器，当计数达到k时提前终止，无需遍历整棵树
# 复杂度: O(h + k) time, O(h) space (h为树高，递归栈深度)
def solution_optimal(root: TreeNode, k: int) -> int:
    # WHY: 使用列表包装counter和result，便于在嵌套函数中修改
    # WHY: counter记录已访问的节点数量
    counter = [0]
    # WHY: result存储第k小的节点值
    result = [0]

    # WHY: 定义递归中序遍历函数，带提前终止逻辑
    def inorder(node):
        # WHY: 空节点或已找到结果，直接返回
        if not node or result[0] != 0:
            return
        # WHY: 先遍历左子树
        inorder(node.left)
        # WHY: 如果已找到结果，提前返回
        if result[0] != 0:
            return
        # WHY: 访问当前节点，递增计数器
        counter[0] += 1
        # WHY: 如果当前节点是第k个访问的节点
        if counter[0] == k:
            # WHY: 记录结果，终止后续遍历
            result[0] = node.val
            return
        # WHY: 再遍历右子树
        inorder(node.right)

    # WHY: 执行优化中序遍历
    inorder(root)
    # WHY: 返回第k小的元素值
    return result[0]


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Kth Smallest Element in BST...")

    # 测试用例1: [3,1,4,null,2], k=1 -> 1
    #     3
    #    / \
    #   1   4
    #    \
    #     2
    root1 = TreeNode(3)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)
    root1.left.right = TreeNode(2)
    assert solution_brute(root1, 1) == 1, "测试用例1暴力解法失败"
    assert solution_optimal(root1, 1) == 1, "测试用例1最优解法失败"
    print("测试用例1通过: [3,1,4,null,2], k=1 -> 1")

    # 测试用例2: [5,3,6,2,4,null,null,1], k=3 -> 3
    #       5
    #      / \
    #     3   6
    #    / \
    #   2   4
    #  /
    # 1
    root2 = TreeNode(5)
    root2.left = TreeNode(3)
    root2.right = TreeNode(6)
    root2.left.left = TreeNode(2)
    root2.left.right = TreeNode(4)
    root2.left.left.left = TreeNode(1)
    assert solution_brute(root2, 3) == 3, "测试用例2暴力解法失败"
    assert solution_optimal(root2, 3) == 3, "测试用例2最优解法失败"
    print("测试用例2通过: [5,3,6,2,4,null,null,1], k=3 -> 3")

    print("All tests passed!")
