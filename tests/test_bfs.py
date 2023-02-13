import unittest
from collections import deque
from algos.bfs import bfs
from graph.graph import Graph

class TestBFS(unittest.TestCase):
    def test_valid_input(self):
        # Create a sample graph object for testing purposes
        graph = Graph()

        # Add vertices and edges to the graph
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_vertex("C")
        graph.add_edge("A", "B", 1)
        graph.add_edge("B", "C", 2)

        # Test the bfs function with valid input
        result = bfs(graph, graph.get_vertex("A"), graph.get_vertex("C"))
        self.assertEqual(result, 3)

    def test_start_vertex_not_found(self):
        # Create a sample graph object for testing purposes
        graph = Graph()

        # Add vertices and edges to the graph
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_vertex("C")
        graph.add_edge("A", "B", 1)
        graph.add_edge("B", "C", 2)

        # Test the bfs function with start vertex not found
        with self.assertRaises(ValueError) as context:
            bfs(graph, graph.get_vertex("D"), graph.get_vertex("C"))

        self.assertEqual(str(context.exception), "Start or end vertex not found in graph")

    def test_end_vertex_not_found(self):
        # Create a sample graph object for testing purposes
        graph = Graph()

        # Add vertices and edges to the graph
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_vertex("C")
        graph.add_edge("A", "B", 1)
        graph.add_edge("B", "C", 2)

        # Test the bfs function with end vertex not found
        with self.assertRaises(ValueError) as context:
            bfs(graph, graph.get_vertex("A"), graph.get_vertex("D"))

        self.assertEqual(str(context.exception), "Start or end vertex not found in graph")

    def test_no_path_found(self):
        # Create a sample graph object for testing purposes
        graph = Graph()

        # Add vertices and edges to the graph
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_vertex("C")
        graph.add_edge("A", "B", 1)
        graph.add_edge("B", "C", 2)

        # Test the bfs function with no path found
        result = bfs(graph, graph.get_vertex("C"), graph.get_vertex("A"))
        self.assertEqual(result, None)

if __name__ == "__main__":
    unittest.main()

