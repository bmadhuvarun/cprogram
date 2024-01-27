from queue import PriorityQueue

def astar(graph, start, goal, heuristic):
    priority_queue = PriorityQueue()
    priority_queue.put((0, start))
    came_from = {}
    cost_so_far = {start: 0}

    while not priority_queue.empty():
        _, current = priority_queue.get()

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return list(reversed(path)), cost_so_far[goal]

        for next_node in graph[current]:
            new_cost = cost_so_far[current] + graph[current][next_node]
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + heuristic[next_node]
                priority_queue.put((priority, next_node))
                came_from[next_node] = current

    return None, None

graph = {
    'S': {'A': 1, 'G': 10},
    'A': {'B': 2, 'C': 1},
    'C': {'D':3,'G':4},
    'D': {'G':2},
    'B': {'D':3},
    'G': {}
}
start_node = 'S'
goal_node = 'G'
heuristic = {'A': 3, 'B': 4, 'C': 2, 'D': 6, 'E': 8, 'F': 2, 'H': 4, 'I': 9, 'S': 5, 'G': 0}

path, cost = astar(graph, start_node, goal_node, heuristic)
if path is not None:
    print(f'A* Path from {start_node} to {goal_node}: {path}')
    print(f'Total cost: {cost}')
else:
    print('No path found.')
