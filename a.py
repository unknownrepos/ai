import heapq

# Graph representation using adjacency list
graph = {
    'A': {'B': 5, 'C': 9},
    'B': {'A': 5, 'D': 2, 'E': 7},
    'C': {'A': 9, 'F': 3},
    'D': {'B': 2},
    'E': {'B': 7, 'F': 8},
    'F': {'C': 3, 'E': 8}
}

# Heuristic function (straight-line distance from each node to the goal)
heuristic = {
    'A': 6,
    'B': 3,
    'C': 4,
    'D': 4,
    'E': 2,
    'F': 0
}

def astar(graph, start, goal, heuristic):
    priority_queue = []  # Priority queue for A* search
    heapq.heappush(priority_queue, (0, start))  # Push the start node into the priority queue
    visited = set()  # Set to keep track of visited nodes
    came_from = {}  # Dictionary to store the parent nodes
    g_score = {node: float('inf') for node in graph}  # Dictionary to store the cost from start to each node
    g_score[start] = 0

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)  # Pop the node with the lowest cost
        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            path.reverse()
            return path

        visited.add(current_node)
        for neighbor, cost in graph[current_node].items():
            if neighbor in visited:
                continue
            tentative_g_score = g_score[current_node] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score = g_score[neighbor] + heuristic[neighbor]  # f(n) = g(n) + h(n)
                heapq.heappush(priority_queue, (f_score, neighbor))

    return None  # If goal is not reachable from start

start_node = 'A'
goal_node = 'F'
result = astar(graph, start_node, goal_node, heuristic)

if result:
    print("Path from", start_node, "to", goal_node, ":", ' -> '.join(result))
else:
    print("Path from", start_node, "to", goal_node, "not found.")
