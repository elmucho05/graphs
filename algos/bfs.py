from collections import deque

def bfs(graph, start, end):
    """
    This function finds the shortest path between two vertices of a graph using Breadth-First Search (BFS) algorithm.


    Args:
    1. graph (Graph): The graph object.
    2. start (str): The label of the start vertex.
    3. end (str): The label of the end vertex.
    
    Returns:
    int: The distance of the shortest path between the start and end vertices. If the path is not found, returns None.

    Raises:
    ValueError: If either the start or end vertex is not found in the graph.
    """
    # check if start and end vertices are present in the graph
    if start not in graph.get_vertices() or end not in graph.get_vertices():
        raise ValueError("Start or end vertex not found in graph")

    # initialize distance dictionary with infinity for all vertices
    distance = {vertex: float('inf') for vertex in graph.get_vertices()}
    distance[start] = 0

    # initialize visited set
    visited = set()

    # initialize queue with start vertex
    queue = deque([start])

    while queue:
        current_vertex = queue.popleft()

        # ignore already visited vertices
        if current_vertex in visited:
            continue

        # mark the current vertex as visited
        visited.add(current_vertex)

        # loop through all outbound edges of the current vertex
        for edge in current_vertex.get_outbound_edges():
            adjacent_vertex = edge.get_end_vertex()
            # ignore already visited adjacent vertices
            if adjacent_vertex in visited:
                continue
            new_distance = distance[current_vertex] + edge.get_weight()
            if new_distance < distance[adjacent_vertex]:
                distance[adjacent_vertex] = new_distance
                queue.append(adjacent_vertex)

    # return the distance of the end vertex
    return distance[end] if distance[end] != float('inf') else None
