# ===================== 1. 定义地图数据 =====================
# 邻接表：存储城市之间的实际道路距离
romania_map = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
}

# 启发函数值：城市到 Bucharest 的**直线距离**(h值来源)
heuristic = {
    'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242,
    'Eforie': 161, 'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151,
    'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234,
    'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193, 'Sibiu': 253,
    'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374
}

# ===================== 2. A* 算法核心实现 =====================
import heapq  # 优先队列：用于每次选择 f(n) 最小的节点

def a_star(start, goal):
    # 优先队列：存储 (f值, 当前城市, 路径, g值)
    open_heap = []
    # 初始化起点：f = g(0) + h(起点)
    heapq.heappush(open_heap, (heuristic[start], start, [start], 0))

    # 闭集合：记录已处理过的节点，避免重复搜索
    closed_set = set()

    # 循环搜索：直到队列为空
    while open_heap:
        # 取出 f(n) 最小的节点
        f_current, city_current, path_current, g_current = heapq.heappop(open_heap)

        # 1. 找到终点：返回路径和总代价
        if city_current == goal:
            return path_current, g_current

        # 2. 节点已处理：跳过
        if city_current in closed_set:
            continue
        closed_set.add(city_current)

        # 3. 遍历当前城市的所有邻居
        for neighbor, cost in romania_map[city_current]:
            # 计算新的g值：起点→当前→邻居
            g_new = g_current + cost
            # 计算新的f值：g + h(邻居)
            f_new = g_new + heuristic[neighbor]
            # 新路径：在原路径基础上添加邻居城市
            path_new = path_current + [neighbor]

            # 将新节点加入优先队列
            heapq.heappush(open_heap, (f_new, neighbor, path_new, g_new))

    # 无路径可达
    return None, None

# ===================== 3. 运行算法 =====================
if __name__ == '__main__':
    start_city = 'Arad'
    goal_city = 'Bucharest'
    result_path, total_cost = a_star(start_city, goal_city)

    print(f"起点：{start_city}")
    print(f"终点：{goal_city}")
    print(f"最优路径：{' → '.join(result_path)}")
    print(f"总路程：{total_cost} km")