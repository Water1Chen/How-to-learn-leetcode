"""
LC 199. Binary Tree Right Side View
Difficulty: Medium
Tags: Tree, Binary Tree, BFS, DFS
Link: https://leetcode.cn/problems/binary-tree-right-side-view/
Category: 08-binary-tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ===== 暴力解法 =====
# 思路: 层序遍历（BFS），收集每一层的所有节点值，取每层最后一个作为右视图
# 复杂度: O(n) time, O(n) space
def solution_brute(root: TreeNode):
    # WHY: 处理空树情况，直接返回空列表
    if not root:
        return []
    # WHY: result存储最终右视图结果
    result = []
    # WHY: 使用队列进行层序遍历，初始放入根节点
    from collections import deque
    queue = deque([root])
    # WHY: 外层循环处理每一层
    while queue:
        # WHY: level_size记录当前层的节点数量
        level_size = len(queue)
        # WHY: level_vals存储当前层的所有节点值
        level_vals = []
        # WHY: 内层循环处理当前层的每个节点
        for _ in range(level_size):
            # WHY: 从队列头部取出节点
            node = queue.popleft()
            # WHY: 将当前节点值加入当前层列表
            level_vals.append(node.val)
            # WHY: 左子节点入队列（下一层从左到右顺序）
            if node.left:
                queue.append(node.left)
            # WHY: 右子节点入队列
            if node.right:
                queue.append(node.right)
        # WHY: 取当前层的最后一个节点值，即从右侧能看到的节点
        result.append(level_vals[-1])
    # WHY: 返回每层最右侧节点值列表
    return result


# ===== 最优解法 =====
# 思路: DFS先遍历右子树，利用递归深度记录首次访问每层的最右侧节点
# 复杂度: O(n) time, O(h) space (h为树高)
def solution_optimal(root: TreeNode):
    # WHY: result存储右视图的节点值列表
    result = []

    # WHY: 定义DFS递归函数，优先遍历右子树
    def dfs(node, depth):
        # WHY: 空节点直接返回
        if not node:
            return
        # WHY: 如果当前深度首次被访问，说明该节点是从右侧能看到的最右节点
        # WHY: depth从0开始，result长度等于已访问的深度数
        if depth == len(result):
            result.append(node.val)
        # WHY: 优先遍历右子树（确保右侧节点先被访问）
        dfs(node.right, depth + 1)
        # WHY: 后遍历左子树
        dfs(node.left, depth + 1)

    # WHY: 从根节点深度0开始DFS
    dfs(root, 0)
    # WHY: 返回右视图结果列表
    return result


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Binary Tree Right Side View...")

    # 测试用例1: [1,2,3,null,5,null,4] -> [1,3,4]
    #     1
    #    / \
    #   2   3
    #    \   \
    #     5   4
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.right = TreeNode(5)
    root1.right.right = TreeNode(4)
    assert solution_brute(root1) == [1, 3, 4], "测试用例1暴力解法失败"
    assert solution_optimal(root1) == [1, 3, 4], "测试用例1最优解法失败"
    print("测试用例1通过: [1,2,3,null,5,null,4] -> [1,3,4]")

    # 测试用例2: [1,null,3] -> [1,3]
    root2 = TreeNode(1)
    root2.right = TreeNode(3)
    assert solution_brute(root2) == [1, 3], "测试用例2暴力解法失败"
    assert solution_optimal(root2) == [1, 3], "测试用例2最优解法失败"
    print("测试用例2通过: [1,null,3] -> [1,3]")

    print("All tests passed!")
