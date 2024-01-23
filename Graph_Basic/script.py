# script.py

from random import randrange
from graph import Graph
from vertex import Vertex

def print_graph(graph):
    """
    Print the vertices and their connected edges in the graph.
    """
    for vertex in graph.graph_dict:
        print("")
        print(vertex + " connected to")
        vertex_neighbors = graph.graph_dict[vertex].edges
        if len(vertex_neighbors) == 0:
            print("No edges!")
        for adjacent_vertex in vertex_neighbors:
            print("=> " + adjacent_vertex)

def build_graph(directed):
    """
    Build a graph with vertices and random edges, then print the graph.
    """
    # Create an instance of the Graph class
    g = Graph(directed)
    # Create a list to store Vertex objects
    vertices = []

    # Create vertices and add them to the graph
    for val in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        vertex = Vertex(val)
        vertices.append(vertex)
        g.add_vertex(vertex)

    # Add random edges between vertices
    for v in range(len(vertices)):
        v_idx = randrange(0, len(vertices) - 1)
        v1 = vertices[v_idx]
        v_idx = randrange(0, len(vertices) - 1)
        v2 = vertices[v_idx]
        # Add an edge between v1 and v2 with a random weight
        g.add_edge(v1, v2, randrange(1, 10))

    # Print the graph
    print_graph(g)

# Test case
build_graph(False)
