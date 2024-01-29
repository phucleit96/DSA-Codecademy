# Import necessary modules
from math import inf, sqrt  # Provide mathematical functions
from heapq import heappop, heappush  # Offer priority queue functions

# Import graph data (assumed to be defined elsewhere)
from manhattan_graph import manhattan_graph, penn_station, grand_central_station
from euclidean_graph import euclidean_graph, bengaluru, jaipur

# Define heuristic functions for estimating distances
def heuristic(start, target):  # Manhattan heuristic (sum of absolute coordinate differences)
    x_distance = abs(start.position[0] - target.position[0])
    y_distance = abs(start.position[1] - target.position[1])
    return x_distance + y_distance

# def heuristic(start, target):  # Euclidean heuristic (straight-line distance, commented out)
#     x_distance = abs(start.position[0] - target.position[0])
#     y_distance = abs(start.position[1] - target.position[1])
#     return sqrt(x_distance * x_distance + y_distance * y_distance)

# Implement the A* algorithm for pathfinding
def a_star(graph, start, target):
    print("Starting A* algorithm!")  # Print initialization message

    count = 0  # Track exploration steps
    paths_and_distances = {}  # Store distances and paths for each vertex

    # Initialize distances to infinity and paths to start vertex for all vertices
    for vertex in graph:
        paths_and_distances[vertex] = [inf, [start.name]]

    # Set start vertex's distance to 0
    paths_and_distances[start][0] = 0

    vertices_to_explore = [(0, start)]  # Create priority queue using a min-heap

    # Explore vertices until target is reached or no more vertices to explore
    while vertices_to_explore and paths_and_distances[target][0] == inf:
        current_distance, current_vertex = heappop(vertices_to_explore)  # Pop vertex with lowest priority

        for neighbor, edge_weight in graph[current_vertex]:  # Explore neighbors
            new_distance = current_distance + edge_weight + heuristic(neighbor, target)  # Estimate total distance
            new_path = paths_and_distances[current_vertex][1] + [neighbor.name]  # Create new path

            if new_distance < paths_and_distances[neighbor][0]:  # Update if new path is better
                paths_and_distances[neighbor][0] = new_distance
                paths_and_distances[neighbor][1] = new_path
                heappush(vertices_to_explore, (new_distance, neighbor))  # Add neighbor to explore later
                count += 1  # Increment exploration count
                print("\nAt " + vertices_to_explore[0][1].name)  # Print current vertex being explored

    # Print path found and return it
    print("Found a path from {0} to {1} in {2} steps: ".format(start.name, target.name, count), paths_and_distances[target][1])

    return paths_and_distances[target][1]

# Call a_star() on manhattan_graph to find the best route
# from penn_station to grand_central_station:
a_star(manhattan_graph, penn_station, grand_central_station)

"""
Starting A* algorithm!

At Manhattan Mall

At 34th Street and 7th Avenue

At Manhattan Mall

At Manhattan Mall

At Macy's

At Herald Square

At Herald Square

At 33rd Street and 5th Avenue

At 36th Street and 7th Avenue

At 35th Street and 6th Avenue

At 35th Street and 6th Avenue

At Empire State Building

At 33rd Street and Madison Avenue

At 36th Street and 6th Avenue

At 36th Street and 6th Avenue

At CUNY Graduate Center

At 34th Street and Madison Avenue

At 37th Street and 6th Avenue

At 37th Street and 6th Avenue

At 36th Street and 5th Avenue

At 35th Street and Madison Avenue

At 38th Street and Sixth Avenue

At 38th Street and Sixth Avenue

At 37th Street and 5th Avenue

At 36th Street and Madison Avenue

At 39th Street and Sixth Avenue

At 39th Street and Sixth Avenue

At 38th Street and Fifth Avenue

At Times Square

At Morgan Library and Museum

At Morgan Library and Museum

At 39th Street and Fifth Avenue

At Times Square - North

At 38th Street and Madison Avenue

At Bryant Park North

At Mexican Consulate General

At New York Public Library

At 41st Street and Madison Avenue

At 41st Street and Madison Avenue
Found a path from Penn Station to Grand Central Station in 39 
steps:  ['Penn Station', '34th Street and 7th Avenue', "Macy's", 
'36th Street and 7th Avenue', '37th Street and 7th Avenue', 
'38th Street and Seventh Avenue', '39th Street and Seventh Avenue',
 'Times Square - South', 'Times Square', 'Times Square - North', 
 'Bryant Park North', 'New York Public Library', 'Grand Central 
 Station']
"""