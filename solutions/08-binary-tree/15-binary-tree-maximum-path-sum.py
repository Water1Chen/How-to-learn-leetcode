"""
LC 124. Binary Tree Maximum Path Sum
Difficulty: Hard
Tags: Tree, Binary Tree, DFS, Dynamic Programming
Link: https://leetcode.cn/problems/binary-tree-maximum-path-sum/
Category: 08-binary-tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ===== 暴力解法 =====
# 思路: 枚举每个节点作为路径最高点，计算经过该节点的最大路径和，取全局最大值
# 复杂度: O(n^2) time, O(h) space
def solution_brute(root: TreeNode) -> int:
    # WHY: 计算以node为起点向下的最大单侧路径和（不拐弯）
    def max_downward(node):
        # WHY: 空节点贡献值为0
        if not node:
            return 0
        # WHY: 取左子树最大向下路径和（负数贡献取0，表示不选该分支）
        left_gain = max(0, max_downward(node.left))
        # WHY: 取右子树最大向下路径和
        right_gain = max(0, max_downward(node.right))
        # WHY: 返回当前节点值加上较大的单侧分支
        return node.val + max(left_gain, right_gain)

    # WHY: 遍历所有节点，计算以该节点为最高点的路径和
    def dfs(node):
        # WHY: 空节点返回负无穷（不影响全局最大值）
        if not node:
            return float('-inf')
        # WHY: 计算经过当前节点的最大路径和（左右两侧都取正增益）
        left_gain = max(0, max_downward(node.left))
        right_gain = max(0, max_downward(node.right))
        current_max = node.val + left_gain + right_gain
        # WHY: 返回当前节点路径和、左子树最大路径和、右子树最大路径和中的最大值
        return max(current_max, dfs(node.left), dfs(node.right))

    # WHY: 从根节点开始遍历统计最大路径和
    return dfs(root)


# ===== 最优解法 =====
# 思路: 一次DFS，每个节点返回经过该节点向下的最大单侧贡献，同时更新全局最大路径和
# 复杂度: O(n) time, O(h) space
def solution_optimal(root: TreeNode) -> int:
    # WHY: 全局最大路径和，初始化为最小可能值
    max_sum = [float('-inf')]

    # WHY: DFS返回以当前节点为起点的最大单侧路径和（不拐弯，供父节点使用）
    def max_gain(node):
        # WHY: 空节点贡献值为0
        if not node:
            return 0

        # WHY: 递归计算左子树的最大单侧贡献（负数则取0，代表不选该分支）
        left_gain = max(0, max_gain(node.left))
        # WHY: 递归计算右子树的最大单侧贡献
        right_gain = max(0, max_gain(node.right))

        # WHY: 经过当前节点且不向上延伸的路径和 = 节点值 + 左右最大贡献
        # WHY: 这条路径以当前节点为最高点，左右子树分别贡献
        current_path_sum = node.val + left_gain + right_gain

        # WHY: 更新全局最大路径和
        max_sum[0] = max(max_sum[0], current_path_sum)

        # WHY: 返回当前节点向上的最大单侧贡献
        # WHY: 只能选择左或右中较大的一侧，因为路径不能分叉
        return node.val + max(left_gain, right_gain)

    # WHY: 从根节点开始DFS
    max_gain(root)
    # WHY: 返回全局最大路径和
    return max_sum[0]


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Binary Tree Maximum Path Sum...")

    # 测试用例1: [-10,9,20,null,null,15,7] -> 42
    #   -10
    #   / \
    #  9   20
    #      / \
    #     15  7
    # 路径: 15->20->7 = 42
    root1 = TreeNode(-10)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    assert solution_brute(root1) == 42, "测试用例1暴力解法失败"
    assert solution_optimal(root1) == 42, "测试用例1最优解法失败"
    print("测试用例1通过: [-10,9,20,null,null,15,7] -> 42")

    # 测试用例2: [2,-1] -> 2
    #   2
    #  /
    # -1
    root2 = TreeNode(2)
    root2.left = TreeNode(-1)
    assert solution_brute(root2) == 2, "测试用例2暴力解法失败"
    assert solution_optimal(root2) == 2, "测试用例2最优解法失败"
    print("测试用例2通过: [2,-1] -> 2")

    print("All tests passed!")
