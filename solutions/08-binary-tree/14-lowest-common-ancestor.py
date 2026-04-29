"""
LC 236. Lowest Common Ancestor of a Binary Tree
Difficulty: Medium
Tags: Tree, Binary Tree, DFS, Recursion
Link: https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/
Category: 08-binary-tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ===== 暴力解法 =====
# 思路: 分别找到根节点到p和q的路径，然后比较路径找到最后一个公共节点
# 复杂度: O(n) time, O(n) space
def solution_brute(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # WHY: 存储根节点到p节点的路径
    path_p = []
    # WHY: 存储根节点到q节点的路径
    path_q = []

    # WHY: 定义DFS函数查找从根到目标节点的路径
    def find_path(node, target, path):
        # WHY: 空节点返回False
        if not node:
            return False
        # WHY: 将当前节点加入路径
        path.append(node)
        # WHY: 如果当前节点就是目标节点，找到路径
        if node == target:
            return True
        # WHY: 递归在左子树中查找
        if find_path(node.left, target, path):
            return True
        # WHY: 递归在右子树中查找
        if find_path(node.right, target, path):
            return True
        # WHY: 左右子树都没找到，回溯移除当前节点
        path.pop()
        return False

    # WHY: 找到p和q的路径
    find_path(root, p, path_p)
    find_path(root, q, path_q)

    # WHY: i用于遍历两条路径，寻找最后一个公共节点
    i = 0
    # WHY: 在两条路径长度范围内逐个比较节点
    while i < len(path_p) and i < len(path_q):
        # WHY: 如果位置i的节点相同，继续检查下一个位置
        if path_p[i] == path_q[i]:
            i += 1
        else:
            # WHY: 遇到不同的节点，退出循环
            break

    # WHY: 返回最后一个公共节点（最低公共祖先）
    return path_p[i - 1]


# ===== 最优解法 =====
# 思路: 递归自底向上查找，如果在左/右子树中找到p或q则返回，若某节点左右都找到则当前节点为LCA
# 复杂度: O(n) time, O(h) space (h为树高)
def solution_optimal(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # WHY: 空节点直接返回None
    if not root:
        return None
    # WHY: 如果当前节点是p或q，则当前节点就是（可能的）LCA
    if root == p or root == q:
        return root

    # WHY: 在左子树中递归查找p或q
    left_result = solution_optimal(root.left, p, q)
    # WHY: 在右子树中递归查找p或q
    right_result = solution_optimal(root.right, p, q)

    # WHY: 如果左右子树都找到了（分别在左右子树中找到p和q）
    # WHY: 则当前节点就是最低公共祖先
    if left_result and right_result:
        return root

    # WHY: 如果只在左子树中找到，则LCA在左子树
    if left_result:
        return left_result
    # WHY: 如果只在右子树中找到，则LCA在右子树
    if right_result:
        return right_result

    # WHY: 左右都没找到，返回None
    return None


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Lowest Common Ancestor of a Binary Tree...")

    # 测试用例1: [3,5,1,6,2,0,8,null,null,7,4], p=5, q=1 -> LCA=3
    #       3
    #      / \
    #     5   1
    #    / \ / \
    #   6  2 0  8
    #     / \
    #    7   4
    root1 = TreeNode(3)
    root1.left = TreeNode(5)
    root1.right = TreeNode(1)
    root1.left.left = TreeNode(6)
    root1.left.right = TreeNode(2)
    root1.right.left = TreeNode(0)
    root1.right.right = TreeNode(8)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(4)
    p1 = root1.left
    q1 = root1.right
    assert solution_brute(root1, p1, q1).val == 3, "测试用例1暴力解法失败"
    assert solution_optimal(root1, p1, q1).val == 3, "测试用例1最优解法失败"
    print("测试用例1通过: p=5, q=1 -> LCA=3")

    # 测试用例2: p=5, q=4 -> LCA=5
    p2 = root1.left
    q2 = root1.left.right.right
    assert solution_brute(root1, p2, q2).val == 5, "测试用例2暴力解法失败"
    assert solution_optimal(root1, p2, q2).val == 5, "测试用例2最优解法失败"
    print("测试用例2通过: p=5, q=4 -> LCA=5")

    print("All tests passed!")
