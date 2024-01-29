import random
from random import randrange
from Graph import Graph
from Vertex import Vertex


# Functions for printing, building a sample graph, and checking visited vertices
def print_graph(graph):
    """Prints a visual representation of the graph."""
    for vertex in graph.graph_dict:
        print("")
        print(vertex + " connected to")
        vertex_neighbors = graph.graph_dict[vertex].edges
        if len(vertex_neighbors) == 0:
            print("No edges!")
        for adjacent_vertex in vertex_neighbors:
            print("=> " + adjacent_vertex)

def build_tsp_graph(directed):
  g = Graph(directed)
  vertices = []
  for val in ['a', 'b', 'c', 'd']:
    vertex = Vertex(val)
    vertices.append(vertex)
    g.add_vertex(vertex)

  g.add_edge(vertices[0], vertices[1], 3)
  g.add_edge(vertices[0], vertices[2], 4)
  g.add_edge(vertices[0], vertices[3], 5)
  g.add_edge(vertices[1], vertices[0], 3)
  g.add_edge(vertices[1], vertices[2], 2)
  g.add_edge(vertices[1], vertices[3], 6)
  g.add_edge(vertices[2], vertices[0], 4)
  g.add_edge(vertices[2], vertices[1], 2)
  g.add_edge(vertices[2], vertices[3], 1)
  g.add_edge(vertices[3], vertices[0], 5)
  g.add_edge(vertices[3], vertices[1], 6)
  g.add_edge(vertices[3], vertices[2], 1)
  return g

def visited_all_nodes(visited_vertices):
    """Checks if all vertices have been visited."""
    for vertex in visited_vertices:
        if visited_vertices[vertex] == "unvisited":
            return False
    return True

# Function to address the Traveling Salesperson Problem
def traveling_salesperson(graph):
    """
    Attempts to find a solution to the Traveling Salesperson Problem (TSP)
    using a greedy approach.
    """

    ts_path = ""  # String to store the TSP path
    visited_vertices = {x: "unvisited" for x in graph.graph_dict}  # Track visited vertices

    # Start at a random vertex
    current_vertex = random.choice(list(graph.graph_dict))
    visited_vertices[current_vertex] = "visited"
    ts_path += current_vertex

    # Continue until all vertices are visited
    while not visited_all_nodes(visited_vertices):

        # Get edges and weights for the current vertex
        current_vertex_edges = graph.graph_dict[current_vertex].get_edges()
        current_vertex_edge_weights = {}  # Dictionary to store edge weights
        for edge in current_vertex_edges:
            current_vertex_edge_weights[edge] = graph.graph_dict[current_vertex].get_edge_weights(edge)

        # Find the unvisited vertex with the smallest edge weight
        found_next_vertex = False
        next_vertex = ""
        while not found_next_vertex:
            # Greedy choice: Pick the unvisited vertex with the smallest edge weight
            next_vertex = min(current_vertex_edge_weights, key =current_vertex_edge_weights.get)
            if visited_vertices[next_vertex] == "visited":
                # If the chosen vertex is already visited, remove it from consideration
                current_vertex_edge_weights.pop(next_vertex)
            else:
                found_next_vertex = True

        # If all edges from the current vertex lead to visited vertices, we're done
        if current_vertex_edge_weights is None:
            visited_all_vertices = True
        else:
            # Update current vertex and path
            current_vertex = next_vertex
            visited_vertices[current_vertex] = "visited"
            ts_path += current_vertex

    print(ts_path)  # Print the final TSP path

graph = build_tsp_graph(False)
traveling_salesperson(graph)