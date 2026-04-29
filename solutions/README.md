# LeetCode Hot 100 — 完整学习索引

> 按 17 个分类组织，共 100+ 题。每个题目有 Python 可运行文件（含暴力解 + 最优解 + 逐行 WHY 注释）。
> 打开 `review.html` 启动间隔重复刷题系统。

---

## 快速开始

1. **刷题系统**: 浏览器打开 `review.html` → 按分类筛选 → 写代码 → 通过/不通过
2. **Python 运行**: `cd solutions/分类名 && python 文件名.py`
3. **方法论**: 阅读 `methodology.md` 学习审题框架
4. **题目索引**: 本文件下方按分类浏览

---

## 分类索引 (17 类)

| # | 分类 | 目录 | 题数 |
|---|------|------|------|
| 01 | 哈希 | [solutions/01-hash/](solutions/01-hash/) | 3 |
| 02 | 双指针 | [solutions/02-two-pointers/](solutions/02-two-pointers/) | 4 |
| 03 | 滑动窗口 | [solutions/03-sliding-window/](solutions/03-sliding-window/) | 2 |
| 04 | 子串 | [solutions/04-substring/](solutions/04-substring/) | 3 |
| 05 | 普通数组 | [solutions/05-array/](solutions/05-array/) | 5 |
| 06 | 矩阵 | [solutions/06-matrix/](solutions/06-matrix/) | 4 |
| 07 | 链表 | [solutions/07-linked-list/](solutions/07-linked-list/) | 14 |
| 08 | 二叉树 | [solutions/08-binary-tree/](solutions/08-binary-tree/) | 15 |
| 09 | 图论 | [solutions/09-graph/](solutions/09-graph/) | 4 |
| 10 | 回溯 | [solutions/10-backtracking/](solutions/10-backtracking/) | 8 |
| 11 | 二分查找 | [solutions/11-binary-search/](solutions/11-binary-search/) | 6 |
| 12 | 栈 | [solutions/12-stack/](solutions/12-stack/) | 5 |
| 13 | 堆 | [solutions/13-heap/](solutions/13-heap/) | 3 |
| 14 | 贪心算法 | [solutions/14-greedy/](solutions/14-greedy/) | 4 |
| 15 | 动态规划 | [solutions/15-dp/](solutions/15-dp/) | 11 |
| 16 | 多维动态规划 | [solutions/16-multi-dp/](solutions/16-multi-dp/) | 5 |
| 17 | 技巧 | [solutions/17-tricks/](solutions/17-tricks/) | 5 |

---

## 完整题目列表

### 01 哈希 (3 题)

| # | 题名 | LC | 难度 | 核心技巧 |
|---|------|-----|------|---------|
| 1 | 两数之和 Two Sum | 1 | Easy | HashMap O(1) 查找 complement |
| 2 | 字母异位词分组 Group Anagrams | 49 | Medium | 字符计数数组 [26] 作为统一签名 |
| 3 | 最长连续序列 Longest Consecutive Sequence | 128 | Medium | 只从序列起点 (num-1 不存在) 向后扩展 |

### 02 双指针 (4 题)

| # | 题名 | LC | 难度 | 核心技巧 |
|---|------|-----|------|---------|
| 1 | 移动零 Move Zeroes | 283 | Easy | 同向双指针 swap |
| 2 | 盛最多水的容器 Container With Most Water | 11 | Medium | 两端收缩，移动较矮边 |
| 3 | 三数之和 3Sum | 15 | Medium | 排序 + 固定一个 + 双指针两端搜索 |
| 4 | 接雨水 Trapping Rain Water | 42 | Hard | 双指针 / 单调栈 / 前缀后缀 max |

### 03 滑动窗口 (2 题)

| # | 题名 | LC | 难度 | 核心技巧 |
|---|------|-----|------|---------|
| 1 | 无重复字符的最长子串 Longest Substring | 3 | Medium | 滑动窗口 + HashMap 记字符位置 |
| 2 | 找到字符串中所有字母异位词 Find All Anagrams | 438 | Medium | 定长窗口 + 频率数组 [26] 比较 |

### 04 子串 (3 题)

| # | 题名 | LC | 难度 | 核心技巧 |
|---|------|-----|------|---------|
| 1 | 和为 K 的子数组 Subarray Sum Equals K | 560 | Medium | 前缀和 + HashMap 频次 |
| 2 | 滑动窗口最大值 Sliding Window Maximum | 239 | Hard | 单调递减队列，队首始终最大 |
| 3 | 最小覆盖子串 Minimum Window Substring | 76 | Hard | 变长窗口 + need 计数器 |

### 05 普通数组 (5 题)

| # | 题名 | LC | 难度 | 核心技巧 |
|---|------|-----|------|---------|
| 1 | 最大子数组和 Maximum Subarray | 53 | Medium | Kadane: dp[i]=max(nums[i], dp[i-1]+nums[i]) |
| 2 | 合并区间 Merge Intervals | 56 | Medium | 按起点排序 + 一次扫描合并 |
| 3 | 轮转数组 Rotate Array | 189 | Medium | 三次反转 O(1) 空间 |
| 4 | 除自身以外数组的乘积 Product Except Self | 238 | Medium | 前缀积 × 后缀积 |
| 5 | 缺失的第一个正数 First Missing Positive | 41 | Hard | 原地哈希: x → 索引 x-1 |

### 06 矩阵 (4 题)

| # | 题名 | LC | 难度 | 核心技巧 |
|---|------|-----|------|---------|
| 1 | 矩阵置零 Set Matrix Zeroes | 73 | Medium | 首行/首列作为标记 O(1) 空间 |
| 2 | 螺旋矩阵 Spiral Matrix | 54 | Medium | 四边界 top/bottom/left/right 收缩 |
| 3 | 旋转图像 Rotate Image | 48 | Medium | 转置 + 水平翻转 = 顺时针 90° |
| 4 | 搜索二维矩阵 II Search 2D Matrix II | 240 | Medium | 从右上角开始 O(m+n) |

### 07 链表 (14 题)

| # | 题名 | LC | 难度 | 核心技巧 |
|---|------|-----|------|---------|
| 1 | 相交链表 Intersection of Two Linked Lists | 160 | Easy | 双指针消除长度差 |
| 2 | 反转链表 Reverse Linked List | 206 | Easy | 三指针迭代 / 递归 |
| 3 | 回文链表 Palindrome Linked List | 234 | Easy | 快慢找中点 + 反转后半 |
| 4 | 环形链表 Linked List Cycle | 141 | Easy | Floyd 快慢判圈 |
| 5 | 环形链表 II Linked List Cycle II | 142 | Medium | Floyd + 数学 (相遇后重置) |
| 6 | 合并两个有序链表 Merge Two Sorted Lists | 21 | Easy | Dummy 头 + 归并 |
| 7 | 两数相加 Add Two Numbers | 2 | Medium | 模拟竖式加法 + carry |
| 8 | 删除链表的倒数第 N 个结点 Remove Nth | 19 | Medium | 快慢指针间隔 n + dummy 头 |
| 9 | 两两交换链表中的节点 Swap Nodes in Pairs | 24 | Medium | 维护 prev 连接交换后的对 |
| 10 | K 个一组翻转链表 Reverse Nodes in k-Group | 25 | Hard | 分组反转 + 递归 /
迭代 |
| 11 | 随机链表的复制 Copy List with Random Pointer | 138 | Medium | HashMap 映射 / 交错插入 |
| 12 | 排序链表 Sort List | 148 | Medium | 归并排序 + 快慢找中点 |
| 13 | 合并 K 个升序链表 Merge k Sorted Lists | 23 | Hard | 小顶堆 / 分治归并 |
| 14 | LRU 缓存 LRU Cache | 146 | Medium | HashMap + 双向链表 O(1) |

### 08 二叉树 (15 题)

| # | 题名 | LC | 难度 | 核心技巧 |
|---|------|-----|------|---------|
| 1 | 二叉树的中序遍历 Inorder Traversal | 94 | Easy | 栈模拟递归 / 递归 |
| 2 | 二叉树的最大深度 Maximum Depth | 104 | Easy | DFS: max(left,right)+1 |
| 3 | 翻转二叉树 Invert Binary Tree | 226 | Easy | 递归 / BFS 交换左右 |
| 4 | 对称二叉树 Symmetric Tree | 101 | Easy | 递归比较镜像位置 |
| 5 | 二叉树的直径 Diameter of BT | 543 | Easy | DFS 同时算深度和全局直径 |
| 6 | 二叉树的层序遍历 Level Order Traversal | 102 | Medium | BFS + level_size |
| 7 | 将有序数组转换为 BST Sorted Array to BST | 108 | Easy | 二分递归，中间为根 |
| 8 | 验证二叉搜索树 Validate BST | 98 | Medium | 递归传上下界 [low,high] |
| 9 | 二叉搜索树中第 K 小的元素 Kth Smallest in BST | 230 | Medium | 中序遍历计数 |
| 10 | 二叉树的右视图 Right Side View | 199 | Medium | BFS 每层最后 / DFS 右优先 |
| 11 | 二叉树展开为链表 Flatten BT to Linked List | 114 | Medium | 后序 / 迭代: 左插到右前 |
| 12 | 从前序与中序构造 Construct from Pre+Inorder | 105 | Medium | 前序找根 + 中序分左右 |
| 13 | 路径总和 III Path Sum III | 437 | Medium | 前缀和 + DFS + HashMap |
| 14 | 二叉树的最近公共祖先 LCA | 236 | Medium | 递归: 左右都找到→当前为 LCA |
| 15 | 二叉树中的最大路径和 Maximum Path Sum | 124 | Hard | DFS 返回单边贡献 + 更新全局 |

### 09 图论 (4 题)

| # | 题名 | LC | 难度 | 核心技巧 |
|---|------|-----|------|---------|
| 1 | 岛屿数量 Number of Islands | 200 | Medium | DFS 沉岛法 / BFS |
| 2 | 腐烂的橘子 Rotting Oranges | 994 | Medium | 多源 BFS 扩散 |
| 3 | 课程表 Course Schedule | 207 | Medium | 拓扑排序: indegree + BFS |
| 4 | 实现 Trie Implement Trie | 208 | Medium | 26 叉树 / children 字典 |

### 10 回溯 (8 题)

| # | 题名 | LC | 难度 | 核心技巧 |
|---|------|-----|------|---------|
| 1 | 全排列 Permutations | 46 | Medium | used[] 数组 + 回溯 |
| 2 | 子集 Subsets | 78 | Medium | 选/不选 + 回溯 / 位掩码迭代 |
| 3 | 电话号码的字母组合 Letter Combinations | 17 | Medium | 回溯 / 队列迭代 |
| 4 | 组合总和 Combination Sum | 39 | Medium | 回溯 + start 防重复 |
| 5 | 括号生成 Generate Parentheses | 22 | Medium | 回溯: 左<n 加左，右<左 加右 |
| 6 | 单词搜索 Word Search | 79 | Medium | DFS + 回溯 + 原地标记 |
| 7 | 分割回文串 Palindrome Partitioning | 131 | Medium | 回溯 + DP 预计算回文 |
| 8 | N 皇后 N-Queens | 51 | Hard | 回溯 + 集合 O(1) 冲突检查 |

### 11 二分查找 (6 题)

| # | 题名 | LC | 难度 | 核心技巧 |
|---|------|-----|------|---------|
| 1 | 搜索插入位置 Search Insert Position | 35 | Easy | 标准二分找左边界 |
| 2 | 搜索二维矩阵 Search a 2D Matrix | 74 | Medium | 视为 1D 数组 + 二分 |
| 3 | 在排序数组中查找第一个和最后一个位置 | 34 | Medium | 两次二分：左边界 + 右边界 |
| 4 | 搜索旋转排序数组 Search in Rotated Array | 33 | Medium | 二分 + 判断哪半有序 |
| 5 | 寻找旋转排序数组中最小值 Find Min in Rotated | 153 | Medium | 二分比较 nums[mid] 和 nums[right] |
| 6 | 寻找两个正序数组的中位数 Median of Two Sorted | 4 | Hard | 二分 partition 较短数组 |

### 12 栈 (5 题)

| # | 题名 | LC | 难度 | 核心技巧 |
|---|------|-----|------|---------|
| 1 | 有效的括号 Valid Parentheses | 20 | Easy | 栈匹配 LIFO |
| 2 | 最小栈 Min Stack | 155 | Medium | 辅助栈 / 差值编码 |
| 3 | 字符串解码 Decode String | 394 | Medium | 双栈: 数字栈 + 字符串栈 |
| 4 | 每日温度 Daily Temperatures | 739 | Medium | 单调递减栈 |
| 5 | 柱状图中最大的矩形 Largest Rectangle | 84 | Hard | 单调递增栈 + 哨兵 |

### 13 堆 (3 题)

| # | 题名 | LC | 难度 | 核心技巧 |
|---|------|-----|------|---------|
| 1 | 数组中第 K 个最大元素 Kth Largest | 215 | Medium | 快速选择 / 小顶堆 |
| 2 | 前 K 个高频元素 Top K Frequent | 347 | Medium | 小顶堆 / 桶排序 |
| 3 | 数据流的中位数 Find Median from Stream | 295 | Hard | 双堆: 大顶 (小半) + 小顶 (大半) |

### 14 贪心算法 (4 题)

| # | 题名 | LC | 难度 | 核心技巧 |
|---|------|-----|------|---------|
| 1 | 买卖股票的最佳时机 Best Time to Buy & Sell | 121 | Easy | 维护最低价，O(n) |
| 2 | 跳跃游戏 Jump Game | 55 | Medium | 贪心 farthest 覆盖 |
| 3 | 跳跃游戏 II Jump Game II | 45 | Medium | BFS 思想: end 标记层边界 |
| 4 | 划分字母区间 Partition Labels | 763 | Medium | 记录最后出现位置 |

### 15 动态规划 (11 题)

| # | 题名 | LC | 难度 | 核心技巧 |
|---|------|-----|------|---------|
| 1 | 爬楼梯 Climbing Stairs | 70 | Easy | dp[i]=dp[i-1]+dp[i-2] 滚动 |
| 2 | 杨辉三角 Pascal's Triangle | 118 | Easy | dp[i][j]=dp[i-1][j-1]+dp[i-1][j] |
| 3 | 打家劫舍 House Robber | 198 | Medium | dp[i]=max(dp[i-1], dp[i-2]+nums[i]) |
| 4 | 完全平方数 Perfect Squares | 279 | Medium | dp[i]=min(dp[i-j²]+1) |
| 5 | 零钱兑换 Coin Change | 322 | Medium | 完全背包 dp |
| 6 | 单词拆分 Word Break | 139 | Medium | dp[i] 检查所有分割点 j |
| 7 | 最长递增子序列 LIS | 300 | Medium | DP O(n²) / patience sorting O(n log n) |
| 8 | 乘积最大子数组 Max Product Subarray | 152 | Medium | 同时维护 max 和 min |
| 9 | 分割等和子集 Partition Equal Subset Sum | 416 | Medium | 0-1 背包问题 |
| 10 | 最长有效括号 Longest Valid Parentheses | 32 | Hard | DP / 栈 / 双向扫描 |
| 11 | 打家劫舍 III House Robber III | 337 | Medium | 树形 DP: [rob, not_rob] |

### 16 多维动态规划 (5 题)

| # | 题名 | LC | 难度 | 核心技巧 |
|---|------|-----|------|---------|
| 1 | 不同路径 Unique Paths | 62 | Medium | dp[i][j]=dp[i-1][j]+dp[i][j-1] |
| 2 | 最小路径和 Minimum Path Sum | 64 | Medium | 同上取 min |
| 3 | 最长回文子串 Longest Palindromic Substring | 5 | Medium | 中心扩展 O(n²) / DP O(n²) |
| 4 | 最长公共子序列 LCS | 1143 | Medium | 二维 DP: match→+1, else→max |
| 5 | 编辑距离 Edit Distance | 72 | Medium | dp[i][j] = min(insert, delete, replace) |

### 17 技巧 (5 题)

| # | 题名 | LC | 难度 | 核心技巧 |
|---|------|-----|------|---------|
| 1 | 只出现一次的数字 Single Number | 136 | Easy | 异或: x^x=0, x^0=x |
| 2 | 多数元素 Majority Element | 169 | Easy | Boyer-Moore 投票 |
| 3 | 颜色分类 Sort Colors | 75 | Medium | 荷兰国旗: p0/curr/p2 三指针 |
| 4 | 下一个排列 Next Permutation | 31 | Medium | 找降序 + 交换 + 反转 |
| 5 | 寻找重复数 Find Duplicate | 287 | Medium | Floyd 判圈 / 二分统计 |

---

## 推荐刷题顺序

```
哈希 → 双指针 → 栈 → 滑动窗口 → 子串 → 普通数组 → 链表 → 二叉树
→ 二分查找 → 贪心 → 回溯 → 动态规划 → 多维DP → 图论 → 堆 → 矩阵 → 技巧
```

**原则**: 先线性的数据结构（数组、链表、栈），再树和图；先确定性算法（双指针、哈希），再"猜测验证"算法（回溯、DP）。

---

## 通用解题模板

### 审题 (前 5 分钟)
1. 数据规模 → 复杂度上限
2. 关键词 → 算法类型
3. 返回值 → 限制条件

### 编码
1. 先写暴力解 (获得正确输出)
2. 找到重复计算 → 优化
3. 检查边界 (空/单/极值)
4. 手动跑用例验证

### 刷题 (三遍法)
1. 30 分钟独立思考
2. 看题解对比差距
3. 第二天重写一次
