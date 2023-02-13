from collections import deque

"""
The dfs function performs a depth-first search (DFS) on a graph starting from a given vertex
@param : start_vertex , is the vertex from which the DFS starts. 
@return : a list of labels of vertices visited in the order they are visited by the DFS.

The algorithm uses a stack to manage the incoming vertices. It initially adds the start_vertex to the stack and creates an empty set visited_vertices to keep track of the vertices that have already been visited. 

Then, it continuously pops a vertex from the stack, adds it to the visited_vertices set and its label to the result list, and adds all of its unvisited adjacent vertices to the stack until the stack is empty.
"""
def dfs(start_vertex):
        """
        DFS(Depth-First Search) use stack to manage incoming vertices, and creates a empty set to keep the visited vertixes. Everytime you pop a vertex, you add it to the visited_verices set. 
        
        """
        # initially, the stack contains only the start vertex and visited_vertices is empty
        stack = deque()
        stack.append(start_vertex)
        visited_vertices = set()

        result = []
        while len(stack) > 0:
            # 1. pop a vertex from the stack
            current_vertex = stack.pop()

            # 2. ignoring this vertex if it has been visited
            if current_vertex in visited_vertices:
                continue

            # 3. mark as visited, so we will not visit it anymore
            visited_vertices.add(current_vertex)
            result.append(current_vertex.get_label())

            # 4. get all adjacent vertices which HAVE NOT been visited
            adjacent_vertices = []
            for edge in current_vertex.get_outbound_edges():
                adjacent_vertex = edge.get_end_vertex()
                if adjacent_vertex not in visited_vertices:
                    adjacent_vertices.append(adjacent_vertex)

            # if necessary we may do some manipulation with adjacent_vertices, e.g. sort them
            # 5. add all adjacent vertices to the stack(DFS)
            stack.extend(adjacent_vertices)

        return result

##
# we can use this module by creating a vertices object, and calling the run function on it
# vertices = dfs(graph.get_vertex("a"))
# 
# then we iterate in that list, and print every element
# #