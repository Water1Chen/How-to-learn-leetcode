"""
LC 200. Number of Islands
Difficulty: Medium
Tags: Graph, BFS, DFS, Union Find, Matrix
Link: https://leetcode.cn/problems/number-of-islands/
Category: 09-graph
"""


# ===== 暴力解法 =====
# 思路: 使用visited集合记录已访问的陆地格子，BFS遍历每个岛屿标记所有连通陆地
# 复杂度: O(mn) time, O(mn) space
def solution_brute(grid):
    # WHY: 处理空网格的情况
    if not grid or not grid[0]:
        return 0

    # WHY: 获取网格的行数和列数
    rows, cols = len(grid), len(grid[0])
    # WHY: visited集合记录已访问的陆地位置
    visited = set()
    # WHY: count记录岛屿数量
    count = 0

    # WHY: 定义BFS函数，从给定起点扩散标记整个岛屿
    def bfs(r, c):
        # WHY: 使用deque作为队列进行BFS
        from collections import deque
        queue = deque([(r, c)])
        # WHY: 标记起点为已访问
        visited.add((r, c))

        # WHY: 定义四个方向的偏移量（上、下、左、右）
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # WHY: 循环处理队列中的每个陆地格子
        while queue:
            # WHY: 取出队首格子
            cur_r, cur_c = queue.popleft()
            # WHY: 检查四个相邻方向
            for dr, dc in directions:
                nr, nc = cur_r + dr, cur_c + dc
                # WHY: 检查相邻格子是否在网格范围内
                if 0 <= nr < rows and 0 <= nc < cols:
                    # WHY: 如果是未访问的陆地格子
                    if grid[nr][nc] == '1' and (nr, nc) not in visited:
                        # WHY: 标记为已访问并入队
                        visited.add((nr, nc))
                        queue.append((nr, nc))

    # WHY: 遍历网格中的每个格子
    for r in range(rows):
        for c in range(cols):
            # WHY: 如果是未访问的陆地格子，发现新岛屿
            if grid[r][c] == '1' and (r, c) not in visited:
                # WHY: 岛屿计数+1
                count += 1
                # WHY: BFS标记整个岛屿的所有陆地格子
                bfs(r, c)

    # WHY: 返回岛屿总数
    return count


# ===== 最优解法 =====
# 思路: DFS沉岛算法，遇到陆地就将其连通的所有陆地沉没（标记为'0'），无需额外空间
# 复杂度: O(mn) time, O(1) extra space（原地修改网格）
def solution_optimal(grid):
    # WHY: 处理空网格的情况
    if not grid or not grid[0]:
        return 0

    # WHY: 获取网格的行数和列数
    rows, cols = len(grid), len(grid[0])
    # WHY: count记录岛屿数量
    count = 0

    # WHY: 定义DFS沉岛函数
    def sink(r, c):
        # WHY: 检查下标越界或者不是陆地，直接返回
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return
        # WHY: 将当前陆地格子沉没（标记为水）
        grid[r][c] = '0'
        # WHY: 递归沉没上、下、左、右四个方向的相邻陆地
        sink(r - 1, c)
        sink(r + 1, c)
        sink(r, c - 1)
        sink(r, c + 1)

    # WHY: 遍历网格中的每个格子
    for r in range(rows):
        for c in range(cols):
            # WHY: 遇到陆地格子，发现新岛屿
            if grid[r][c] == '1':
                # WHY: 岛屿计数+1
                count += 1
                # WHY: DFS沉没整个岛屿
                sink(r, c)

    # WHY: 返回岛屿总数
    return count


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Number of Islands...")

    # 测试用例1: 单个大岛屿
    grid1 = [
        ['1','1','1','1','0'],
        ['1','1','0','1','0'],
        ['1','1','0','0','0'],
        ['0','0','0','0','0']
    ]
    assert solution_brute([row[:] for row in grid1]) == 1, "测试用例1暴力解法失败"
    assert solution_optimal([row[:] for row in grid1]) == 1, "测试用例1最优解法失败"
    print("测试用例1通过: 1个岛屿")

    # 测试用例2: 多个岛屿
    grid2 = [
        ['1','1','0','0','0'],
        ['1','1','0','0','0'],
        ['0','0','1','0','0'],
        ['0','0','0','1','1']
    ]
    assert solution_brute([row[:] for row in grid2]) == 3, "测试用例2暴力解法失败"
    assert solution_optimal([row[:] for row in grid2]) == 3, "测试用例2最优解法失败"
    print("测试用例2通过: 3个岛屿")

    print("All tests passed!")
