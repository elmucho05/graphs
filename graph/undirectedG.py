from .graph import Graph

class UndirectedGraph(Graph):
    def __init__(self):
        super().__init__(directed=False)