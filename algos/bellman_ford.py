from graph.graph import Graph    


def bellman_ford(graph, start_label):
    """
    This function implements the Bellman-Ford algorithm to find the shortest path between a start vertex and all other vertices in the graph. 

    :param graph: the graph object
    :param start_label: The label of the start vertex.
    :return: A dictionary mapping vertex labels to their distance from the start vertex.
    :rtype: dict[str, float]
    
    :raises ValueError: If the start vertex is not in the graph or if the graph contains a negative weight cycle.
    """

    start_vertex = graph.get_vertex(start_label)
    if start_vertex is None:
        raise ValueError("Start vertex not in graph")

    # Initial distance
    for vertex in graph.get_vertices().values():
        vertex.set_distance(float("inf"))
    start_vertex.set_distance(0)
    
    # Iterate over all verices
    for _ in range(len(graph.get_vertices()) - 1):
        for edge in graph.get_edges(): # Now Edges
            start_vertex = edge.get_start_vertex()
            end_vertex = edge.get_end_vertex()
            new_distance = start_vertex.get_distance() + edge.get_weight()
            if new_distance < end_vertex.get_distance():
                end_vertex.set_distance(new_distance)

    for edge in graph.get_edges():
        start_vertex = edge.get_start_vertex()
        end_vertex = edge.get_end_vertex()

        if start_vertex.get_distance() + edge.get_weight() < end_vertex.get_distance():
            raise ValueError("Graph contains negative weight cycle") # Checks for a cycle

    return {vertex.get_label(): vertex.get_distance() for vertex in graph.get_vertices().values()} # Create a dictionary key:value on wich the key is the label(a,b,c ...) and the  distance is the value. 
    # Uses a dictionary comprehantion to iterate over the values of get_vertices().values wich # contains all of the vertices in the graph. 
    # For each vertex, gets the label and then get the distance

if __name__ == "__main__":
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

    distances = bellman_ford(test_graph.get_vertex("a"))

    for vertex, distance in distances.items():
            print(f"{vertex.get_label()} has a distance of {distance} from the vertex {test_graph.source_vertex.get_label()}")

