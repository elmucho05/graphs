import unittest
from graph.graph import Graph
from algos.dijkstra import dijkstra

class TestDijkstra(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.graph.add_vertex("a")
        self.graph.add_vertex("b")
        self.graph.add_vertex("c")
        self.graph.add_vertex("d")
        self.graph.add_vertex("e")
        self.graph.add_vertex("f")

        self.graph.add_edge("a", "b", 2)
        self.graph.add_edge("a", "c", 4)
        self.graph.add_edge("b", "c", 1)
        self.graph.add_edge("c", "d", 5)
        self.graph.add_edge("c", "e", 3)
        self.graph.add_edge("d", "e", 1)
        self.graph.add_edge("e", "f", 8)

    def test_dijkstra(self):
        shortest_distances_to_vertices = dijkstra(
            self.graph, self.graph.get_vertex("a"))
        self.assertEqual(shortest_distances_to_vertices["b"], 2)
        self.assertEqual(shortest_distances_to_vertices["c"], 3)
        self.assertEqual(shortest_distances_to_vertices["d"], 8)
        self.assertEqual(shortest_distances_to_vertices["e"], 4)
        self.assertEqual(shortest_distances_to_vertices["f"], 12)

if __name__ == '__main__':
    unittest.main()
