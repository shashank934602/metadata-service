def has_cycle(graph, start, target):
    visited = set()

    def dfs(node):
        if node == target:
            return True
        visited.add(node)

        for nxt in graph.get(node, []):
            if nxt not in visited:
                if dfs(nxt):
                    return True
        return False

    return dfs(start)
