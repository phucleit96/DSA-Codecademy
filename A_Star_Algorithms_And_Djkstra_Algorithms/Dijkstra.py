# Import necessary modules
from heapq import heappop, heappush  # Provide priority queue functions
from math import inf  # Provide the infinity constant

# Define the graph using a dictionary
graph = {
    'A': [('B', 10), ('C', 3)],  # Vertex 'A' connects to 'B' with weight 10, and 'C' with weight 3
    'C': [('D', 2)],  # Vertex 'C' connects to 'D' with weight 2
    'D': [('E', 10)],  # Vertex 'D' connects to 'E' with weight 10
    'E': [('A', 7)],  # Vertex 'E' connects to 'A' with weight 7
    'B': [('C', 3), ('D', 2)]  # Vertex 'B' connects to 'C' with weight 3, and 'D' with weight 2
}

# Implement Dijkstra's algorithm for finding shortest paths
def dijkstras(graph, start):
    distances = {}  # Store shortest distances from the start vertex

    # Initialize distances to infinity for all vertices
    for vertex in graph:
        distances[vertex] = inf

    # Set the start vertex's distance to 0
    distances[start] = 0

    # Create a priority queue to efficiently explore vertices
    vertices_to_explore = [(0, start)]

    # Explore vertices until there are none left
    while vertices_to_explore:
        # Get the vertex with the shortest known distance
        current_distance, current_vertex = heappop(vertices_to_explore)

        # Explore neighbors of the current vertex
        for neighbor, edge_weight in graph[current_vertex]:
            # Calculate potential new distance to the neighbor
            new_distance = current_distance + edge_weight

            # Update distance if a shorter path is found
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heappush(vertices_to_explore, (new_distance, neighbor))

    # Return the calculated shortest distances
    return distances

# Calculate shortest distances from vertex 'D'
distances_from_d = dijkstras(graph, 'D')

# Print the results
print("\n\nShortest Distances: {0}".format(distances_from_d))

"Shortest Distances: {'A': 17, 'C': 20, 'D': 0, 'E': 10, 'B': 27}"