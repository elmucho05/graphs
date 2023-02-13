import unittest
from graph.graph import Graph
from algos.bellman_ford import bellman_ford

class TestBellmanFord(unittest.TestCase):
    def test_bellman_ford(self):
        test_graph = Graph()

        test_graph.add_vertex("a")
        test_graph.add_vertex("b")
        test_graph.add_vertex("c")
        test_graph.add_vertex("d")
        test_graph.add_vertex("e")
        test_graph.add_vertex("f")

        test_graph.add_edge("a", "b", 2)
        test_graph.add_edge("a", "c", 4)
        test_graph.add_edge("b", "c", 1)
        test_graph.add_edge("c", "d", 5)
        test_graph.add_edge("c", "e", 3)
        test_graph.add_edge("d", "e", 1)
        test_graph.add_edge("e", "f", 8)

        distances = bellman_ford(test_graph, "a")
        expected_distances = {'a': 0, 'b': 2, 'c': 1, 'd': 6, 'e': 4, 'f': 12}
        self.assertEqual(distances, expected_distances)

if __name__ == '__main__':
    unittest.main()
