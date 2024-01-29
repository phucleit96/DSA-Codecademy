class Graph:
    """Represents a collection of vertices and edges."""

    def __init__(self, directed=False):
        """Initializes a graph, optionally specifying if it's directed."""
        self.graph_dict = {}  # Dictionary to store vertices
        self.directed = directed

    def add_vertex(self, vertex):
        """Adds a vertex to the graph."""
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex, weight=0):
        """Adds an edge between two vertices with an optional weight."""
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)