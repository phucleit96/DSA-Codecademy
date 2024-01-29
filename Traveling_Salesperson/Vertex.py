# Define classes to represent vertices and graphs

class Vertex:
    """Represents a node in the graph."""

    def __init__(self, value):
        """Initializes a vertex with a value."""
        self.value = value
        self.edges = {}  # Dictionary to store connections to other vertices

    def add_edge(self, vertex, weight=0):
        """Adds a connection (edge) to another vertex with an optional weight."""
        self.edges[vertex] = weight

    def get_edges(self):
        """Returns a list of connected vertices."""
        return list(self.edges.keys())

    def get_edge_weights(self, edge):
        """Returns the weight of a specific edge."""
        return self.edges[edge]
