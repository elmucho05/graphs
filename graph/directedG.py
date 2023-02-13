from .graph import Graph

class DirectedGraph(Graph):
    def __init__(self):
        super().__init__(directed=True)