"""
LC 114. Flatten Binary Tree to Linked List
Difficulty: Medium
Tags: Tree, Binary Tree, DFS, Linked List
Link: https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/
Category: 08-binary-tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ===== 暴力解法 =====
# 思路: 前序遍历收集所有节点到列表，然后按顺序重新链接成右斜树
# 复杂度: O(n) time, O(n) space
def solution_brute(root: TreeNode) -> None:
    # WHY: 处理空树情况
    if not root:
        return
    # WHY: 使用列表存储前序遍历的节点顺序
    nodes = []

    # WHY: 定义前序遍历函数
    def preorder(node):
        # WHY: 空节点直接返回
        if not node:
            return
        # WHY: 先访问根节点，将节点加入列表
        nodes.append(node)
        # WHY: 再遍历左子树
        preorder(node.left)
        # WHY: 最后遍历右子树
        preorder(node.right)

    # WHY: 执行前序遍历
    preorder(root)
    # WHY: 遍历节点列表，重新构建链表结构
    for i in range(len(nodes) - 1):
        # WHY: 当前节点的左子指针置空
        nodes[i].left = None
        # WHY: 当前节点的右子指针指向下一个节点，形成链表
        nodes[i].right = nodes[i + 1]
    # WHY: 最后一个节点的左右指针都置空
    nodes[-1].left = None
    nodes[-1].right = None


# ===== 最优解法 =====
# 思路: 反向后序遍历（右-左-根），用全局prev指针记录上一个访问的节点，原地构建链表
# 复杂度: O(n) time, O(h) space (h为树高)
def solution_optimal(root: TreeNode) -> None:
    # WHY: prev指针记录前一个已处理的节点（在展平链表中的下一个节点）
    prev = None

    # WHY: 定义反向后序遍历函数（右-左-根）
    def flatten_post(node):
        # WHY: 使用nonlocal声明prev变量来自外部作用域
        nonlocal prev
        # WHY: 空节点直接返回
        if not node:
            return
        # WHY: 先展平右子树（因为展平后右子树在链表尾部）
        flatten_post(node.right)
        # WHY: 再展平左子树
        flatten_post(node.left)
        # WHY: 当前节点的右指针指向上一个处理的节点
        # WHY: 因为是从后往前处理，prev始终是链表中当前节点之后的节点
        node.right = prev
        # WHY: 当前节点的左指针置空
        node.left = None
        # WHY: 更新prev为当前节点，供前一个节点使用
        prev = node

    # WHY: 从根节点开始展平
    flatten_post(root)


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Flatten Binary Tree to Linked List...")

    # 辅助函数：将展平后的树转换为值列表用于验证
    def tree_to_list(root):
        vals = []
        while root:
            vals.append(root.val)
            root = root.right
        return vals

    # 测试用例1: [1,2,5,3,4,null,6] -> 1->2->3->4->5->6
    #     1
    #    / \
    #   2   5
    #  / \   \
    # 3   4   6
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(5)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(4)
    root1.right.right = TreeNode(6)

    # 复制树用于最优解法测试
    root1a = TreeNode(1)
    root1a.left = TreeNode(2)
    root1a.right = TreeNode(5)
    root1a.left.left = TreeNode(3)
    root1a.left.right = TreeNode(4)
    root1a.right.right = TreeNode(6)

    solution_brute(root1)
    assert tree_to_list(root1) == [1, 2, 3, 4, 5, 6], "测试用例1暴力解法失败"
    print("测试用例1暴力解法通过")

    solution_optimal(root1a)
    assert tree_to_list(root1a) == [1, 2, 3, 4, 5, 6], "测试用例1最优解法失败"
    print("测试用例1最优解法通过")

    # 测试用例2: 单节点 [0] -> [0]
    root2 = TreeNode(0)
    root2a = TreeNode(0)
    solution_brute(root2)
    assert tree_to_list(root2) == [0], "测试用例2暴力解法失败"
    solution_optimal(root2a)
    assert tree_to_list(root2a) == [0], "测试用例2最优解法失败"
    print("测试用例2通过: [0] -> [0]")

    print("All tests passed!")
