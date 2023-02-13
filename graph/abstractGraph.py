import abc

class AbstractGraph(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add_vertex(self, label):
        pass

    @abc.abstractmethod
    def add_edge(self, label):
        pass