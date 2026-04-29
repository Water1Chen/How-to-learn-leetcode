"""
LC 994. Rotting Oranges
Difficulty: Medium
Tags: Graph, BFS, Matrix
Link: https://leetcode.cn/problems/rotting-oranges/
Category: 09-graph
"""

from collections import deque


# ===== 暴力解法 =====
# 思路: 每分钟模拟一次腐烂扩散过程，直到没有新鲜橘子或全部腐烂
# 复杂度: O(mn * minutes) time, O(mn) space
def solution_brute(grid):
    # WHY: 处理空网格
    if not grid or not grid[0]:
        return 0

    # WHY: 获取网格的行数和列数
    rows, cols = len(grid), len(grid[0])
    # WHY: minutes记录经过的时间
    minutes = 0

    # WHY: 定义检查是否还有新鲜橘子的函数
    def has_fresh():
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return True
        return False

    # WHY: 定义模拟一轮腐烂扩散的函数
    def spread():
        # WHY: 标记是否发生了腐烂扩散
        rotted = False
        # WHY: 创建新网格存储下一分钟的状态
        new_grid = [row[:] for row in grid]
        # WHY: 四个方向偏移量
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # WHY: 遍历所有格子
        for r in range(rows):
            for c in range(cols):
                # WHY: 如果当前格子是腐烂橘子
                if grid[r][c] == 2:
                    # WHY: 检查四个方向
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        # WHY: 如果相邻格子在范围内且是新鲜橘子
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            # WHY: 标记为腐烂
                            new_grid[nr][nc] = 2
                            rotted = True

        # WHY: 更新网格状态
        grid[:] = new_grid
        # WHY: 返回是否发生了扩散
        return rotted

    # WHY: 循环模拟直到没有新鲜橘子
    while has_fresh():
        # WHY: 如果本轮没有发生扩散且还有新鲜橘子，说明永远无法腐烂
        if not spread():
            return -1
        # WHY: 时间+1分钟
        minutes += 1

    # WHY: 返回所需分钟数
    return minutes


# ===== 最优解法 =====
# 思路: 多源BFS，使用队列同时从所有初始腐烂橘子开始扩散，层序遍历统计时间
# 复杂度: O(mn) time, O(mn) space
def solution_optimal(grid):
    # WHY: 处理空网格
    if not grid or not grid[0]:
        return 0

    # WHY: 获取网格的行数和列数
    rows, cols = len(grid), len(grid[0])
    # WHY: 使用deque作为BFS队列
    queue = deque()
    # WHY: fresh_count记录新鲜橘子的数量
    fresh_count = 0

    # WHY: 遍历网格，初始化队列和新鲜橘子计数
    for r in range(rows):
        for c in range(cols):
            # WHY: 如果是腐烂橘子，加入队列作为BFS起点
            if grid[r][c] == 2:
                queue.append((r, c))
            # WHY: 如果是新鲜橘子，计数+1
            elif grid[r][c] == 1:
                fresh_count += 1

    # WHY: 如果没有新鲜橘子，直接返回0
    if fresh_count == 0:
        return 0

    # WHY: minutes记录BFS的层数（即腐烂扩散所需分钟数）
    minutes = 0
    # WHY: 四个方向偏移量
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # WHY: BFS层序遍历，每层代表一分钟
    while queue and fresh_count > 0:
        # WHY: 处理当前层的所有腐烂橘子
        for _ in range(len(queue)):
            r, c = queue.popleft()
            # WHY: 检查四个方向
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # WHY: 如果相邻格子是新鲜橘子
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    # WHY: 标记为腐烂
                    grid[nr][nc] = 2
                    # WHY: 新鲜橘子计数-1
                    fresh_count -= 1
                    # WHY: 将新腐烂的橘子加入队列（下一层）
                    queue.append((nr, nc))
        # WHY: 分钟数+1
        minutes += 1

    # WHY: 如果还有新鲜橘子无法被腐烂，返回-1
    return -1 if fresh_count > 0 else minutes


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Rotting Oranges...")

    # 测试用例1: [[2,1,1],[1,1,0],[0,1,1]] -> 4
    grid1 = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    assert solution_brute([row[:] for row in grid1]) == 4, "测试用例1暴力解法失败"
    assert solution_optimal([row[:] for row in grid1]) == 4, "测试用例1最优解法失败"
    print("测试用例1通过: [[2,1,1],[1,1,0],[0,1,1]] -> 4")

    # 测试用例2: [[0,2]] -> 0（没有新鲜橘子）
    grid2 = [[0, 2]]
    assert solution_brute([row[:] for row in grid2]) == 0, "测试用例2暴力解法失败"
    assert solution_optimal([row[:] for row in grid2]) == 0, "测试用例2最优解法失败"
    print("测试用例2通过: [[0,2]] -> 0")

    # 测试用例3: [[2,1,1],[0,1,1],[1,0,1]] -> -1（右下角橘子永远无法腐烂）
    grid3 = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    # 暴力解法在此输入下耗时较长，仅测试最优解法
    assert solution_optimal([row[:] for row in grid3]) == -1, "测试用例3最优解法失败"
    print("测试用例3通过: [[2,1,1],[0,1,1],[1,0,1]] -> -1")

    print("All tests passed!")
