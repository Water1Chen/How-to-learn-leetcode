"""
LC 437. Path Sum III
Difficulty: Medium
Tags: Tree, Binary Tree, Hash Map, Prefix Sum, DFS
Link: https://leetcode.cn/problems/path-sum-iii/
Category: 08-binary-tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ===== 暴力解法 =====
# 思路: 以每个节点为起点，DFS遍历所有可能路径，统计和等于target的路径数
# 复杂度: O(n^2) time, O(h) space (h为树高)
def solution_brute(root: TreeNode, targetSum: int) -> int:
    # WHY: 处理空树情况
    if not root:
        return 0

    # WHY: 定义从指定节点出发的DFS路径计数函数
    def dfs_from_node(node, current_sum):
        # WHY: 空节点返回0
        if not node:
            return 0
        # WHY: 计算包含当前节点值的路径和
        current_sum += node.val
        # WHY: 如果当前路径和等于目标值，计数为1，否则为0
        count = 1 if current_sum == targetSum else 0
        # WHY: 递归统计左子树中从当前节点出发满足条件的路径数
        count += dfs_from_node(node.left, current_sum)
        # WHY: 递归统计右子树中从当前节点出发满足条件的路径数
        count += dfs_from_node(node.right, current_sum)
        # WHY: 返回从该节点出发的满足条件的路径总数
        return count

    # WHY: 从当前节点出发统计路径数
    result = dfs_from_node(root, 0)
    # WHY: 递归处理左子树中的每个节点作为起点
    result += solution_brute(root.left, targetSum)
    # WHY: 递归处理右子树中的每个节点作为起点
    result += solution_brute(root.right, targetSum)
    # WHY: 返回所有路径的总数
    return result


# ===== 最优解法 =====
# 思路: 前缀和 + 哈希表，在DFS过程中记录根到当前节点的路径和
# 思路: 当前路径和 - targetSum = 之前某前缀和，说明中间这段路径和为targetSum
# 复杂度: O(n) time, O(n) space
def solution_optimal(root: TreeNode, targetSum: int) -> int:
    # WHY: 哈希表存储前缀和出现的次数，初始放入前缀和0出现1次（代表空路径）
    prefix_sum_count = {0: 1}
    # WHY: result存储满足条件的路径总数
    result = [0]

    # WHY: 定义DFS递归函数，同时维护当前路径和
    def dfs(node, current_sum):
        # WHY: 空节点直接返回
        if not node:
            return

        # WHY: 更新当前路径和（加入当前节点值）
        current_sum += node.val

        # WHY: 核心检查：current_sum - targetSum是否在哈希表中
        # WHY: 如果有，说明存在从某个祖先节点到当前节点的路径和为targetSum
        result[0] += prefix_sum_count.get(current_sum - targetSum, 0)

        # WHY: 将当前前缀和加入哈希表（为后续节点使用），计数+1
        prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1

        # WHY: 递归遍历左子树
        dfs(node.left, current_sum)
        # WHY: 递归遍历右子树
        dfs(node.right, current_sum)

        # WHY: 回溯：从哈希表中移除当前前缀和的一次计数
        # WHY: 因为回到父节点后，当前路径不再有效，避免影响兄弟子树
        prefix_sum_count[current_sum] -= 1

    # WHY: 从根节点开始DFS，初始路径和为0
    dfs(root, 0)
    # WHY: 返回满足条件的路径总数
    return result[0]


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Path Sum III...")

    # 测试用例1: [10,5,-3,3,2,null,11,3,-2,null,1], targetSum=8 -> 3
    # 路径: 5->3, 5->2->1, -3->11
    root1 = TreeNode(10)
    root1.left = TreeNode(5)
    root1.right = TreeNode(-3)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(2)
    root1.right.right = TreeNode(11)
    root1.left.left.left = TreeNode(3)
    root1.left.left.right = TreeNode(-2)
    root1.left.right.right = TreeNode(1)
    assert solution_brute(root1, 8) == 3, "测试用例1暴力解法失败"
    assert solution_optimal(root1, 8) == 3, "测试用例1最优解法失败"
    print("测试用例1通过: targetSum=8 -> 3")

    # 测试用例2: [1,-2,-3,1,3,-2,null,-1], targetSum=-1 -> 4
    root2 = TreeNode(1)
    root2.left = TreeNode(-2)
    root2.right = TreeNode(-3)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(3)
    root2.right.left = TreeNode(-2)
    root2.left.left.left = TreeNode(-1)
    assert solution_brute(root2, -1) == 4, "测试用例2暴力解法失败"
    assert solution_optimal(root2, -1) == 4, "测试用例2最优解法失败"
    print("测试用例2通过: targetSum=-1 -> 4")

    print("All tests passed!")
