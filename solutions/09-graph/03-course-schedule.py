"""
LC 207. Course Schedule
Difficulty: Medium
Tags: Graph, Topological Sort, BFS, DFS
Link: https://leetcode.cn/problems/course-schedule/
Category: 09-graph
"""

from collections import deque, defaultdict


# ===== 暴力解法 =====
# 思路: DFS检测图中是否存在环，对每个未访问节点进行DFS遍历
# 复杂度: O(V+E) time, O(V+E) space
def solution_brute(numCourses, prerequisites):
    # WHY: 构建邻接表表示的图，每个课程指向其后续课程
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        # WHY: prereq -> course 表示先修课后修课程
        graph[prereq].append(course)

    # WHY: visited状态数组：0=未访问，1=正在访问（当前路径上），2=已访问完成
    visited = [0] * numCourses

    # WHY: 定义DFS检测环函数
    def has_cycle(node):
        # WHY: 如果当前节点正在访问路径上，说明存在环
        if visited[node] == 1:
            return True
        # WHY: 如果当前节点已经访问完成，无需重复访问
        if visited[node] == 2:
            return False

        # WHY: 标记当前节点为正在访问
        visited[node] = 1

        # WHY: 遍历当前节点的所有后续课程
        for neighbor in graph[node]:
            # WHY: 递归检测后续课程是否存在环
            if has_cycle(neighbor):
                return True

        # WHY: 标记当前节点为已访问完成
        visited[node] = 2
        # WHY: 当前路径无环
        return False

    # WHY: 对每个未访问的节点进行DFS环检测
    for i in range(numCourses):
        if visited[i] == 0:
            # WHY: 如果检测到环，则无法完成所有课程
            if has_cycle(i):
                return False

    # WHY: 无环，可以完成所有课程
    return True


# ===== 最优解法 =====
# 思路: 拓扑排序（Kahn算法），统计每个节点的入度，用队列处理入度为0的节点
# 复杂度: O(V+E) time, O(V+E) space
def solution_optimal(numCourses, prerequisites):
    # WHY: 构建邻接表和入度数组
    graph = defaultdict(list)
    indegree = [0] * numCourses

    # WHY: 遍历先修关系列表，构建图和入度
    for course, prereq in prerequisites:
        # WHY: prereq -> course 建立边
        graph[prereq].append(course)
        # WHY: course的入度+1（有一个先修课要求）
        indegree[course] += 1

    # WHY: 使用deque初始化队列，将入度为0的课程入队
    queue = deque()
    for i in range(numCourses):
        if indegree[i] == 0:
            queue.append(i)

    # WHY: count记录已处理的课程数量（可完成的课程数）
    count = 0

    # WHY: 处理队列中的课程
    while queue:
        # WHY: 取出一个入度为0的课程
        course = queue.popleft()
        # WHY: 已处理的课程数量+1
        count += 1

        # WHY: 遍历该课程的所有后续课程
        for neighbor in graph[course]:
            # WHY: 后续课程的入度-1（少了一个先修课要求）
            indegree[neighbor] -= 1
            # WHY: 如果后续课程入度变为0，加入队列
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # WHY: 如果处理的课程数等于总课程数，说明可以完成所有课程
    return count == numCourses


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Course Schedule...")

    # 测试用例1: numCourses=2, [[1,0]] -> true
    assert solution_brute(2, [[1, 0]]) == True, "测试用例1暴力解法失败"
    assert solution_optimal(2, [[1, 0]]) == True, "测试用例1最优解法失败"
    print("测试用例1通过: 2, [[1,0]] -> true")

    # 测试用例2: numCourses=2, [[1,0],[0,1]] -> false（存在环 0->1->0）
    assert solution_brute(2, [[1, 0], [0, 1]]) == False, "测试用例2暴力解法失败"
    assert solution_optimal(2, [[1, 0], [0, 1]]) == False, "测试用例2最优解法失败"
    print("测试用例2通过: 2, [[1,0],[0,1]] -> false")

    print("All tests passed!")
