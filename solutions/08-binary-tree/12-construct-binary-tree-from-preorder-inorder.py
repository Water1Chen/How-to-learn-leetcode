"""
LC 105. Construct Binary Tree from Preorder and Inorder Traversal
Difficulty: Medium
Tags: Tree, Binary Tree, Hash Map, Divide and Conquer
Link: https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
Category: 08-binary-tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ===== 暴力解法 =====
# 思路: 递归构建，每次在inorder中线性查找根节点位置，左右子树递归构建
# 复杂度: O(n^2) time, O(n) space
def solution_brute(preorder, inorder):
    # WHY: 处理空遍历序列的情况
    if not preorder or not inorder:
        return None

    # WHY: 前序遍历的第一个节点是根节点
    root_val = preorder[0]
    root = TreeNode(root_val)

    # WHY: 在中序遍历中找到根节点位置（线性查找，O(n)）
    # WHY: 在中序序列中，根节点左侧是左子树，右侧是右子树
    root_idx = inorder.index(root_val)

    # WHY: 递归构建左子树
    # WHY: 左子树的前序序列为preorder[1:root_idx+1]，中序序列为inorder[:root_idx]
    root.left = solution_brute(preorder[1:root_idx + 1], inorder[:root_idx])

    # WHY: 递归构建右子树
    # WHY: 右子树的前序序列为preorder[root_idx+1:]，中序序列为inorder[root_idx+1:]
    root.right = solution_brute(preorder[root_idx + 1:], inorder[root_idx + 1:])

    # WHY: 返回构建好的根节点
    return root


# ===== 最优解法 =====
# 思路: 使用HashMap存储inorder的值到索引的映射，递归构建时O(1)查找根位置
# 复杂度: O(n) time, O(n) space
def solution_optimal(preorder, inorder):
    # WHY: 构建中序遍历值到索引的哈希映射，实现O(1)查找
    inorder_map = {}
    for i, val in enumerate(inorder):
        inorder_map[val] = i

    # WHY: 使用可变数组pre_idx在递归中跟踪当前前序索引
    pre_idx = [0]

    # WHY: 定义递归构建函数，使用左右边界避免数组切片
    def build(left, right):
        # WHY: 左边界超过右边界时，表示没有节点需要构建
        if left > right:
            return None

        # WHY: 根据前序索引获取当前子树的根节点值
        root_val = preorder[pre_idx[0]]
        # WHY: 递增前序索引，指向下一个子树的根
        pre_idx[0] += 1

        # WHY: 创建当前根节点
        root = TreeNode(root_val)

        # WHY: 在中序映射中查找根节点位置
        # WHY: 根节点左侧为左子树范围，右侧为右子树范围
        mid = inorder_map[root_val]

        # WHY: 先递归构建左子树（前序遍历顺序：根 -> 左 -> 右）
        root.left = build(left, mid - 1)
        # WHY: 再递归构建右子树
        root.right = build(mid + 1, right)

        # WHY: 返回构建好的根节点
        return root

    # WHY: 从完整范围[0, len(inorder)-1]开始构建
    return build(0, len(inorder) - 1)


# ===== 测试 =====
def tree_to_list(root):
    # WHY: 辅助函数：将树转换为层序遍历列表用于验证
    if not root:
        return []
    from collections import deque
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # WHY: 去除末尾的None值，保持输出简洁
    while result and result[-1] is None:
        result.pop()
    return result


if __name__ == '__main__':
    print("Testing Construct Binary Tree from Preorder and Inorder...")

    # 测试用例1: preorder=[3,9,20,15,7], inorder=[9,3,15,20,7]
    preorder1 = [3, 9, 20, 15, 7]
    inorder1 = [9, 3, 15, 20, 7]
    tree1 = solution_brute(preorder1, inorder1)
    assert tree_to_list(tree1) == [3, 9, 20, None, None, 15, 7], "测试用例1暴力解法失败"
    tree1_opt = solution_optimal(preorder1, inorder1)
    assert tree_to_list(tree1_opt) == [3, 9, 20, None, None, 15, 7], "测试用例1最优解法失败"
    print("测试用例1通过: [3,9,20,15,7], [9,3,15,20,7]")

    # 测试用例2: preorder=[-1], inorder=[-1]
    preorder2 = [-1]
    inorder2 = [-1]
    tree2 = solution_brute(preorder2, inorder2)
    assert tree_to_list(tree2) == [-1], "测试用例2暴力解法失败"
    tree2_opt = solution_optimal(preorder2, inorder2)
    assert tree_to_list(tree2_opt) == [-1], "测试用例2最优解法失败"
    print("测试用例2通过: [-1], [-1] -> [-1]")

    print("All tests passed!")
