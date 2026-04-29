"""
LC 337. House Robber III (打家劫舍 III)
Difficulty: Medium
Tags: Tree, Depth-First Search, Dynamic Programming, Binary Tree
Link: https://leetcode.cn/problems/house-robber-iii/
Category: 15-dp
"""

from typing import Optional, Tuple


# ===== TreeNode 定义 =====
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        # WHY: 初始化二叉树节点
        self.val = val
        self.left = left
        self.right = right


# ===== 暴力解法 =====
# 思路: 对于每个节点，递归地考虑两种情况：抢劫该节点（跳过子节点）或不抢劫该节点（可以抢劫子节点）。
#        使用记忆化搜索（memo）避免重复计算。
# 复杂度: O(n) time, O(n) space (递归栈 + memo)
def solution_brute(root: Optional[TreeNode]) -> int:
    # WHY: 使用字典作为记忆化缓存，记录每个节点对应的最大金额
    memo: dict = {}

    # WHY: 定义递归函数，计算以node为根的子树能抢到的最大金额
    def rob_node(node: Optional[TreeNode]) -> int:
        # WHY: 如果节点为空，返回0
        if node is None:
            return 0
        # WHY: 如果已经计算过该节点，直接返回缓存结果
        if node in memo:
            return memo[node]

        # WHY: 选项1：抢劫当前节点，则跳过左右子节点，但可以抢劫孙子节点
        rob_curr = node.val
        if node.left:
            rob_curr += rob_node(node.left.left) + rob_node(node.left.right)
        if node.right:
            rob_curr += rob_node(node.right.left) + rob_node(node.right.right)

        # WHY: 选项2：不抢劫当前节点，可以抢劫左右子节点
        not_rob_curr = rob_node(node.left) + rob_node(node.right)

        # WHY: 取两种选择的最大值，存入缓存
        memo[node] = max(rob_curr, not_rob_curr)
        return memo[node]

    # WHY: 从根节点开始计算
    return rob_node(root)


# ===== 最优解法 =====
# 思路: 树形DP，每个节点返回一个长度为2的数组[rob, not_rob]。
#        rob表示抢劫当前节点的最大值，not_rob表示不抢劫当前节点的最大值。
#        抢劫当前节点时：rob = node.val + left.not_rob + right.not_rob
#        不抢劫当前节点时：not_rob = max(left.rob, left.not_rob) + max(right.rob, right.not_rob)
# 复杂度: O(n) time, O(n) space (递归栈)
def solution_optimal(root: Optional[TreeNode]) -> int:
    # WHY: 定义后续遍历函数，返回[rob, not_rob]
    def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
        # WHY: 如果节点为空，抢劫和不抢劫都是0
        if node is None:
            return (0, 0)

        # WHY: 后序遍历，先处理左右子树
        left = dfs(node.left)
        right = dfs(node.right)

        # WHY: 抢劫当前节点：当前节点值 + 不抢劫左子树 + 不抢劫右子树
        rob = node.val + left[1] + right[1]
        # WHY: 不抢劫当前节点：取左右子树各自的最大值之和
        not_rob = max(left[0], left[1]) + max(right[0], right[1])

        # WHY: 返回当前节点的[抢劫, 不抢劫]结果
        return (rob, not_rob)

    # WHY: 从根节点开始计算，返回两种选择的最大值
    result = dfs(root)
    return max(result[0], result[1])


# ===== 辅助函数：根据列表构建二叉树 =====
def build_tree(values: list) -> Optional[TreeNode]:
    # WHY: 空列表返回空树
    if not values:
        return None
    # WHY: 创建根节点
    root = TreeNode(values[0])
    # WHY: 使用队列进行层序遍历构建
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        # WHY: 构建左子节点
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        # WHY: 构建右子节点
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing House Robber III...")

    # 测试用例1: [3,2,3,null,3,null,1] → 7 (3+3+1=7)
    # 树结构：
    #     3
    #    / \
    #   2   3
    #    \   \
    #     3   1
    tree1 = build_tree([3, 2, 3, None, 3, None, 1])
    expected1 = 7
    assert solution_brute(tree1) == expected1, f"brute test1 failed"
    assert solution_optimal(tree1) == expected1, f"optimal test1 failed"

    # 测试用例2: [3,4,5,1,3,null,1] → 9 (4+5=9)
    # 树结构：
    #     3
    #    / \
    #   4   5
    #  / \   \
    # 1   3   1
    tree2 = build_tree([3, 4, 5, 1, 3, None, 1])
    expected2 = 9
    assert solution_brute(tree2) == expected2, f"brute test2 failed"
    assert solution_optimal(tree2) == expected2, f"optimal test2 failed"

    # 测试用例3: 空树 → 0
    expected3 = 0
    assert solution_optimal(None) == expected3, f"optimal test3 failed"

    print(f"Brute force: {solution_brute(tree1)}")
    print("All tests passed!")
