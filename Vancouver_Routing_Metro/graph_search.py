# Breadth-First Search (BFS) function
def bfs(graph, start_vertex, target_value):
    # Initialize the path with the start vertex
    path = [start_vertex]

    # Create a list with the start vertex and its path
    vertex_and_path = [start_vertex, path]

    # Create a queue for BFS with the initial vertex and its path
    bfs_queue = [vertex_and_path]

    # Initialize a set to keep track of visited vertices
    visited = set()

    # Main BFS loop
    while bfs_queue:
        # Dequeue the first vertex and its path
        current_vertex, path = bfs_queue.pop(0)

        # Mark the current vertex as visited
        visited.add(current_vertex)

        # Explore neighbors
        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                # If the neighbor is the target, return the complete path
                if neighbor == target_value:
                    return path + [neighbor]
                else:
                    # Enqueue the neighbor and its extended path
                    bfs_queue.append([neighbor, path + [neighbor]])

# Depth-First Search (DFS) function
def dfs(graph, current_vertex, target_value, visited=None):
    # If visited is not provided, initialize it as an empty list
    if visited is None:
        visited = []

    # Add the current vertex to the visited list
    visited.append(current_vertex)

    # If the current vertex is the target, return the visited path
    if current_vertex == target_value:
        return visited

    # Explore neighbors recursively
    for neighbor in graph[current_vertex]:
        if neighbor not in visited:
            # Recursive call to explore the neighbor
            path = dfs(graph, neighbor, target_value, visited)

            # If a path is found, return it
            if path:
                return path
