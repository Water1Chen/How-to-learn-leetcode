"""
LC 108. 将有序数组转换为二叉搜索树 (Convert Sorted Array to BST)
Difficulty: Easy
Tags: Tree, Binary Search Tree, Array, Divide and Conquer, Binary Tree
Link: https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/
Category: 08-binary-tree
"""


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right


# ===== 暴力解法 (Sequential Insert) =====
# 思路: 逐个插入节点，但每次插入需要寻找插入位置，且无法保证
#       树的平衡性。最坏情况下退化为链表。
# 复杂度: O(n²) time in worst case, O(n) space
def solution_brute(nums: list[int]) -> TreeNode | None:
    # WHY: 辅助函数：将值 val 插入到以 root 为根的 BST 中
    def insert(root: TreeNode | None, val: int) -> TreeNode:
        if not root:
            # WHY: 空位置创建新节点
            return TreeNode(val)
        # WHY: 根据 BST 性质决定插入左子树还是右子树
        if val < root.val:
            root.left = insert(root.left, val)
        else:
            root.right = insert(root.right, val)
        return root

    if not nums:
        return None

    # WHY: 以第一个元素为根节点
    root = TreeNode(nums[0])
    # WHY: 逐个插入剩余元素，无法保证树的平衡性
    for v in nums[1:]:
        insert(root, v)

    return root


# ===== 最优解法 (Binary Partition / Divide and Conquer) =====
# 思路: 每次取数组的中间元素作为根节点，左半部分递归构建左子树，
#       右半部分递归构建右子树。因为数组已排序，这样构建的 BST
#       一定是平衡的（左右子树节点数最多相差 1）。
# 复杂度: O(n) time, O(log n) space (递归栈，因为生成的是平衡树)
def solution_optimal(nums: list[int]) -> TreeNode | None:
    # WHY: 辅助函数构建闭区间 [left, right] 上的平衡 BST
    def build(left: int, right: int) -> TreeNode | None:
        # WHY: 区间无效时返回 None，终止递归
        if left > right:
            return None

        # WHY: 选择中间元素作为根节点，保证平衡性
        # WHY: mid = (left + right) // 2 也可，取右中位或左中位都可以
        mid = (left + right) // 2

        # WHY: 创建根节点，值为中间元素
        root = TreeNode(nums[mid])

        # WHY: 递归构建左子树，范围是 [left, mid-1]
        root.left = build(left, mid - 1)
        # WHY: 递归构建右子树，范围是 [mid+1, right]
        root.right = build(mid + 1, right)

        # WHY: 返回构建好的子树根节点
        return root

    # WHY: 从整个数组区间 [0, len(nums)-1] 开始构建
    return build(0, len(nums) - 1)


# ===== 辅助函数 =====
def tree_to_inorder(root: TreeNode | None) -> list[int]:
    """中序遍历转数组，用于验证结果是否为 BST 且包含所有值"""
    result: list[int] = []
    def inorder(node: TreeNode | None) -> None:
        if not node:
            return
        inorder(node.left)
        result.append(node.val)
        inorder(node.right)
    inorder(root)
    return result


def tree_height(root: TreeNode | None) -> int:
    """计算树高，辅助验证平衡性"""
    if not root:
        return 0
    left_h = tree_height(root.left)
    right_h = tree_height(root.right)
    return max(left_h, right_h) + 1


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Convert Sorted Array to BST...")

    # Test 1: [-10,-3,0,5,9] 可能的结果之一是 [0,-10,5,null,-3,null,9]
    nums1 = [-10, -3, 0, 5, 9]
    root1 = solution_optimal(nums1)
    # WHY: 中序遍历应该得到升序数组（验证 BST 性质）
    assert tree_to_inorder(root1) == nums1, "Test 1: BST property failed!"
    # WHY: 检查平衡性：高度差不应超过 1
    assert abs(tree_height(root1.left) - tree_height(root1.right)) <= 1, \
        "Test 1: Not balanced!"

    # Test 2: [1,3] -> 可能的结构是 1->3 或 3->1
    nums2 = [1, 3]
    root2 = solution_optimal(nums2)
    assert tree_to_inorder(root2) == nums2, "Test 2: BST property failed!"
    assert abs(tree_height(root2.left) - tree_height(root2.right)) <= 1, \
        "Test 2: Not balanced!"

    # Test 3: 空数组 -> None
    root3 = solution_optimal([])
    assert root3 is None, "Test 3 failed!"

    # Test 4: [1] -> 只有一个节点
    root4 = solution_optimal([1])
    assert tree_to_inorder(root4) == [1], "Test 4 failed!"

    print("All tests passed!")
