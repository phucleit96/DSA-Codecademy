# vertex.py

class Vertex:
    def __init__(self, value):
        """
        Initialize a vertex with a given value and an empty dictionary for edges.
        """
        self.value = value
        self.edges = {}

    def add_edge(self, vertex, weight=0):
        """
        Add an edge to the vertex with an optional weight.
        """
        # Add a directed edge from this vertex to the given vertex with the specified weight
        self.edges[vertex] = weight

    def get_edges(self):
        """
        Get a list of all vertices connected to this vertex.
        """
        # Return a list of vertices connected to this vertex
        return list(self.edges.keys())
