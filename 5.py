def dl(g, start, goal, dli):
    v = set()

    def dfs(node, d, path):
        if d > dli:
            return False
        if node == goal:
            path.append(node)
            return True
        if node in v:
            return False

        v.add(node)
        for neg in g.get(node, []):
            if dfs(neg, d + 1, path):
                path.append(node)
                return True
        return False

    path = []
    result = dfs(start, 0, path)
    if result:
        path.reverse()  # Reverse the path to get it in the correct order
        print("Path found:", "->".join(path))
    else:
        print("No path")

g = {
    'a': ['b', 'c'],
    'b': ['d', 'e'],
    'c': [],
    'd': [],
    'e': []
}

start = 'a'
goal = 'd'
dli = 2

dl(g, start, goal, dli)

