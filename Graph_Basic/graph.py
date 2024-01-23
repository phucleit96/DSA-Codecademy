# graph.py

class Graph:
    def __init__(self, directed=False):
        """
        Initialize a graph with an empty dictionary for vertices and a directed flag.
        """
        # Dictionary to store vertices and their edges
        self.graph_dict = {}
        # Flag indicating whether the graph is directed or undirected
        self.directed = directed

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        # Add a vertex to the graph dictionary with its value as the key
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex, weight=0):
        """
        Add an edge between two vertices with an optional weight.
        """
        # Add a directed edge from 'from_vertex' to 'to_vertex' with the specified weight
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
        # If the graph is undirected, add an edge in the opposite direction as well
        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

    def find_path(self, start_vertex, end_vertex):
        """
        Find a path between two vertices using breadth-first search.
        """
        # Initialize a queue with the start vertex
        start = [start_vertex]
        # Dictionary to track visited vertices
        seen = {}
        while len(start) > 0:
            # Pop the first vertex from the queue
            current_vertex = start.pop(0)
            # Mark the vertex as visited
            seen[current_vertex] = True
            print("Visiting " + current_vertex)
            # Check if the current vertex is the end vertex
            if current_vertex == end_vertex:
                return True
            else:
                # Get the set of vertices to visit from the current vertex
                vertices_to_visit = set(self.graph_dict[current_vertex].edges.keys())
                # Add vertices to the queue if they haven't been visited
                start += [vertex for vertex in vertices_to_visit if vertex not in seen]
        # No path found
        return False
